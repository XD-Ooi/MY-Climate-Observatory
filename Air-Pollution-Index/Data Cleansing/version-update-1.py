"""
6 Jun 2020
Author: Xiandi Ooi

Dataset version update 01 

These are issues were identified during the visualization process.

"""
import pandas as pd 
import numpy as np

df = pd.read_csv(r"filepath\aggregateAPI.csv")

#Fixing some comma space issue
df["Area"] = df["Area"].str.replace("Batu Muda,Kuala Lumpur", 
                                    "Batu Muda, Kuala Lumpur")
df["Area"] = df["Area"].str.replace("Cheras,Kuala Lumpur", 
                                    "Cheras, Kuala Lumpur")

#The original API values for nan is 0, we've decided to change it back to nan
df["API_Values"] = df["API_Values"].replace(0, np.nan)

#State value error for Balok Baru, Kuantan data
df["State"] = df["State"].str.replace("Kuantan", "Pahang")

#Area value error for Tanah Merah, Kelantan
df["Area"] = df["Area"].str.replace("Tanah Merah ", "Tanah Merah")

#We will create new dataframes for interim period where there's no data
#Missing nan values for Putrajaya between 25-12-2006 to 30-01-2007
ptjy_missing = pd.date_range(start="2006-12-26", end="2007-01-29", freq = "D")
ptjy_datetime = pd.Series(ptjy_missing)
ptjy_df = pd.DataFrame({"API_Values": [np.nan],
                        "State": ["Wilayah Persekutuan"],
                        "Area": ["Putrajaya"]})
ptjy = pd.concat([ptjy_df]*(len(ptjy_datetime)), ignore_index = True)
df_putrajaya = ptjy.join(ptjy_datetime.rename("Datetime"))

#Missing nan values for SMK Tanjung Chat, Kota Bharu between 18-01-2012 to 01-07-2012
kb_missing = pd.date_range(start="2012-01-17", end="2012-07-01", freq = "D")
kb_datetime = pd.Series(kb_missing)
kb_df = pd.DataFrame({"API_Values": [np.nan],
                      "State": ["Kelantan"],
                      "Area": ["SMK Tanjung Chat, Kota Bharu"]})
kb = pd.concat([kb_df]*(len(kb_datetime)), ignore_index = True)
df_kb = kb.join(kb_datetime.rename("Datetime"))

#Missing nan values for Cheras, KL between 05-08-2008 to 04-02-2009
cheras_missing = pd.date_range(start="2008-08-15", end="2009-02-04", freq = "D")
cheras_datetime = pd.Series(cheras_missing)
cheras_df = pd.DataFrame({"API_Values": [np.nan],
                          "State": ["Wilayah Persekutuan"],
                          "Area": ["Cheras, Kuala Lumpur"]})
cheras = pd.concat([cheras_df]*(len(cheras_datetime)), ignore_index = True)
df_cheras = cheras.join(cheras_datetime.rename("Datetime"))


#Joining the additional dataframe to our original dateframe
df_update = pd.concat([df, df_putrajaya, df_kb, df_cheras])

#Output our file csv file
df_update.to_csv(r"filepath\Aggregate-API.csv")
