"""
1 June 2020
Author: Xiandi Ooi

This is a file for exploring the data visualization.

We will be looking at the API values in each area across time. 

"""
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

#the data can be retrived from our github repo
df = pd.read_csv("https://www.dropbox.com/s/84hol3lm6tdehe7/Aggregate-API.csv?dl=1", sep = ";")

selected_area = "Sandakan" #any area
df_temp = df.loc[(df.Area == selected_area),
                 ["Datetime", "API_Values"]]

#or you can use the following query version if you prefer 
#df_temp = df[["Datetime", "API_Values"]].query('Area == selected_area and start_time <= Datetime < end_time')

#the following code is sourced from Plotly Graphing Libraries > Custom Controls > Range Slider and Selector
#initiate the figure
fig = go.Figure()

fig.add_trace(go.Scatter(x = list(df_temp["Datetime"]), 
                         y = list(df_temp["API_Values"])))

#set title
fig.update_layout(
    title_text = "API Values in {}".format(selected_area))

#adding range slider
fig.update_layout(xaxis = 
                  dict(rangeselector = 
                               dict(buttons = 
                                    list([dict(count=1,
                                               label="1m",
                                               step="month",
                                               stepmode="backward"),
                                          dict(count=1,
                                               label="1y",
                                               step="year",
                                               stepmode="backward"),
                                          dict(step="all")])),
                               rangeslider = dict(visible = True),
                               type="date"))

#plotting the figure in a browser if you are using a local IDE
plot(fig)
