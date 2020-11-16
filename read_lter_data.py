# Package ID: knb-lter-nwt.402.3 Cataloging System:https://pasta.edirepository.org.
# Data set title: Climate data for D1 data loggers (CR23X and CR1000), 2000 - ongoing, daily..
# Data set creator:  Jennifer F Morse -
# Data set creator:  Mark Losleben -
# Data set creator:    - Niwot Ridge LTER
# Contact:    - Information Manager Niwot Ridge LTER  - lternwt@colorado.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu
#
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run.

# Edited by Mylène Jacquemart, 2020-11-10

import numpy as np
import pandas as pd

def read_data_d1(file, verbose=False):
    '''
    Return pandas dataframe with date as index from D1 station data.

    Parameters:
            file (str):     D1 data file
            verbose (bool): print data summary if True. Default False.

    Returns:
            data (pandas.DataFrame) with date as index
    '''
    dt1 =pd.read_csv(file
              ,skiprows=1
                ,sep=","
                    ,quotechar='"'
               , names=[
                        "LTER_site",
                        "local_site",
                        "logger",
                        "date",
                        "year",
                        "jday",
                        "airtemp_max",
                        "flag_airtemp_max",
                        "airtemp_min",
                        "flag_airtemp_min",
                        "airtemp_avg",
                        "flag_airtemp_avg",
                        "rh_max",
                        "flag_rh_max",
                        "rh_min",
                        "flag_rh_min",
                        "rh_avg",
                        "flag_rh_avg",
                        "bp_max",
                        "flag_bp_max",
                        "bp_min",
                        "flag_bp_min",
                        "bp_avg",
                        "flag_bp_avg",
                        "ws_max",
                        "flag_ws_max",
                        "ws_min",
                        "flag_ws_min",
                        "ws_avg",
                        "flag_ws_avg",
                        "wd",
                        "flag_wd",
                        "solrad_avg",
                        "flag_solrad_avg",
                        "solrad_tot",
                        "flag_solrad_tot",
                        "soiltemp_5cm_avg",
                        "flag_soiltemp_5cm_avg",
                        "soilmoist_5cm_avg",
                        "flag_soilmoist_5cm_avg",
                        "airtemp_hmp1_max",
                        "flag_airtemp_hmp1_max",
                        "airtemp_hmp1_min",
                        "flag_airtemp_hmp1_min",
                        "airtemp_hmp1_avg",
                        "flag_airtemp_hmp1_avg",
                        "airtemp_hmp2_max",
                        "flag_airtemp_hmp2_max",
                        "airtemp_hmp2_min",
                        "flag_airtemp_hmp2_min",
                        "airtemp_hmp2_avg",
                        "flag_airtemp_hmp2_avg",
                        "airtemp_hmp3_max",
                        "flag_airtemp_hmp3_max",
                        "airtemp_hmp3_min",
                        "flag_airtemp_hmp3_min",
                        "airtemp_hmp3_avg",
                        "flag_airtemp_hmp3_avg",
                        "rh_hmp1_max",
                        "flag_rh_hmp1_max",
                        "rh_hmp1_min",
                        "flag_rh_hmp1_min",
                        "rh_hmp1_avg",
                        "flag_rh_hmp1_avg",
                        "rh_hmp2_max",
                        "flag_rh_hmp2_max",
                        "rh_hmp2_min",
                        "flag_rh_hmp2_min",
                        "rh_hmp2_avg",
                        "flag_rh_hmp2_avg",
                        "rh_hmp3_max",
                        "flag_rh_hmp3_max",
                        "rh_hmp3_min",
                        "flag_rh_hmp3_min",
                        "rh_hmp3_avg",
                        "flag_rh_hmp3_avg"    ]
    # data type checking is commented out because it may cause data
    # loads to fail if the data contains inconsistent values. Uncomment
    # the following lines to enable data type checking

    #            ,dtype={
    #             'LTER_site':'str' ,
    #             'local_site':'str' ,
    #             'logger':'str' ,
    #             'date':'str' ,
    #             'year':'str' ,
    #             'jday':'int' ,
    #             'airtemp_max':'float' ,
    #             'flag_airtemp_max':'str' ,
    #             'airtemp_min':'float' ,
    #             'flag_airtemp_min':'str' ,
    #             'airtemp_avg':'float' ,
    #             'flag_airtemp_avg':'str' ,
    #             'rh_max':'float' ,
    #             'flag_rh_max':'str' ,
    #             'rh_min':'float' ,
    #             'flag_rh_min':'str' ,
    #             'rh_avg':'float' ,
    #             'flag_rh_avg':'str' ,
    #             'bp_max':'float' ,
    #             'flag_bp_max':'str' ,
    #             'bp_min':'float' ,
    #             'flag_bp_min':'str' ,
    #             'bp_avg':'float' ,
    #             'flag_bp_avg':'str' ,
    #             'ws_max':'float' ,
    #             'flag_ws_max':'str' ,
    #             'ws_min':'float' ,
    #             'flag_ws_min':'str' ,
    #             'ws_avg':'float' ,
    #             'flag_ws_avg':'str' ,
    #             'wd':'float' ,
    #             'flag_wd':'str' ,
    #             'solrad_avg':'float' ,
    #             'flag_solrad_avg':'str' ,
    #             'solrad_tot':'float' ,
    #             'flag_solrad_tot':'str' ,
    #             'soiltemp_5cm_avg':'float' ,
    #             'flag_soiltemp_5cm_avg':'str' ,
    #             'soilmoist_5cm_avg':'float' ,
    #             'flag_soilmoist_5cm_avg':'str' ,
    #             'airtemp_hmp1_max':'float' ,
    #             'flag_airtemp_hmp1_max':'str' ,
    #             'airtemp_hmp1_min':'float' ,
    #             'flag_airtemp_hmp1_min':'str' ,
    #             'airtemp_hmp1_avg':'float' ,
    #             'flag_airtemp_hmp1_avg':'str' ,
    #             'airtemp_hmp2_max':'float' ,
    #             'flag_airtemp_hmp2_max':'str' ,
    #             'airtemp_hmp2_min':'float' ,
    #             'flag_airtemp_hmp2_min':'str' ,
    #             'airtemp_hmp2_avg':'float' ,
    #             'flag_airtemp_hmp2_avg':'str' ,
    #             'airtemp_hmp3_max':'float' ,
    #             'flag_airtemp_hmp3_max':'str' ,
    #             'airtemp_hmp3_min':'float' ,
    #             'flag_airtemp_hmp3_min':'str' ,
    #             'airtemp_hmp3_avg':'float' ,
    #             'flag_airtemp_hmp3_avg':'str' ,
    #             'rh_hmp1_max':'float' ,
    #             'flag_rh_hmp1_max':'str' ,
    #             'rh_hmp1_min':'float' ,
    #             'flag_rh_hmp1_min':'str' ,
    #             'rh_hmp1_avg':'float' ,
    #             'flag_rh_hmp1_avg':'str' ,
    #             'rh_hmp2_max':'float' ,
    #             'flag_rh_hmp2_max':'str' ,
    #             'rh_hmp2_min':'float' ,
    #             'flag_rh_hmp2_min':'str' ,
    #             'rh_hmp2_avg':'float' ,
    #             'flag_rh_hmp2_avg':'str' ,
    #             'rh_hmp3_max':'float' ,
    #             'flag_rh_hmp3_max':'str' ,
    #             'rh_hmp3_min':'float' ,
    #             'flag_rh_hmp3_min':'str' ,
    #             'rh_hmp3_avg':'float' ,
    #             'flag_rh_hmp3_avg':'str'
    #        }
              ,parse_dates=[
                            'date',
#                            'year',
                    ]
                ,na_values={
                      'LTER_site':[
                              'NaN',],
                      'local_site':[
                              'NaN',],
                      'logger':[
                              'NaN',],
                      'date':[
                              'NaN',],
                      'year':[
                              'NaN',],
                      'jday':[
                              'NaN',],
                      'airtemp_max':[
                              'NaN',],
                      'flag_airtemp_max':[
                              'NaN',],
                      'airtemp_min':[
                              'NaN',],
                      'flag_airtemp_min':[
                              'NaN',],
                      'airtemp_avg':[
                              'NaN',],
                      'flag_airtemp_avg':[
                              'NaN',],
                      'rh_max':[
                              'NaN',],
                      'flag_rh_max':[
                              'NaN',],
                      'rh_min':[
                              'NaN',],
                      'flag_rh_min':[
                              'NaN',],
                      'rh_avg':[
                              'NaN',],
                      'flag_rh_avg':[
                              'NaN',],
                      'bp_max':[
                              'NaN',],
                      'flag_bp_max':[
                              'NaN',],
                      'bp_min':[
                              'NaN',],
                      'flag_bp_min':[
                              'NaN',],
                      'bp_avg':[
                              'NaN',],
                      'flag_bp_avg':[
                              'NaN',],
                      'ws_max':[
                              'NaN',],
                      'flag_ws_max':[
                              'NaN',],
                      'ws_min':[
                              'NaN',],
                      'flag_ws_min':[
                              'NaN',],
                      'ws_avg':[
                              'NaN',],
                      'flag_ws_avg':[
                              'NaN',],
                      'wd':[
                              'NaN',],
                      'flag_wd':[
                              'NaN',],
                      'solrad_avg':[
                              'NaN',],
                      'flag_solrad_avg':[
                              'NaN',],
                      'solrad_tot':[
                              'NaN',],
                      'flag_solrad_tot':[
                              'NaN',],
                      'soiltemp_5cm_avg':[
                              'NaN',],
                      'flag_soiltemp_5cm_avg':[
                              'NaN',],
                      'soilmoist_5cm_avg':[
                              'NaN',],
                      'flag_soilmoist_5cm_avg':[
                              'NaN',],
                      'airtemp_hmp1_max':[
                              'NaN',],
                      'flag_airtemp_hmp1_max':[
                              'NaN',],
                      'airtemp_hmp1_min':[
                              'NaN',],
                      'flag_airtemp_hmp1_min':[
                              'NaN',],
                      'airtemp_hmp1_avg':[
                              'NaN',],
                      'flag_airtemp_hmp1_avg':[
                              'NaN',],
                      'airtemp_hmp2_max':[
                              'NaN',],
                      'flag_airtemp_hmp2_max':[
                              'NaN',],
                      'airtemp_hmp2_min':[
                              'NaN',],
                      'flag_airtemp_hmp2_min':[
                              'NaN',],
                      'airtemp_hmp2_avg':[
                              'NaN',],
                      'flag_airtemp_hmp2_avg':[
                              'NaN',],
                      'airtemp_hmp3_max':[
                              'NaN',],
                      'flag_airtemp_hmp3_max':[
                              'NaN',],
                      'airtemp_hmp3_min':[
                              'NaN',],
                      'flag_airtemp_hmp3_min':[
                              'NaN',],
                      'airtemp_hmp3_avg':[
                              'NaN',],
                      'flag_airtemp_hmp3_avg':[
                              'NaN',],
                      'rh_hmp1_max':[
                              'NaN',],
                      'flag_rh_hmp1_max':[
                              'NaN',],
                      'rh_hmp1_min':[
                              'NaN',],
                      'flag_rh_hmp1_min':[
                              'NaN',],
                      'rh_hmp1_avg':[
                              'NaN',],
                      'flag_rh_hmp1_avg':[
                              'NaN',],
                      'rh_hmp2_max':[
                              'NaN',],
                      'flag_rh_hmp2_max':[
                              'NaN',],
                      'rh_hmp2_min':[
                              'NaN',],
                      'flag_rh_hmp2_min':[
                              'NaN',],
                      'rh_hmp2_avg':[
                              'NaN',],
                      'flag_rh_hmp2_avg':[
                              'NaN',],
                      'rh_hmp3_max':[
                              'NaN',],
                      'flag_rh_hmp3_max':[
                              'NaN',],
                      'rh_hmp3_min':[
                              'NaN',],
                      'flag_rh_hmp3_min':[
                              'NaN',],
                      'rh_hmp3_avg':[
                              'NaN',],
                      'flag_rh_hmp3_avg':[
                              'NaN',],}

        )
    # Coerce the data into the types specified in the metadata
    dt1.LTER_site=dt1.LTER_site.astype('category')
    dt1.local_site=dt1.local_site.astype('category')
    dt1.logger=dt1.logger.astype('category')
    # Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
    # This new column is added to the dataframe but does not show up in automated summaries below.
    #dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))
    # Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
    # This new column is added to the dataframe but does not show up in automated summaries below.
    #dt1=dt1.assign(year_datetime=pd.to_datetime(dt1.year,errors='coerce'))
    dt1.jday=pd.to_numeric(dt1.jday,errors='coerce',downcast='integer')
    dt1.airtemp_max=pd.to_numeric(dt1.airtemp_max,errors='coerce')
    dt1.flag_airtemp_max=dt1.flag_airtemp_max.astype('category')
    dt1.airtemp_min=pd.to_numeric(dt1.airtemp_min,errors='coerce')
    dt1.flag_airtemp_min=dt1.flag_airtemp_min.astype('category')
    dt1.airtemp_avg=pd.to_numeric(dt1.airtemp_avg,errors='coerce')
    dt1.flag_airtemp_avg=dt1.flag_airtemp_avg.astype('category')
    dt1.rh_max=pd.to_numeric(dt1.rh_max,errors='coerce')
    dt1.flag_rh_max=dt1.flag_rh_max.astype('category')
    dt1.rh_min=pd.to_numeric(dt1.rh_min,errors='coerce')
    dt1.flag_rh_min=dt1.flag_rh_min.astype('category')
    dt1.rh_avg=pd.to_numeric(dt1.rh_avg,errors='coerce')
    dt1.flag_rh_avg=dt1.flag_rh_avg.astype('category')
    dt1.bp_max=pd.to_numeric(dt1.bp_max,errors='coerce')
    dt1.flag_bp_max=dt1.flag_bp_max.astype('category')
    dt1.bp_min=pd.to_numeric(dt1.bp_min,errors='coerce')
    dt1.flag_bp_min=dt1.flag_bp_min.astype('category')
    dt1.bp_avg=pd.to_numeric(dt1.bp_avg,errors='coerce')
    dt1.flag_bp_avg=dt1.flag_bp_avg.astype('category')
    dt1.ws_max=pd.to_numeric(dt1.ws_max,errors='coerce')
    dt1.flag_ws_max=dt1.flag_ws_max.astype('category')
    dt1.ws_min=pd.to_numeric(dt1.ws_min,errors='coerce')
    dt1.flag_ws_min=dt1.flag_ws_min.astype('category')
    dt1.ws_avg=pd.to_numeric(dt1.ws_avg,errors='coerce')
    dt1.flag_ws_avg=dt1.flag_ws_avg.astype('category')
    dt1.wd=pd.to_numeric(dt1.wd,errors='coerce')
    dt1.flag_wd=dt1.flag_wd.astype('category')
    dt1.solrad_avg=pd.to_numeric(dt1.solrad_avg,errors='coerce')
    dt1.flag_solrad_avg=dt1.flag_solrad_avg.astype('category')
    dt1.solrad_tot=pd.to_numeric(dt1.solrad_tot,errors='coerce')
    dt1.flag_solrad_tot=dt1.flag_solrad_tot.astype('category')
    dt1.soiltemp_5cm_avg=pd.to_numeric(dt1.soiltemp_5cm_avg,errors='coerce')
    dt1.flag_soiltemp_5cm_avg=dt1.flag_soiltemp_5cm_avg.astype('category')
    dt1.soilmoist_5cm_avg=pd.to_numeric(dt1.soilmoist_5cm_avg,errors='coerce')
    dt1.flag_soilmoist_5cm_avg=dt1.flag_soilmoist_5cm_avg.astype('category')
    dt1.airtemp_hmp1_max=pd.to_numeric(dt1.airtemp_hmp1_max,errors='coerce')
    dt1.flag_airtemp_hmp1_max=dt1.flag_airtemp_hmp1_max.astype('category')
    dt1.airtemp_hmp1_min=pd.to_numeric(dt1.airtemp_hmp1_min,errors='coerce')
    dt1.flag_airtemp_hmp1_min=dt1.flag_airtemp_hmp1_min.astype('category')
    dt1.airtemp_hmp1_avg=pd.to_numeric(dt1.airtemp_hmp1_avg,errors='coerce')
    dt1.flag_airtemp_hmp1_avg=dt1.flag_airtemp_hmp1_avg.astype('category')
    dt1.airtemp_hmp2_max=pd.to_numeric(dt1.airtemp_hmp2_max,errors='coerce')
    dt1.flag_airtemp_hmp2_max=dt1.flag_airtemp_hmp2_max.astype('category')
    dt1.airtemp_hmp2_min=pd.to_numeric(dt1.airtemp_hmp2_min,errors='coerce')
    dt1.flag_airtemp_hmp2_min=dt1.flag_airtemp_hmp2_min.astype('category')
    dt1.airtemp_hmp2_avg=pd.to_numeric(dt1.airtemp_hmp2_avg,errors='coerce')
    dt1.flag_airtemp_hmp2_avg=dt1.flag_airtemp_hmp2_avg.astype('category')
    dt1.airtemp_hmp3_max=pd.to_numeric(dt1.airtemp_hmp3_max,errors='coerce')
    dt1.flag_airtemp_hmp3_max=dt1.flag_airtemp_hmp3_max.astype('category')
    dt1.airtemp_hmp3_min=pd.to_numeric(dt1.airtemp_hmp3_min,errors='coerce')
    dt1.flag_airtemp_hmp3_min=dt1.flag_airtemp_hmp3_min.astype('category')
    dt1.airtemp_hmp3_avg=pd.to_numeric(dt1.airtemp_hmp3_avg,errors='coerce')
    dt1.flag_airtemp_hmp3_avg=dt1.flag_airtemp_hmp3_avg.astype('category')
    dt1.rh_hmp1_max=pd.to_numeric(dt1.rh_hmp1_max,errors='coerce')
    dt1.flag_rh_hmp1_max=dt1.flag_rh_hmp1_max.astype('category')
    dt1.rh_hmp1_min=pd.to_numeric(dt1.rh_hmp1_min,errors='coerce')
    dt1.flag_rh_hmp1_min=dt1.flag_rh_hmp1_min.astype('category')
    dt1.rh_hmp1_avg=pd.to_numeric(dt1.rh_hmp1_avg,errors='coerce')
    dt1.flag_rh_hmp1_avg=dt1.flag_rh_hmp1_avg.astype('category')
    dt1.rh_hmp2_max=pd.to_numeric(dt1.rh_hmp2_max,errors='coerce')
    dt1.flag_rh_hmp2_max=dt1.flag_rh_hmp2_max.astype('category')
    dt1.rh_hmp2_min=pd.to_numeric(dt1.rh_hmp2_min,errors='coerce')
    dt1.flag_rh_hmp2_min=dt1.flag_rh_hmp2_min.astype('category')
    dt1.rh_hmp2_avg=pd.to_numeric(dt1.rh_hmp2_avg,errors='coerce')
    dt1.flag_rh_hmp2_avg=dt1.flag_rh_hmp2_avg.astype('category')
    dt1.rh_hmp3_max=pd.to_numeric(dt1.rh_hmp3_max,errors='coerce')
    dt1.flag_rh_hmp3_max=dt1.flag_rh_hmp3_max.astype('category')
    dt1.rh_hmp3_min=pd.to_numeric(dt1.rh_hmp3_min,errors='coerce')
    dt1.flag_rh_hmp3_min=dt1.flag_rh_hmp3_min.astype('category')
    dt1.rh_hmp3_avg=pd.to_numeric(dt1.rh_hmp3_avg,errors='coerce')
    dt1.flag_rh_hmp3_avg=dt1.flag_rh_hmp3_avg.astype('category')
    dt1 = dt1.set_index('date')
    if verbose:
        print("Here is a description of the data frame dt1 and number of lines\n")
        print(dt1.info())
        print("--------------------\n\n")
        print("Here is a summary of numerical variables in the data frame dt1\n")
        print(dt1.describe())
        print("--------------------\n\n")
        print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")
        print(dt1.LTER_site.describe())
        print("--------------------\n\n")
        print(dt1.local_site.describe())
        print("--------------------\n\n")
        print(dt1.logger.describe())
        print("--------------------\n\n")
#        print(dt1.date.describe())
#        print("--------------------\n\n")
        print(dt1.year.describe())
        print("--------------------\n\n")
        print(dt1.jday.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_max.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_min.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_avg.describe())
        print("--------------------\n\n")
        print(dt1.rh_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_max.describe())
        print("--------------------\n\n")
        print(dt1.rh_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_min.describe())
        print("--------------------\n\n")
        print(dt1.rh_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_avg.describe())
        print("--------------------\n\n")
        print(dt1.bp_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_bp_max.describe())
        print("--------------------\n\n")
        print(dt1.bp_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_bp_min.describe())
        print("--------------------\n\n")
        print(dt1.bp_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_bp_avg.describe())
        print("--------------------\n\n")
        print(dt1.ws_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_ws_max.describe())
        print("--------------------\n\n")
        print(dt1.ws_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_ws_min.describe())
        print("--------------------\n\n")
        print(dt1.ws_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_ws_avg.describe())
        print("--------------------\n\n")
        print(dt1.wd.describe())
        print("--------------------\n\n")
        print(dt1.flag_wd.describe())
        print("--------------------\n\n")
        print(dt1.solrad_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_solrad_avg.describe())
        print("--------------------\n\n")
        print(dt1.solrad_tot.describe())
        print("--------------------\n\n")
        print(dt1.flag_solrad_tot.describe())
        print("--------------------\n\n")
        print(dt1.soiltemp_5cm_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_soiltemp_5cm_avg.describe())
        print("--------------------\n\n")
        print(dt1.soilmoist_5cm_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_soilmoist_5cm_avg.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp1_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp1_max.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp1_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp1_min.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp1_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp1_avg.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp2_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp2_max.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp2_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp2_min.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp2_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp2_avg.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp3_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp3_max.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp3_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp3_min.describe())
        print("--------------------\n\n")
        print(dt1.airtemp_hmp3_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_airtemp_hmp3_avg.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp1_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp1_max.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp1_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp1_min.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp1_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp1_avg.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp2_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp2_max.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp2_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp2_min.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp2_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp2_avg.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp3_max.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp3_max.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp3_min.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp3_min.describe())
        print("--------------------\n\n")
        print(dt1.rh_hmp3_avg.describe())
        print("--------------------\n\n")
        print(dt1.flag_rh_hmp3_avg.describe())
        print("--------------------\n\n")
    return dt1

    # Package ID: knb-lter-nwt.401.4 Cataloging System:https://pasta.edirepository.org.
# Data set title: Climate data for C1 data loggers (CR23X and CR1000), 2000 - ongoing, daily..
# Data set creator:  Jennifer F Morse -
# Data set creator:    - Niwot Ridge LTER
# Contact:    - Information Manager Niwot Ridge LTER  - lternwt@colorado.edu
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu
#
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run.

def read_data_c1(file, verbose=False):
    '''
    Return pandas dataframe with date as index from D1 station data.

    Parameters:
            file (str):     C1 data file
            verbose (bool): print data summary if True. Default False.

    Returns:
            data (pandas.DataFrame) with date as index
    '''
    dt1 =pd.read_csv(file
              ,skiprows=1
                ,sep=","
                    ,quotechar='"'
               , names=[
                        "LTER_site",
                        "local_site",
                        "logger",
                        "date",
                        "year",
                        "jday",
                        "airtemp_max",
                        "flag_airtemp_max",
                        "airtemp_min",
                        "flag_airtemp_min",
                        "airtemp_avg",
                        "flag_airtemp_avg",
                        "rh_max",
                        "flag_rh_max",
                        "rh_min",
                        "flag_rh_min",
                        "rh_avg",
                        "flag_rh_avg",
                        "bp_max",
                        "flag_bp_max",
                        "bp_min",
                        "flag_bp_min",
                        "bp_avg",
                        "flag_bp_avg",
                        "ws_max",
                        "flag_ws_max",
                        "ws_min",
                        "flag_ws_min",
                        "ws_avg",
                        "flag_ws_avg",
                        "wd",
                        "flag_wd",
                        "solrad_avg",
                        "flag_solrad_avg",
                        "solrad_tot",
                        "flag_solrad_tot",
                        "ppt_tot",
                        "flag_ppt_tot",
                        "snowdepth_avg",
                        "flag_snowdepth_avg",
                        "soiltemp_5cm_max",
                        "flag_soiltemp_5cm_max",
                        "soiltemp_5cm_min",
                        "flag_soiltemp_5cm_min",
                        "soiltemp_5cm_avg",
                        "flag_soiltemp_5cm_avg",
                        "soilmoist_5cm_avg",
                        "flag_soilmoist_5cm_avg",
                        "soilmoistprof_10cm_avg",
                        "flag_soilmoistprof_10cm_avg",
                        "soilmoistprof_20cm_avg",
                        "flag_soilmoistprof_20cm_avg",
                        "soilmoistprof_30cm_avg",
                        "flag_soilmoistprof_30cm_avg",
                        "soilmoistprof_50cm_avg",
                        "flag_soilmoistprof_50cm_avg",
                        "soilmoistprof_70cm_avg",
                        "flag_soilmoistprof_70cm_avg",
                        "soilmoistprof_100cm_avg",
                        "flag_soilmoistprof_100cm_avg",
                        "soilmoistprof_150cm_avg",
                        "flag_soilmoistprof_150cm_avg",
                        "soilmoistprof_200cm_avg",
                        "flag_soilmoistprof_200cm_avg",
                        "airtemp_hmp1_max",
                        "flag_airtemp_hmp1_max",
                        "airtemp_hmp1_min",
                        "flag_airtemp_hmp1_min",
                        "airtemp_hmp1_avg",
                        "flag_airtemp_hmp1_avg",
                        "airtemp_hmp2_max",
                        "flag_airtemp_hmp2_max",
                        "airtemp_hmp2_min",
                        "flag_airtemp_hmp2_min",
                        "airtemp_hmp2_avg",
                        "flag_airtemp_hmp2_avg",
                        "airtemp_hmp3_max",
                        "flag_airtemp_hmp3_max",
                        "airtemp_hmp3_min",
                        "flag_airtemp_hmp3_min",
                        "airtemp_hmp3_avg",
                        "flag_airtemp_hmp3_avg",
                        "rh_hmp1_max",
                        "flag_rh_hmp1_max",
                        "rh_hmp1_min",
                        "flag_rh_hmp1_min",
                        "rh_hmp1_avg",
                        "flag_rh_hmp1_avg",
                        "rh_hmp2_max",
                        "flag_rh_hmp2_max",
                        "rh_hmp2_min",
                        "flag_rh_hmp2_min",
                        "rh_hmp2_avg",
                        "flag_rh_hmp2_avg",
                        "rh_hmp3_max",
                        "flag_rh_hmp3_max",
                        "rh_hmp3_min",
                        "flag_rh_hmp3_min",
                        "rh_hmp3_avg",
                        "flag_rh_hmp3_avg"    ]
    # data type checking is commented out because it may cause data
    # loads to fail if the data contains inconsistent values. Uncomment
    # the following lines to enable data type checking

    #            ,dtype={
    #             'LTER_site':'str' ,
    #             'local_site':'str' ,
    #             'logger':'str' ,
    #             'date':'str' ,
    #             'year':'str' ,
    #             'jday':'int' ,
    #             'airtemp_max':'float' ,
    #             'flag_airtemp_max':'str' ,
    #             'airtemp_min':'float' ,
    #             'flag_airtemp_min':'str' ,
    #             'airtemp_avg':'float' ,
    #             'flag_airtemp_avg':'str' ,
    #             'rh_max':'float' ,
    #             'flag_rh_max':'str' ,
    #             'rh_min':'float' ,
    #             'flag_rh_min':'str' ,
    #             'rh_avg':'float' ,
    #             'flag_rh_avg':'str' ,
    #             'bp_max':'float' ,
    #             'flag_bp_max':'str' ,
    #             'bp_min':'float' ,
    #             'flag_bp_min':'str' ,
    #             'bp_avg':'float' ,
    #             'flag_bp_avg':'str' ,
    #             'ws_max':'float' ,
    #             'flag_ws_max':'str' ,
    #             'ws_min':'float' ,
    #             'flag_ws_min':'str' ,
    #             'ws_avg':'float' ,
    #             'flag_ws_avg':'str' ,
    #             'wd':'float' ,
    #             'flag_wd':'str' ,
    #             'solrad_avg':'float' ,
    #             'flag_solrad_avg':'str' ,
    #             'solrad_tot':'float' ,
    #             'flag_solrad_tot':'str' ,
    #             'ppt_tot':'float' ,
    #             'flag_ppt_tot':'str' ,
    #             'snowdepth_avg':'float' ,
    #             'flag_snowdepth_avg':'str' ,
    #             'soiltemp_5cm_max':'float' ,
    #             'flag_soiltemp_5cm_max':'str' ,
    #             'soiltemp_5cm_min':'float' ,
    #             'flag_soiltemp_5cm_min':'str' ,
    #             'soiltemp_5cm_avg':'float' ,
    #             'flag_soiltemp_5cm_avg':'str' ,
    #             'soilmoist_5cm_avg':'float' ,
    #             'flag_soilmoist_5cm_avg':'str' ,
    #             'soilmoistprof_10cm_avg':'float' ,
    #             'flag_soilmoistprof_10cm_avg':'str' ,
    #             'soilmoistprof_20cm_avg':'float' ,
    #             'flag_soilmoistprof_20cm_avg':'str' ,
    #             'soilmoistprof_30cm_avg':'float' ,
    #             'flag_soilmoistprof_30cm_avg':'str' ,
    #             'soilmoistprof_50cm_avg':'float' ,
    #             'flag_soilmoistprof_50cm_avg':'str' ,
    #             'soilmoistprof_70cm_avg':'float' ,
    #             'flag_soilmoistprof_70cm_avg':'str' ,
    #             'soilmoistprof_100cm_avg':'float' ,
    #             'flag_soilmoistprof_100cm_avg':'str' ,
    #             'soilmoistprof_150cm_avg':'float' ,
    #             'flag_soilmoistprof_150cm_avg':'str' ,
    #             'soilmoistprof_200cm_avg':'float' ,
    #             'flag_soilmoistprof_200cm_avg':'str' ,
    #             'airtemp_hmp1_max':'float' ,
    #             'flag_airtemp_hmp1_max':'str' ,
    #             'airtemp_hmp1_min':'float' ,
    #             'flag_airtemp_hmp1_min':'str' ,
    #             'airtemp_hmp1_avg':'float' ,
    #             'flag_airtemp_hmp1_avg':'str' ,
    #             'airtemp_hmp2_max':'float' ,
    #             'flag_airtemp_hmp2_max':'str' ,
    #             'airtemp_hmp2_min':'float' ,
    #             'flag_airtemp_hmp2_min':'str' ,
    #             'airtemp_hmp2_avg':'float' ,
    #             'flag_airtemp_hmp2_avg':'str' ,
    #             'airtemp_hmp3_max':'float' ,
    #             'flag_airtemp_hmp3_max':'str' ,
    #             'airtemp_hmp3_min':'float' ,
    #             'flag_airtemp_hmp3_min':'str' ,
    #             'airtemp_hmp3_avg':'float' ,
    #             'flag_airtemp_hmp3_avg':'str' ,
    #             'rh_hmp1_max':'float' ,
    #             'flag_rh_hmp1_max':'str' ,
    #             'rh_hmp1_min':'float' ,
    #             'flag_rh_hmp1_min':'str' ,
    #             'rh_hmp1_avg':'float' ,
    #             'flag_rh_hmp1_avg':'str' ,
    #             'rh_hmp2_max':'float' ,
    #             'flag_rh_hmp2_max':'str' ,
    #             'rh_hmp2_min':'float' ,
    #             'flag_rh_hmp2_min':'str' ,
    #             'rh_hmp2_avg':'float' ,
    #             'flag_rh_hmp2_avg':'str' ,
    #             'rh_hmp3_max':'float' ,
    #             'flag_rh_hmp3_max':'str' ,
    #             'rh_hmp3_min':'float' ,
    #             'flag_rh_hmp3_min':'str' ,
    #             'rh_hmp3_avg':'float' ,
    #             'flag_rh_hmp3_avg':'str'
    #        }
              ,parse_dates=[
                            'date',
                            'year',
                    ]
                ,na_values={
                      'LTER_site':[
                              'NaN',],
                      'local_site':[
                              'NaN',],
                      'logger':[
                              'NaN',],
                      'date':[
                              'NaN',],
                      'year':[
                              'NaN',],
                      'jday':[
                              'NaN',],
                      'airtemp_max':[
                              'NaN',
                              'NP',],
                      'flag_airtemp_max':[
                              'NaN',],
                      'airtemp_min':[
                              'NaN',
                              'NP',],
                      'flag_airtemp_min':[
                              'NaN',],
                      'airtemp_avg':[
                              'NaN',
                              'NP',],
                      'flag_airtemp_avg':[
                              'NaN',],
                      'rh_max':[
                              'NaN',
                              'NP',],
                      'flag_rh_max':[
                              'NaN',],
                      'rh_min':[
                              'NaN',
                              'NP',],
                      'flag_rh_min':[
                              'NaN',],
                      'rh_avg':[
                              'NaN',
                              'NP',],
                      'flag_rh_avg':[
                              'NaN',],
                      'bp_max':[
                              'NaN',
                              'NP',],
                      'flag_bp_max':[
                              'NaN',],
                      'bp_min':[
                              'NaN',
                              'NP',],
                      'flag_bp_min':[
                              'NaN',],
                      'bp_avg':[
                              'NaN',
                              'NP',],
                      'flag_bp_avg':[
                              'NaN',],
                      'ws_max':[
                              'NaN',
                              'NP',],
                      'flag_ws_max':[
                              'NaN',],
                      'ws_min':[
                              'NaN',
                              'NP',],
                      'flag_ws_min':[
                              'NaN',],
                      'ws_avg':[
                              'NaN',
                              'NP',],
                      'flag_ws_avg':[
                              'NaN',],
                      'wd':[
                              'NaN',
                              'NP',],
                      'flag_wd':[
                              'NaN',],
                      'solrad_avg':[
                              'NaN',
                              'NP',],
                      'flag_solrad_avg':[
                              'NaN',],
                      'solrad_tot':[
                              'NaN',
                              'NP',],
                      'flag_solrad_tot':[
                              'NaN',],
                      'ppt_tot':[
                              'NaN',],
                      'flag_ppt_tot':[
                              'NaN',],
                      'snowdepth_avg':[
                              'NaN',
                              'NP',],
                      'flag_snowdepth_avg':[
                              'NaN',],
                      'soiltemp_5cm_max':[
                              'NaN',
                              'NP',],
                      'flag_soiltemp_5cm_max':[
                              'NaN',],
                      'soiltemp_5cm_min':[
                              'NaN',
                              'NP',],
                      'flag_soiltemp_5cm_min':[
                              'NaN',],
                      'soiltemp_5cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soiltemp_5cm_avg':[
                              'NaN',],
                      'soilmoist_5cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoist_5cm_avg':[
                              'NaN',],
                      'soilmoistprof_10cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_10cm_avg':[
                              'NaN',],
                      'soilmoistprof_20cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_20cm_avg':[
                              'NaN',],
                      'soilmoistprof_30cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_30cm_avg':[
                              'NaN',],
                      'soilmoistprof_50cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_50cm_avg':[
                              'NaN',],
                      'soilmoistprof_70cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_70cm_avg':[
                              'NaN',],
                      'soilmoistprof_100cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_100cm_avg':[
                              'NaN',],
                      'soilmoistprof_150cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_150cm_avg':[
                              'NaN',],
                      'soilmoistprof_200cm_avg':[
                              'NaN',
                              'NP',],
                      'flag_soilmoistprof_200cm_avg':[
                              'NaN',],
                      'airtemp_hmp1_max':[
                              'NaN',],
                      'flag_airtemp_hmp1_max':[
                              'NaN',],
                      'airtemp_hmp1_min':[
                              'NaN',],
                      'flag_airtemp_hmp1_min':[
                              'NaN',],
                      'airtemp_hmp1_avg':[
                              'NaN',],
                      'flag_airtemp_hmp1_avg':[
                              'NaN',],
                      'airtemp_hmp2_max':[
                              'NaN',],
                      'flag_airtemp_hmp2_max':[
                              'NaN',],
                      'airtemp_hmp2_min':[
                              'NaN',],
                      'flag_airtemp_hmp2_min':[
                              'NaN',],
                      'airtemp_hmp2_avg':[
                              'NaN',],
                      'flag_airtemp_hmp2_avg':[
                              'NaN',],
                      'airtemp_hmp3_max':[
                              'NaN',],
                      'flag_airtemp_hmp3_max':[
                              'NaN',],
                      'airtemp_hmp3_min':[
                              'NaN',],
                      'flag_airtemp_hmp3_min':[
                              'NaN',],
                      'airtemp_hmp3_avg':[
                              'NaN',],
                      'flag_airtemp_hmp3_avg':[
                              'NaN',],
                      'rh_hmp1_max':[
                              'NaN',],
                      'flag_rh_hmp1_max':[
                              'NaN',],
                      'rh_hmp1_min':[
                              'NaN',],
                      'flag_rh_hmp1_min':[
                              'NaN',],
                      'rh_hmp1_avg':[
                              'NaN',],
                      'flag_rh_hmp1_avg':[
                              'NaN',],
                      'rh_hmp2_max':[
                              'NaN',],
                      'flag_rh_hmp2_max':[
                              'NaN',],
                      'rh_hmp2_min':[
                              'NaN',],
                      'flag_rh_hmp2_min':[
                              'NaN',],
                      'rh_hmp2_avg':[
                              'NaN',],
                      'flag_rh_hmp2_avg':[
                              'NaN',],
                      'rh_hmp3_max':[
                              'NaN',],
                      'flag_rh_hmp3_max':[
                              'NaN',],
                      'rh_hmp3_min':[
                              'NaN',],
                      'flag_rh_hmp3_min':[
                              'NaN',],
                      'rh_hmp3_avg':[
                              'NaN',],
                      'flag_rh_hmp3_avg':[
                              'NaN',],}
        )
    # Coerce the data into the types specified in the metadata
    dt1.LTER_site=dt1.LTER_site.astype('category')
    dt1.local_site=dt1.local_site.astype('category')
    dt1.logger=dt1.logger.astype('category')
    # Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
    # This new column is added to the dataframe but does not show up in automated summaries below.
    #dt1=dt1.assign(date_datetime=pd.to_datetime(dt1.date,errors='coerce'))
    # Since date conversions are tricky, the coerced dates will go into a new column with _datetime appended
    # This new column is added to the dataframe but does not show up in automated summaries below.
    #dt1=dt1.assign(year_datetime=pd.to_datetime(dt1.year,errors='coerce'))
    dt1.jday=pd.to_numeric(dt1.jday,errors='coerce',downcast='integer')
    dt1.airtemp_max=pd.to_numeric(dt1.airtemp_max,errors='coerce')
    dt1.flag_airtemp_max=dt1.flag_airtemp_max.astype('category')
    dt1.airtemp_min=pd.to_numeric(dt1.airtemp_min,errors='coerce')
    dt1.flag_airtemp_min=dt1.flag_airtemp_min.astype('category')
    dt1.airtemp_avg=pd.to_numeric(dt1.airtemp_avg,errors='coerce')
    dt1.flag_airtemp_avg=dt1.flag_airtemp_avg.astype('category')
    dt1.rh_max=pd.to_numeric(dt1.rh_max,errors='coerce')
    dt1.flag_rh_max=dt1.flag_rh_max.astype('category')
    dt1.rh_min=pd.to_numeric(dt1.rh_min,errors='coerce')
    dt1.flag_rh_min=dt1.flag_rh_min.astype('category')
    dt1.rh_avg=pd.to_numeric(dt1.rh_avg,errors='coerce')
    dt1.flag_rh_avg=dt1.flag_rh_avg.astype('category')
    dt1.bp_max=pd.to_numeric(dt1.bp_max,errors='coerce')
    dt1.flag_bp_max=dt1.flag_bp_max.astype('category')
    dt1.bp_min=pd.to_numeric(dt1.bp_min,errors='coerce')
    dt1.flag_bp_min=dt1.flag_bp_min.astype('category')
    dt1.bp_avg=pd.to_numeric(dt1.bp_avg,errors='coerce')
    dt1.flag_bp_avg=dt1.flag_bp_avg.astype('category')
    dt1.ws_max=pd.to_numeric(dt1.ws_max,errors='coerce')
    dt1.flag_ws_max=dt1.flag_ws_max.astype('category')
    dt1.ws_min=pd.to_numeric(dt1.ws_min,errors='coerce')
    dt1.flag_ws_min=dt1.flag_ws_min.astype('category')
    dt1.ws_avg=pd.to_numeric(dt1.ws_avg,errors='coerce')
    dt1.flag_ws_avg=dt1.flag_ws_avg.astype('category')
    dt1.wd=pd.to_numeric(dt1.wd,errors='coerce')
    dt1.flag_wd=dt1.flag_wd.astype('category')
    dt1.solrad_avg=pd.to_numeric(dt1.solrad_avg,errors='coerce')
    dt1.flag_solrad_avg=dt1.flag_solrad_avg.astype('category')
    dt1.solrad_tot=pd.to_numeric(dt1.solrad_tot,errors='coerce')
    dt1.flag_solrad_tot=dt1.flag_solrad_tot.astype('category')
    dt1.ppt_tot=pd.to_numeric(dt1.ppt_tot,errors='coerce')
    dt1.flag_ppt_tot=dt1.flag_ppt_tot.astype('category')
    dt1.snowdepth_avg=pd.to_numeric(dt1.snowdepth_avg,errors='coerce')
    dt1.flag_snowdepth_avg=dt1.flag_snowdepth_avg.astype('category')
    dt1.soiltemp_5cm_max=pd.to_numeric(dt1.soiltemp_5cm_max,errors='coerce')
    dt1.flag_soiltemp_5cm_max=dt1.flag_soiltemp_5cm_max.astype('category')
    dt1.soiltemp_5cm_min=pd.to_numeric(dt1.soiltemp_5cm_min,errors='coerce')
    dt1.flag_soiltemp_5cm_min=dt1.flag_soiltemp_5cm_min.astype('category')
    dt1.soiltemp_5cm_avg=pd.to_numeric(dt1.soiltemp_5cm_avg,errors='coerce')
    dt1.flag_soiltemp_5cm_avg=dt1.flag_soiltemp_5cm_avg.astype('category')
    dt1.soilmoist_5cm_avg=pd.to_numeric(dt1.soilmoist_5cm_avg,errors='coerce')
    dt1.flag_soilmoist_5cm_avg=dt1.flag_soilmoist_5cm_avg.astype('category')
    dt1.soilmoistprof_10cm_avg=pd.to_numeric(dt1.soilmoistprof_10cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_10cm_avg=dt1.flag_soilmoistprof_10cm_avg.astype('category')
    dt1.soilmoistprof_20cm_avg=pd.to_numeric(dt1.soilmoistprof_20cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_20cm_avg=dt1.flag_soilmoistprof_20cm_avg.astype('category')
    dt1.soilmoistprof_30cm_avg=pd.to_numeric(dt1.soilmoistprof_30cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_30cm_avg=dt1.flag_soilmoistprof_30cm_avg.astype('category')
    dt1.soilmoistprof_50cm_avg=pd.to_numeric(dt1.soilmoistprof_50cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_50cm_avg=dt1.flag_soilmoistprof_50cm_avg.astype('category')
    dt1.soilmoistprof_70cm_avg=pd.to_numeric(dt1.soilmoistprof_70cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_70cm_avg=dt1.flag_soilmoistprof_70cm_avg.astype('category')
    dt1.soilmoistprof_100cm_avg=pd.to_numeric(dt1.soilmoistprof_100cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_100cm_avg=dt1.flag_soilmoistprof_100cm_avg.astype('category')
    dt1.soilmoistprof_150cm_avg=pd.to_numeric(dt1.soilmoistprof_150cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_150cm_avg=dt1.flag_soilmoistprof_150cm_avg.astype('category')
    dt1.soilmoistprof_200cm_avg=pd.to_numeric(dt1.soilmoistprof_200cm_avg,errors='coerce')
    dt1.flag_soilmoistprof_200cm_avg=dt1.flag_soilmoistprof_200cm_avg.astype('category')
    dt1.airtemp_hmp1_max=pd.to_numeric(dt1.airtemp_hmp1_max,errors='coerce')
    dt1.flag_airtemp_hmp1_max=dt1.flag_airtemp_hmp1_max.astype('category')
    dt1.airtemp_hmp1_min=pd.to_numeric(dt1.airtemp_hmp1_min,errors='coerce')
    dt1.flag_airtemp_hmp1_min=dt1.flag_airtemp_hmp1_min.astype('category')
    dt1.airtemp_hmp1_avg=pd.to_numeric(dt1.airtemp_hmp1_avg,errors='coerce')
    dt1.flag_airtemp_hmp1_avg=dt1.flag_airtemp_hmp1_avg.astype('category')
    dt1.airtemp_hmp2_max=pd.to_numeric(dt1.airtemp_hmp2_max,errors='coerce')
    dt1.flag_airtemp_hmp2_max=dt1.flag_airtemp_hmp2_max.astype('category')
    dt1.airtemp_hmp2_min=pd.to_numeric(dt1.airtemp_hmp2_min,errors='coerce')
    dt1.flag_airtemp_hmp2_min=dt1.flag_airtemp_hmp2_min.astype('category')
    dt1.airtemp_hmp2_avg=pd.to_numeric(dt1.airtemp_hmp2_avg,errors='coerce')
    dt1.flag_airtemp_hmp2_avg=dt1.flag_airtemp_hmp2_avg.astype('category')
    dt1.airtemp_hmp3_max=pd.to_numeric(dt1.airtemp_hmp3_max,errors='coerce')
    dt1.flag_airtemp_hmp3_max=dt1.flag_airtemp_hmp3_max.astype('category')
    dt1.airtemp_hmp3_min=pd.to_numeric(dt1.airtemp_hmp3_min,errors='coerce')
    dt1.flag_airtemp_hmp3_min=dt1.flag_airtemp_hmp3_min.astype('category')
    dt1.airtemp_hmp3_avg=pd.to_numeric(dt1.airtemp_hmp3_avg,errors='coerce')
    dt1.flag_airtemp_hmp3_avg=dt1.flag_airtemp_hmp3_avg.astype('category')
    dt1.rh_hmp1_max=pd.to_numeric(dt1.rh_hmp1_max,errors='coerce')
    dt1.flag_rh_hmp1_max=dt1.flag_rh_hmp1_max.astype('category')
    dt1.rh_hmp1_min=pd.to_numeric(dt1.rh_hmp1_min,errors='coerce')
    dt1.flag_rh_hmp1_min=dt1.flag_rh_hmp1_min.astype('category')
    dt1.rh_hmp1_avg=pd.to_numeric(dt1.rh_hmp1_avg,errors='coerce')
    dt1.flag_rh_hmp1_avg=dt1.flag_rh_hmp1_avg.astype('category')
    dt1.rh_hmp2_max=pd.to_numeric(dt1.rh_hmp2_max,errors='coerce')
    dt1.flag_rh_hmp2_max=dt1.flag_rh_hmp2_max.astype('category')
    dt1.rh_hmp2_min=pd.to_numeric(dt1.rh_hmp2_min,errors='coerce')
    dt1.flag_rh_hmp2_min=dt1.flag_rh_hmp2_min.astype('category')
    dt1.rh_hmp2_avg=pd.to_numeric(dt1.rh_hmp2_avg,errors='coerce')
    dt1.flag_rh_hmp2_avg=dt1.flag_rh_hmp2_avg.astype('category')
    dt1.rh_hmp3_max=pd.to_numeric(dt1.rh_hmp3_max,errors='coerce')
    dt1.flag_rh_hmp3_max=dt1.flag_rh_hmp3_max.astype('category')
    dt1.rh_hmp3_min=pd.to_numeric(dt1.rh_hmp3_min,errors='coerce')
    dt1.flag_rh_hmp3_min=dt1.flag_rh_hmp3_min.astype('category')
    dt1.rh_hmp3_avg=pd.to_numeric(dt1.rh_hmp3_avg,errors='coerce')
    dt1.flag_rh_hmp3_avg=dt1.flag_rh_hmp3_avg.astype('category')
    dt1 = dt1.set_index('date')
    if verbose:
        print("Here is a description of the data frame dt1 and number of lines\n")
        print(dt1.info())
        print("--------------------\n\n")
        print("Here is a summary of numerical variables in the data frame dt1\n")
        print(dt1.describe())
        print("--------------------\n\n")

        print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")

        print(dt1.LTER_site.describe())
        print("--------------------\n\n")

        print(dt1.local_site.describe())
        print("--------------------\n\n")

        print(dt1.logger.describe())
        print("--------------------\n\n")

        print(dt1.date.describe())
        print("--------------------\n\n")

        #print(dt1.year.describe())
        #print("--------------------\n\n")

        print(dt1.jday.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_max.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_min.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_avg.describe())
        print("--------------------\n\n")

        print(dt1.rh_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_max.describe())
        print("--------------------\n\n")

        print(dt1.rh_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_min.describe())
        print("--------------------\n\n")

        print(dt1.rh_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_avg.describe())
        print("--------------------\n\n")

        print(dt1.bp_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_bp_max.describe())
        print("--------------------\n\n")

        print(dt1.bp_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_bp_min.describe())
        print("--------------------\n\n")

        print(dt1.bp_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_bp_avg.describe())
        print("--------------------\n\n")

        print(dt1.ws_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_ws_max.describe())
        print("--------------------\n\n")

        print(dt1.ws_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_ws_min.describe())
        print("--------------------\n\n")

        print(dt1.ws_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_ws_avg.describe())
        print("--------------------\n\n")

        print(dt1.wd.describe())
        print("--------------------\n\n")

        print(dt1.flag_wd.describe())
        print("--------------------\n\n")

        print(dt1.solrad_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_solrad_avg.describe())
        print("--------------------\n\n")

        print(dt1.solrad_tot.describe())
        print("--------------------\n\n")

        print(dt1.flag_solrad_tot.describe())
        print("--------------------\n\n")

        print(dt1.ppt_tot.describe())
        print("--------------------\n\n")

        print(dt1.flag_ppt_tot.describe())
        print("--------------------\n\n")

        print(dt1.snowdepth_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_snowdepth_avg.describe())
        print("--------------------\n\n")

        print(dt1.soiltemp_5cm_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_soiltemp_5cm_max.describe())
        print("--------------------\n\n")

        print(dt1.soiltemp_5cm_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_soiltemp_5cm_min.describe())
        print("--------------------\n\n")

        print(dt1.soiltemp_5cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soiltemp_5cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoist_5cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoist_5cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_10cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_10cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_20cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_20cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_30cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_30cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_50cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_50cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_70cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_70cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_100cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_100cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_150cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_150cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.soilmoistprof_200cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_soilmoistprof_200cm_avg.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp1_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp1_max.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp1_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp1_min.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp1_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp1_avg.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp2_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp2_max.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp2_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp2_min.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp2_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp2_avg.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp3_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp3_max.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp3_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp3_min.describe())
        print("--------------------\n\n")

        print(dt1.airtemp_hmp3_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_airtemp_hmp3_avg.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp1_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp1_max.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp1_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp1_min.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp1_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp1_avg.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp2_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp2_max.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp2_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp2_min.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp2_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp2_avg.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp3_max.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp3_max.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp3_min.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp3_min.describe())
        print("--------------------\n\n")

        print(dt1.rh_hmp3_avg.describe())
        print("--------------------\n\n")

        print(dt1.flag_rh_hmp3_avg.describe())
        print("--------------------\n\n")
    return dt1
