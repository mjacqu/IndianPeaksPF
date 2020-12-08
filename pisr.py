import numpy as np
import glimpse
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1 import make_axes_locatable


#scale aspect to 0 (N) to 1 (S):
aspect = glimpse.Raster.read('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/terrain/Aspect.tif')
aspect.Z[aspect.Z == -1] = np.nan
aspect.Z[aspect.Z > 180] = np.abs(aspect.Z[aspect.Z > 180] - 360)
aspect.Z = aspect.Z/180 #aspect scaled between 0 and 1

#plt.imshow(aspect.Z)
#plt.show()

# Build solar radiation grid
slope = glimpse.Raster.read('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/terrain/Slope.tif')
summer_rad = glimpse.Raster.read('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/solar/AreaSol_Jun_Nov.tif')
spring_rad = glimpse.Raster.read('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/solar/AreaSol_Jan_May.tif')
winter_rad = glimpse.Raster.read('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/solar/AreaSol_Dec.tif')

full_rad = glimpse.Raster(winter_rad.Z + spring_rad.Z + summer_rad.Z)

scaled_rad = full_rad.copy()

scaled_rad.Z[:-1,:-1][slope.Z < 40] = summer_rad.Z[:-1,:-1][slope.Z < 40]
scaled_rad.Z[:-1,:-1][slope.Z >= 40] = full_rad.Z[:-1,:-1][slope.Z > 40] * aspect.Z[:-1,:-1][slope.Z > 40]

#calculate MAGT:
elevation = glimpse.Raster.read('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/terrain/niwot_dem_UTM.tif')
dh = 1100# dh is rough elevation difference of zero-degree isoline between CO and Switzerland (see calc for CO in hobo_data.py).
MAGT = glimpse.Raster(19.497+4.532e-6 *scaled_rad.Z - 0.008043*(elevation.Z-dh), x=elevation.x, y = elevation.y)


#load sensor locations
sensors = pd.read_csv('/Users/mistral/Documents/CUBoulder/Science/permafrost/data/metadata/sensor_locations.csv')
geo_sensors = gpd.GeoDataFrame(sensors, geometry = gpd.points_from_xy(sensors.long_W, sensors.lat_N))
geo_sensors.crs = 'EPSG:4326'
geo_sensors = geo_sensors.to_crs("EPSG:26913")


#add measured magt (from hobo_data.py) to geo_sensors DataFrame
geo_sensors = geo_sensors.join(measured_MAGT, on='WP')

#extract MAGT from modeled grid
mod_MAGT = []
for i in range(0,len(geo_sensors)):
    mod = MAGT.sample(np.array([[geo_sensors.geometry.x[i]], [geo_sensors.geometry.y[i]]]), grid = True)[0][0]
    mod_MAGT.append(mod)

geo_sensors['modeled_MAGT'] = pd.DataFrame(mod_MAGT)

#Plot modeled gst with residuals compared to measured.
fig, ax = plt.subplots(figsize = (9,9))
img = ax.imshow(MAGT.Z, vmin = -5, vmax = 5, cmap = 'coolwarm', extent = [summer_rad.x.min(), summer_rad.x.max(), summer_rad.y.min(), summer_rad.y.max()])
geo_sensors.plot(ax = ax, facecolor = "k", edgecolor = 'k', markersize = 10) #plot again so that all WPs show
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
geo_sensors.plot(ax = ax, column = 'measured_MAGT', edgecolor = 'k', cmap = 'coolwarm',
        cax = cax, legend = True, vmin = -5, vmax = 5, markersize = 50)
ax.set_xlim([444500, 448000])
ax.set_ylim([4432500, 4435300])
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')

#axins = inset_axes(ax,
#                   width="5%",  # width = 5% of parent_bbox width
#                   height="100%",  # height : 50%
#                   loc='lower left',
#                   bbox_to_anchor=(1.1, 0., 1, 1),
#                   bbox_transform=ax.transAxes,
#                   borderpad=0,
#                   )

#fig.colorbar(img, shrink = 0.7, cax = axins)
fig.tight_layout()
fig.show()
#plt.savefig('Modeled_measured_MAGT.pdf')
