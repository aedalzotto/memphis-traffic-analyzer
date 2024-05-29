import pandas as pd
from os import listdir

class DMNI:
    def __init__(self, scen_path):
        dmni_path = "{}/debug/dmni".format(scen_path)
        dmni_logs = ["{}/{}".format(dmni_path, s) for s in listdir(dmni_path)]

        self._df = pd.concat(map(pd.read_csv, dmni_logs), ignore_index=True)

        self._df['timestamp']  = self._df['timestamp']  / 100000.0

        self._df['cons'] = self._df['cons'].apply(str).apply(int, base=16)
        self._df['app']  = self._df['cons'].apply(lambda x: x >> 8)
        self._df.drop(self._df[self._df['app'] > 0xFF].index,     inplace=True)
        self._df.drop(self._df[self._df['app'] == 0].index,       inplace=True)

        self._df['prod'] = self._df['prod'].apply(str).apply(int, base=16)
        self._df['cons'] = self._df['cons'] & 0xFF
        self._df['prod'] = self._df['prod'] & 0xFF

        self._df['total_time'] = self._df['total_time'] / 100.0
        self._df['noc_time']   = self._df['noc_time']   / 100.0
        self._df['dmni_time']  = self._df['total_time'] - self._df['noc_time']
        
        self._df.sort_values(by='timestamp', inplace = True)

        self._df.reset_index(drop = True, inplace = True)

    @property
    def df(self):
        return self._df

    def __getitem__(self, key):
        return self._df[self._df['app'] == key]
