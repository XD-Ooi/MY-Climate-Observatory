"""
17 June 2020
Author: Xiandi Ooi

Visualizing the types of pollutants.
 
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go

df = pd.read_csv(r"C:\Users\Xiandi\Desktop\Python\Aggregate-API.csv", sep = ";")

# Data wrangling for this particular visual
df_update = df.set_index(pd.DatetimeIndex(df["Datetime"]))
df_update.drop(df_update.columns[4], axis = 1, inplace = True)

# Make the selection
selected_area = "Sandakan"

df_temp = df_update.loc[(df_update.Area == selected_area),
                        ["Area", "Dominant"]]

# Wrangling 
df_group_time = df_update.groupby(pd.Grouper(freq = "Q")).size().reset_index(name = "Total")

df_group = df_update.groupby([pd.Grouper(freq = "Q"),
                              pd.Grouper("Dominant")]).size().reset_index(name = "Count")
df_output = df_group.set_index("Datetime").join(df_group_time.set_index("Datetime"))
df_output["Frequency"] = df_output["Count"] / df_output["Total"]

# Creating df subset for the stacked bars, here we are only dealing with the main dominant pollutants
df_pm2_5 = df_output.loc[(df_output.Dominant == "**")]
df_pm10 = df_output.loc[(df_output.Dominant == "*")]
df_so2 = df_output.loc[(df_output.Dominant == "a")]
df_no2 = df_output.loc[(df_output.Dominant == "b")]
df_o3 = df_output.loc[(df_output.Dominant == "c")]
df_co = df_output.loc[(df_output.Dominant == "d")]

# Now comes the bar chart
fig = go.Figure()

fig.add_trace(go.Bar(x = df_pm2_5.index, 
                     y = df_pm2_5["Frequency"],
                     name = "PM 2.5"))

fig.add_trace(go.Bar(x = df_pm10.index, 
                     y = df_pm10["Frequency"],
                     name = "PM 10"))

fig.add_trace(go.Bar(x = df_so2.index, 
                     y = df_so2["Frequency"],
                     name = "SO2"))

fig.add_trace(go.Bar(x = df_no2.index, 
                     y = df_no2["Frequency"],
                     name = "NO2"))

fig.add_trace(go.Bar(x = df_o3.index, 
                     y = df_o3["Frequency"],
                     name = "O3"))

fig.add_trace(go.Bar(x = df_co.index, 
                     y = df_co["Frequency"],
                     name = "CO"))

fig.update_layout(barmode = "stack", title_text="Frequency of Detected Pollutants")

plot(fig)
