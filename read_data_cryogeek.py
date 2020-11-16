import numpy as np
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
from datetime import datetime

data_path = '/Users/mistral/Documents/CUBoulder/Science/variousprojects/permafrost/data/Cryogeeks_CalibrationData'
f_list = glob.glob(os.path.join(data_path,'*.csv'))
no_data = ['TIME', '#1:oC', 'HK-BAT:V']#, ' 963 Lines>', ' 961 Lines>', ' 962 Lines>']
for i in range(0, len(f_list)):
    data = pd.read_csv(f_list[i], header = 9, usecols = [1,2,3], skipfooter=1, engine = 'python', na_values = no_data, names = ['datetime','temp', 'bat'])
    data['datetime'] = pd.to_datetime(data['datetime'], format = '%d.%m.%Y %H:%M:%S')
    #data.head()
    plt.plot(data[(data['datetime'] > '15.09.20 18:40') & (data['datetime'] < '15.09.20 20:54')].datetime,
            data[(data['datetime'] > '15.09.20 18:40') & (data['datetime'] <'15.09.20 20:54')].temp)
    plt.title(os.path.basename(f"{f_list[i]}")[:-4])
    plt.vlines(datetime.strptime('15.09.20 18:55', '%d.%m.%y %H:%M'), -0.5, 1.5, color = 'k')
    plt.vlines(datetime.strptime('15.09.20 19:45', '%d.%m.%y %H:%M'), -0.5, 1.5, color = 'k')
    print(data[(data['datetime'] > '15.09.20 18:55') & (data['datetime'] <'15.09.20 19:55')].temp.median())
    plt.show()
    #plt.savefig(f"{f_list[i]}"[:-4]+'.png')
