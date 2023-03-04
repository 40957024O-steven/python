import sys
sys.path.append('packages')
from pathlib import Path
import numpy as np
import pandas as pd
from LidarData import LidarData
import config

rootPath = config.songShanDataPath
cachePath = config.cachePath

def writeCacheFile(df, file):
    if file.suffix == '.parquet':
        df.to_parquet(file)
    elif file.suffix == '.csv':
        df.to_csv(file, index = False)

def readCacheFile(file):
    return pd.read_parquet(file)


# path : 路徑依照每日跑一次
monthPath = '2019-12'

for day in range(1, 10):
    dayPath = '{}-{:02d}'.format(monthPath, day)
    lidarData = LidarData(rootPath / monthPath / dayPath)
    cacheName = '_' + dayPath[:4] + dayPath[5:7] + dayPath[8:10]
    subName = '.csv'
    writeCacheFile(lidarData.sequenceDatas, cachePath / (cacheName + '_level1' + subName))
    writeCacheFile(lidarData.losDatas, cachePath / (cacheName + '_level2' + subName))
    writeCacheFile(lidarData.uvDatas, cachePath / (cacheName + '_uv' + subName))

