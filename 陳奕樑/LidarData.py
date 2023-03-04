from pathlib import Path
import numpy as np
import pandas as pd

# 資料確認需要的欄位
_needColumns = [
    'Timestamp',
    'Settings ID',
    'Resolution ID',
    'Scan ID',
    'LOS ID',
    'Sequence ID',
    'Azimuth [財',
    'Elevation [財',
    'Altitude [m]',
    'Horizontal Wind Speed [m/s]',
    'Vertical Wind Speed [m/s]',
    'Horizontal Wind Direction [財',
    'Radial Wind Speed [m/s]',
    'CNR [dB]',
    'Confidence Index [%]',
    'Confidence Index Status',
]

class LidarDataError(Exception):
    pass

class LidarData:

    def __init__(self, srcPath):
        self._srcPath = srcPath
        self.createCacheData(srcPath)

    # 分析資料格式並取得資料的 SequenceID
    def _parseSequenceID(self, df):
        # check columns
        if len(df.columns) != len(_needColumns):
            raise LidarDataError('columns length diff')
        for i,j in zip(df.columns, _needColumns):
            if i != j:
                raise LidarDataError('columns {} <> {}'.format(i, j))

        # 經過檢查，並非都是 37，2019/12/01, 02 就是 44
        # if not np.all(df['Settings ID'] == 37):
        #    return False, 'Settings ID != 37'
        if not np.all(df['Resolution ID'] == 8):
            raise LidarDataError('Resolution ID != 8')
        # 經過檢查，並非都是 74，2019/12/01, 02 就是 103
        #if not np.all(df['Scan ID'] == 74):
        #    return False, 'Scan ID != 74'

        sequenceID = df['Sequence ID'][0]
        if not np.all(df['Sequence ID'] == sequenceID):
            raise LidarDataError('Sequence ID not all the same')

        return sequenceID

    def _parseLOSData(self, df):
        allData = []
        currentLosID = 0
        for index, group in df.groupby('Timestamp'):
            losID = group['LOS ID'].iloc[0]
            if not np.all(group['LOS ID'] == losID):
                raise LidarDataError('{} Timestamp : {} not all LOS IDthe same'.format(self._file, index))
            if losID != currentLosID:
                continue
            data = self._parseOneLOSData(losID, group)
            allData.append(data)
            # only get losID from 0~3 one time
            currentLosID += 1
            if currentLosID == 4:
                break
        if len(allData) == 0:
            return pd.DataFrame(columns = ['Azimuth','Elevation','LosID','Timestamp'])
        return pd.DataFrame(allData)
    """
    def _parseLOSData(self, df):
        allData = []
        for index, group in df.groupby('LOS ID'):
            if index < 0 or index > 4:
                raise LidarDataError('illegal LOS ID {}'.format(index))
            if index >= 0 and index < 4:
                # not check vertical scan #
                data = self._parseOneLOSData(index, group)
                allData.append(data)
        if len(allData) == 0:
            return pd.DataFrame(columns = ['Azimuth','Elevation','LosID','Timestamp'])
        return pd.DataFrame(allData)
    """

    def _parseOneLOSData(self, LosID, df):
        Timestamp = df['Timestamp'].iat[0]
        if not np.all(df['Timestamp'] == Timestamp):
            raise LidarDataError('{} Los ID: {} Timestamp not all the same'.format(self._file, LosID))

        Azimuth = df['Azimuth [財'].iat[0]
        if not np.all(df['Azimuth [財'] == Azimuth):
            raise LidarDataError('{} Los ID: {} Azimuth not all the same'.format(self._file, LosID))

        Elevation = df['Elevation [財'].iat[0]
        if not np.all(df['Elevation [財'] == Elevation):
            raise LidarDataError('{} Los ID: {} Elevation not all the same'.format(self._file, LosID))

        return {'LosID':LosID, 'Timestamp':Timestamp, 'Azimuth':Azimuth, 'Elevation':Elevation}

    # 取的隨高度的風場資料
    def _getUVbyAlt(self, df):
        data = df[df['Confidence Index Status'] == 1][['LOS ID', 'Altitude [m]', 'Radial Wind Speed [m/s]']]
        data.columns = ['LosID', 'Altitude', 'RWS']
        data = data.set_index('Altitude')
        angle = 15

        m = []
        keys = ['n', 'e', 's', 'w']
        for i, key in enumerate(keys):
            m.append(data[data['LosID'] == i]['RWS'].rename(key))
        m = pd.concat(m, axis = 1).dropna()
    
        m['u'] = (m.loc[:,'w'] - m.loc[:,'e']) / (2. * np.sin(angle * np.pi / 180.))
        m['v'] = (m.loc[:,'s'] - m.loc[:,'n']) / (2. * np.sin(angle * np.pi / 180.))
        m = (m.reset_index())[['Altitude', 'u', 'v']]
        return m

    @property
    def sequenceDatas(self):
        return self._sequenceDatas

    @property
    def losDatas(self):
        return self._losDatas

    @property
    def uvDatas(self):
        return self._uvDatas

    def createCacheData(self, srcPath):
        files = sorted(srcPath.glob('**/*.csv'))

        sequenceDatas = []
        losDatas = []
        uvDatas = []

        for i, file in enumerate(files):
            self._file = file
            df = pd.read_csv(file, encoding='big5', sep=';', parse_dates=['Timestamp'])
        
            sequenceID = self._parseSequenceID(df)
            losData = self._parseLOSData(df)
            
            # 檢查 仰角要在 75左右，方位角要在 0, 90, 180, 270 左右
            az = (losData['Azimuth'] - (losData['LosID'] * 90)) % 360
            el = losData['Elevation'] - 75
            if not np.all((az > -359.9) | (az < 0.1)):
                raise LidarDataError('{} az diff over 0.1'.format(file))
            if not np.all((el > -0.1) & (el < 0.1)):
                raise LidarDataError('{} el diff over 0.1'.format(file))
            
            scanTime = losData['Timestamp'].min() # 所有掃描的最小時間(作為本次掃描的標準時間)

            sequenceDatas.append({'ScanTime':scanTime, 'SequenceID':sequenceID})
            losData['SequenceID'] = sequenceID
            losDatas.append(losData)

            # 過濾 losData 取出的資料
            uv = self._getUVbyAlt(df[df['Timestamp'].isin(losData['Timestamp'])])
            uv['Timestamp'] = scanTime
            uvDatas.append(uv)

        if len(sequenceDatas) == 0:
            self._sequenceDatas = pd.DataFrame(columns = ['ScanTime','SequenceID'])
        else:
            self._sequenceDatas = pd.DataFrame(sequenceDatas)

        if len(losDatas) == 0:
            self._losDatas = pd.DataFrame(columns = [
                'Azimuth','Elevation','LosID','Timestamp','SequenceID'])
        else:
            self._losDatas = pd.concat(losDatas)
        
        if len(uvDatas) == 0:
            self._uvDatas = pd.DataFrame(columns = [
                'Altitude','u','v','Timestamp'])
        else:
            self._uvDatas = pd.concat(uvDatas)
