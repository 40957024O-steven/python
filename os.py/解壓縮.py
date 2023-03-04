import gzip

def un_gf(file_name):
    f_name = file_name.replace(".gz","")
    g_file = gzip.GzipFile(file_name)
    open(f_name,"wb+").write(g_file.read())
    g_file.close()


f = "C:/Users/steve/Desktop/python相關資料/test/wind_reconstruction_data/00-00/WLS100s-46_WindReconstructionData_2019-01-19_00-00-06_DBS_74_25m.csv.gz"

un_gf(f)