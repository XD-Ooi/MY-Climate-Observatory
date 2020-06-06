"""
30 May 2020
Author: Xiandi Ooi

After we have cleaned all the datasets, we will now combine everything into a 
single dataframe.

Saving it as csv for the moment as we are still trying to figure out how we can
best share this data. 

"""
import pandas as pd

#Simple calling of all the cleaned csv files with the file path censored
df1 = pd.read_csv(r"file_path\API_2005_2013_cleaned.csv")
df2 = pd.read_csv(r"file_path\API_2013_2014_cleaned.csv")
df3 = pd.read_csv(r"file_path\API_2014_2015_cleaned.csv")
df4 = pd.read_csv(r"file_path\API_2015_cleaned.csv")
df5 = pd.read_csv(r"file_path\API_2016_cleaned.csv")
df6 = pd.read_csv(r"file_path\API_Johor_2017_cleaned.csv")
df7 = pd.read_csv(r"file_path\API_Johor_2018_cleaned.csv")
df8 = pd.read_csv(r"file_path\API_Johor_2019_cleaned.csv")
df9 = pd.read_csv(r"file_path\API_Kedah_2017_cleaned.csv")
df10 = pd.read_csv(r"file_path\API_Kedah_2018_cleaned.csv")
df11 = pd.read_csv(r"file_path\API_Kedah_2019_cleaned.csv")
df12 = pd.read_csv(r"file_path\API_Kelantan_2017_cleaned.csv")
df13 = pd.read_csv(r"file_path\API_Kelantan_2018_cleaned.csv")
df14 = pd.read_csv(r"file_path\API_Kelantan_2019_cleaned.csv")
df15 = pd.read_csv(r"file_path\API_KL_2017_cleaned.csv")
df16 = pd.read_csv(r"file_path\API_Melaka_2017_cleaned.csv")
df17 = pd.read_csv(r"file_path\API_Melaka_2018_cleaned.csv")
df18 = pd.read_csv(r"file_path\API_NS_2017_cleaned.csv")
df19 = pd.read_csv(r"file_path\API_NS_2018_cleaned.csv")
df20 = pd.read_csv(r"file_path\API_Pahang_2017_cleaned.csv")
df21 = pd.read_csv(r"file_path\API_Pahang_2018_cleaned.csv")
df22 = pd.read_csv(r"file_path\API_Penang_2017_cleaned.csv")
df23 = pd.read_csv(r"file_path\API_Penang_2018_cleaned.csv")
df24 = pd.read_csv(r"file_path\API_Perak_2017_cleaned.csv")
df25 = pd.read_csv(r"file_path\API_Perak_2018_cleaned.csv")
df26 = pd.read_csv(r"file_path\API_Perlis_2017_cleaned.csv")
df27 = pd.read_csv(r"file_path\API_Perlis_2018_cleaned.csv")
df28 = pd.read_csv(r"file_path\API_Putrajaya_2017_cleaned.csv")
df29 = pd.read_csv(r"file_path\API_Sabah_2017_cleaned.csv")
df30 = pd.read_csv(r"file_path\API_Sabah_2018_cleaned.csv")
df31 = pd.read_csv(r"file_path\API_Sarawak_2017_cleaned.csv")
df32 = pd.read_csv(r"file_path\API_Sarawak_2018_cleaned.csv")
df33 = pd.read_csv(r"file_path\API_Terengganu_2017_cleaned.csv")
df34 = pd.read_csv(r"file_path\API_Terengganu_2018_cleaned.csv")

df_total = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10,
                      df11, df12, df13, df14, df15, df16, df17, df18, df19, df20,
                      df21, df22, df23, df24, df25, df26, df27, df28, df29, df30,
                      df31, df32, df33, df34])
df_total = df_total.drop(columns = ["Unnamed: 0"])

#Output our file csv file
df_total.to_csv(r"file_path\aggregateAPI.csv")
