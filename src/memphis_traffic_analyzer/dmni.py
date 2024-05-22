import pandas as pd
from os import listdir

class DMNI:
    def __init__(self, scen_path):
        dmni_path = "{}/debug/dmni".format(scen_path)
        dmni_logs = ["{}/{}".format(dmni_path, s) for s in listdir(dmni_path)]

        self.df = pd.concat(map(pd.read_csv, dmni_logs), ignore_index=True)

        self.df['timestamp']  = self.df['timestamp']  / 100000.0

        self.df['cons'] = self.df['cons'].apply(str).apply(int, base=16)
        self.df['app']  = self.df['cons'].apply(lambda x: x >> 8)
        self.df.drop(self.df[self.df['app'] > 0xFF].index,     inplace=True)
        self.df.drop(self.df[self.df['app'] == 0].index,       inplace=True)

        self.df['prod'] = self.df['prod'].apply(str).apply(int, base=16)
        self.df['cons'] = self.df['cons'] & 0xFF
        self.df['prod'] = self.df['prod'] & 0xFF

        self.df['total_time'] = self.df['total_time'] / 100.0
        self.df['noc_time']   = self.df['noc_time']   / 100.0
        self.df['dmni_time']  = self.df['total_time'] - self.df['noc_time']
        
        self.df.sort_values(by='timestamp', inplace = True)

        self.df.reset_index(drop = True, inplace = True)

    def __getitem__(self, key):
        return self.df[self.df['app'] == key]
