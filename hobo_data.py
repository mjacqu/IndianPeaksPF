import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import re
from datetime import datetime
import read_lter_data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import operator

data_path = '/Users/mistral/Documents/CUBoulder/Science/permafrost/data/Hobo_2019_2020'
f_list = glob.glob(os.path.join(data_path,'*.csv'))
f_ist = f_list.sort()

data = [pd.read_csv(f, usecols = [0,1,2], header = 1, names = ['Datetime', 'Temp1', 'Temp2']).replace(r"^\s*$", np.nan, regex=True) for f in f_list]
sn = [re.findall(r'\d{8}',f)[0] for f in f_list]

metadata_path = '/Users/mistral/Documents/CUBoulder/Science/permafrost/data/metadata/sensor_locations.csv'
metadata = pd.read_csv(metadata_path)
metadata = metadata.fillna(0)
metadata["sn"] = metadata["sn"].round().astype(int)

data_dict = {}

for d in range(0,len(data)):
    data[d]['Datetime'] = pd.to_datetime(data[d]['Datetime'], format = '%Y-%m-%d %H:%M:%S')
    data[d]['Temp1'] = pd.to_numeric(data[d]['Temp1'])
    data[d]['Temp2'] = pd.to_numeric(data[d]['Temp2'])
    data[d] = data[d].set_index('Datetime')
    data[d]['sn'] = sn[d]
    data_dict[sn[d]] = data[d] #also make dict with data

daily_mean_list = [d['Temp1'].groupby(pd.Grouper(freq = '1D')).mean() for d in data]
daily_mean = {k:v.groupby(pd.Grouper(freq = '1D')).mean() for (k,v) in data_dict.items()}

fig, axs = plt.subplots(12,1, figsize = (16,8), sharex = True)
for i in range(0,len(data)):
    daily_mean_N = daily_mean_list[i].copy()
    daily_mean_P = daily_mean_list[i].copy()
    daily_mean_N[daily_mean_N > 0] = np.nan
    daily_mean_P[daily_mean_P <= 0] = np.nan
    axs[i].plot(daily_mean_N, color = 'cornflowerblue')
    axs[i].plot(daily_mean_P, color = 'orangered')
    axs[i].set_ylim([-35,35])
    axs[i].axhline(y=0, color = 'grey', linewidth = 0.5)
    axs[i].text(datetime.strptime('2019-08-25', '%Y-%m-%d'), 17,
        'Thermo ' + str(metadata.WP[metadata.sn == int(data[i].sn[0])].values[0]), fontsize = 8)
    axs[i].text(datetime.strptime('2020-09-8', '%Y-%m-%d'), 15,
        str(metadata.elevation[metadata.sn == int(data[i].sn[0])].values[0])+'m asl', fontsize = 8)
    axs[i].text(datetime.strptime('2020-09-8', '%Y-%m-%d'), -17,
        'mean:'+ "{0:0.1f}".format(daily_mean_list[i].mean()), fontsize = 8)

fig.subplots_adjust(hspace=0)
fig.show()
#fig.savefig('data_overview.pdf')

# Thermo 7 and thermo 5(20689683) seem to be very similar to 11 (sn = 20706949) and 12 (sn=20706950). Use data from thermo
# 7 (20689678) to expand time series of thermo 11 and 12.

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (12,8))
ax1.scatter(daily_mean['20689683']['Temp1']['2019-09-25':'2020-03-07'],
            daily_mean['20706949']['Temp1']['2019-09-25':'2020-03-07'])
x = daily_mean['20689683']['Temp1']['2019-09-25':'2020-03-07'].to_numpy().reshape((-1,1))
y = daily_mean['20706949']['Temp1']['2019-09-25':'2020-03-07'].to_numpy()
model1 = LinearRegression().fit(x,y)
ax1.plot(x, model1.predict(x))
ax1.set_xlabel('Thermo 5')
ax1.set_ylabel('Thermo 11')
ax1.text(-15, 0, r'$R^2$: '+"{0:0.2f}".format(model1.score(x,y)))

ax2.scatter(daily_mean['20689683']['Temp1']['2019-09-25':'2020-02-06'],
            daily_mean['20706950']['Temp1']['2019-09-25':'2020-02-06'])
x = daily_mean['20689683']['Temp1']['2019-09-25':'2020-02-06'].to_numpy().reshape((-1,1))
y = daily_mean['20706950']['Temp1']['2019-09-25':'2020-02-06'].to_numpy()
model2 = LinearRegression().fit(x,y)
ax2.plot(x, model2.predict(x))
ax2.set_xlabel('Thermo 5')
ax2.set_ylabel('Thermo 12')
ax2.text(-15, 5, r'$R^2$: '+"{0:0.2f}".format(model2.score(x,y)))

ax3.scatter(daily_mean['20689678']['Temp1']['2019-09-25':'2020-03-07'],
            daily_mean['20706949']['Temp1']['2019-09-25':'2020-03-07'])
x = daily_mean['20689678']['Temp1']['2019-09-25':'2020-03-07'].to_numpy().reshape((-1,1))
y = daily_mean['20706949']['Temp1']['2019-09-25':'2020-03-07'].to_numpy()
model3 = LinearRegression().fit(x,y)
ax3.plot(x, model3.predict(x))
ax3.set_xlabel('Thermo 7')
ax3.set_ylabel('Thermo 11')
ax3.text(-15, 0, r'$R^2$: '+"{0:0.2f}".format(model3.score(x,y)))

ax4.scatter(daily_mean['20689678']['Temp1']['2019-09-25':'2020-02-06'],
            daily_mean['20706950']['Temp1']['2019-09-25':'2020-02-06'])
x = daily_mean['20689678']['Temp1']['2019-09-25':'2020-02-06'].to_numpy().reshape((-1,1))
y = daily_mean['20706950']['Temp1']['2019-09-25':'2020-02-06'].to_numpy()
model4 = LinearRegression().fit(x,y)
ax4.plot(x, model4.predict(x))
ax4.set_xlabel('Thermo 7')
ax4.set_ylabel('Thermo 12')
ax4.text(-15, 5, r'$R^2$: '+"{0:0.2f}".format(model4.score(x,y)))

fig.suptitle('Ground temperature prediction')
fig.tight_layout()
fig.show()
#fig.savefig('Thermo11_12_prediction.png')

# Best predictions found: 5-->11 (model1), 7-->12 (model4), 7-->9 (model5)
x = daily_mean['20689678']['Temp1']['2019-09-25':'2020-03-22'].to_numpy().reshape((-1,1))
y = daily_mean['20689675']['Temp1']['2019-09-25':'2020-03-22'].to_numpy()
model5 = LinearRegression().fit(x,y)
thermo9_predicted = model5.predict(daily_mean['20689678']['Temp1'].to_numpy().reshape((-1,1)))
thermo11_predicted = model1.predict(daily_mean['20689683']['Temp1'].to_numpy().reshape((-1,1)))
thermo12_predicted = model4.predict(daily_mean['20689678']['Temp1'].to_numpy().reshape((-1,1)))

predicted_data = {
        "thermo9" : pd.DataFrame(zip(daily_mean['20689678'].index,thermo9_predicted), columns = ['Datetime','temp']).set_index('Datetime'),
        "thermo11" : pd.DataFrame(zip(daily_mean['20689683'].index,thermo11_predicted), columns = ['Datetime','temp']).set_index('Datetime'),
        "thermo12" : pd.DataFrame(zip(daily_mean['20689678'].index,thermo12_predicted), columns = ['Datetime','temp']).set_index('Datetime')
}


#D1 station data1
infile1  = '/Users/mistral/Documents/CUBoulder/Science/permafrost/data/station_data/d-1cr23x-cr1000.daily.ml.data.csv'
infile2  = '/Users/mistral/Documents/CUBoulder/Science/permafrost/data/station_data/c-1cr23x-cr1000.daily.ml.data.csv'


d1 = read_lter_data.read_data_d1(infile1)
c1 = read_lter_data.read_data_c1(infile2)

#mean soil temperature at D1
mean_soil = d1.soiltemp_5cm_avg.groupby(pd.Grouper(freq = '1D')).mean()
mean_yearly_soil = d1.soiltemp_5cm_avg['2001-01-01':'2019-12-31'].groupby(pd.Grouper(freq = '1Y')).mean()
mean_air = d1.airtemp_avg.groupby(pd.Grouper(freq = '1D')).mean()
mean_yearly_air = d1.airtemp_avg['2001-01-01':'2018-12-31'].groupby(pd.Grouper(freq = '1Y')).mean()

# Side by side plot of soil and air temperature
plt.style.use('ggplot')
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12,6))

#ax1.axhline(c = 'k', linewidth = 0.8)
ax1.plot(mean_air, label = 'Mean daily')
ax1.plot(mean_yearly_air, '_', c = 'k', label = 'Mean annual', markersize = 15, mew = 1.2)
ax1.set_title('Air temperature')
ax1.set_ylim([-30,30])
ax1.legend(loc = 2)

#ax2.axhline(c = 'k', linewidth = 0.8)
ax2.plot(mean_soil, label = 'Mean daily')
ax2.plot(mean_yearly_soil, '_', c = 'k', label = 'Mean annual', markersize = 15, mew = 1.2)
ax2.set_title('Soil temperature @ 5cm')
ax2.set_ylim([-30,30])
ax2.legend(loc = 2)

fig.tight_layout()
fig.show()
#fig.savefig('D1data.png')

# Quick and dirty compilation of mean annual temperature for somewhat reliable points:
m_MAGT = {
        "1": daily_mean['20689680']['Temp1'].mean(),
        "2": np.nan,
        "3": np.nan,
        "4": np.nan,
        "5": daily_mean['20689683']['Temp1'].mean(),
        "6": daily_mean['20689679']['Temp1'].mean(),
        "7": daily_mean['20689678']['Temp1'].mean(),
        "8": daily_mean['20689677']['Temp1'].mean(),
        "9": predicted_data['thermo9']['temp'].mean(),
        "10": daily_mean['20689674']['Temp1'].mean(),
        "11": predicted_data['thermo11']['temp'].mean(),
        "12": predicted_data['thermo12']['temp'].mean(),
        "D1": d1.soiltemp_5cm_avg.mean()
}

measured_MAGT = pd.DataFrame.from_dict(m_MAGT, orient = 'index', columns = ['measured_MAGT'])

#calculate lapse rate between c1 and d1
elev_d1 = 3793
elev_c1 = 3022
elev_diff = elev_d1 - elev_c1
mean_diff = np.mean(c1.airtemp_avg-d1.airtemp_avg)
lapse_rate = mean_diff / elev_diff #per meter

lt_mean_c1 = c1.airtemp_avg.mean()
lt_mean_d1 = d1.airtemp_avg.mean()

dh_d1 = lt_mean_d1/lapse_rate
dh_c1 = lt_mean_c1/lapse_rate

zero_iso_d1 = elev_d1 + dh_d1
zero_iso_c1 = elev_c1 + dh_c1
mean_zero_iso = (zero_iso_c1+zero_iso_d1)/2
