"""
14 June 2020
Author: Xiandi Ooi

Dataset version update 02
 
These are issues were identified during the visualization process.

"""

import pandas as pd
import numpy as np

df = pd.read_csv(r"pathdirectory\Aggregate-API.csv", sep = ";")
df = df.drop(columns = ["Unnamed: 0"])

# Changing 0 to NaN as we noticed it is necessary for our visualizations
df["API_Values"] = df["API_Values"].replace(0, np.nan)

# Making sure our df won't have the column "Unnamed:0" when we load it again
df_update.to_csv(r"pathdirectory\Aggregate-API.csv", sep = ";", index = False)
