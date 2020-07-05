"""
2 June 2020
Author: Xiandi Ooi

For the first dashboard on API values of a particular area across time. 

"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#the data can be retrived from our github repo
#df_master = pd.read_csv("https://www.dropbox.com/s/84hol3lm6tdehe7/Aggregate-API.csv?dl=1", sep = ";")
#df_master = pd.read_csv("https://media.githubusercontent.com/media/XD-Ooi/MY-Climate-Observatory/master/Air-Pollution-Index/Aggregate-API.csv", sep = ";")
df = pd.read_csv(r"C:\Users\Xiandi\Desktop\Python\Aggregate-API.csv", sep = ";")

#preparing the items for the drop down menu
state_group = df.groupby("State")
state_area = state_group.apply(lambda x: x["Area"].unique())
selection = state_area.to_dict()

#initiating the dash object 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#setting up the layout of our dashboard
app.title = "MY Climate Observatory"

app.layout = html.Div([
    html.Div([
        html.Img(
            src = "https://raw.githubusercontent.com/XD-Ooi/MY-Climate-Observatory/master/Pictorial-assets/MYCO-logo.png",
            alt = "MY Climate Observatory",
            style = {"height": "10%",
                     "width": "10%",
                     "float": "left",
                     "position": "relative",
                     "margin-left": "5%",
                     "padding-top": 5})]),
    
    html.Div([
        html.Div("MY Climate Observatory",
                style = {"textAlign": "left",
                         "font-family": "Verdana",
                         "font-size": 24,
                         "clear":"left",
                         "margin-left": "5%"}),
        
        html.Div("Explore | Question | Have Fun",
                 style = {"textAlign": "left",
                          "font-family": "Verdana",
                          "font-size": 16,
                          "clear":"left",
                          "margin-left": "5%",
                          "padding-bottom": 10})],
        style = {"background-color": "#E8E8E8"}),
    
    dcc.Markdown(
        """
        **How has the air pollution level changed across time?**

        This graph displays the Air Pollution Index (API) values of each station throughout Malaysia.
        Use the dropdown menu to select an area and start exploring! 
        
        Is our air less polluted than before?
        Notice the trends and start asking questions about the peculiarities you discovered!
        
        *Please be patient while the data loads.*      
        """,
        style = {"font-family": "Arial",
                 "font-size": 16,
                 "float": "center",
                 "clear": "left",
                 "padding-top": 16,
                 "margin-left": "5%",
                 "margin-right": "5%"}),
    
    html.Div([    
        html.Div([
            html.Label("Select a State"),
            
            dcc.Dropdown(
                id = "state-select",
                options = [{"label": i, "value": i} for i in selection.keys()],
                value = "Wilayah Persekutuan",
                style={"width": "250px"})], 
            className = "three columns"),
    
        html.Div([
            html.Label("Select an Area"),
            
            dcc.Dropdown(
                id = "area-select",
                value = "Batu Muda, Kuala Lumpur",
                style={"width": "250px"})],
            className = "nine columns")], 
        style = {"margin-left": "5%",
                 "font-family": "Arial",
                 "font-size": 16},
        className = "row"),

    dcc.Graph(id = "Multi-area-API",
              style = {"margin-left": "5%",
                       "margin-right": "5%"}),
    
    html.Div([
        html.Div([
            dcc.Graph(id = "API-time-series")],
                      className = "six columns"),
        html.Div([            
            dcc.Graph(id = "Pollutant-frequency")],
                      className = "six columns")],
        style = {"margin-left": "5%",
                 "margin-right": "5%"},
        className = "row"),    
    
    dcc.Markdown(
        """
        The dataset used to develop our dashboard is accessible 
        [here](https://www.dropbox.com/s/84hol3lm6tdehe7/Aggregate-API.csv?dl=1).
        The data is sourced from [data.gov.my](http://www.data.gov.my/).""",
        style = {"font-family": "Arial",
                 "font-size": 16,
                 "float": "center",
                 "clear": "left",
                 "padding-bottom": 12,
                 "margin-left": "5%",
                 "margin-right": "5%"}),
    
    html.Div([  
        html.Div([    
            html.Div([       
                dcc.Markdown(
                    """
                    **About Us**
                    
                    MY Climate Observatory is a non-profit platform working towards accessible climate
                    education. We aim to bridge the data gap in climate education by 
                    putting available climate-related data together, and sharing them in an interactive manner.
                    
                    [![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)
                    
                    """,
                    style={"font-family": "Arial",
                           "font-size": 16,
                           "padding-top": 24,
                           "padding-bottom": 24,
                           "margin-right": "5%"}
                    )], 
                className = "six columns"),
        
            html.Div([
                dcc.Markdown(
                    """
                    **Contact Us**
                               
                    my.climate.observatory@gmail.com
                    """,
                    style={"font-family": "Arial",
                           "font-size": 16,
                           "padding-top": 24}),
                
                html.Div([
                    html.Div([
                        html.A([
                            html.Img(
                                src = "https://raw.githubusercontent.com/XD-Ooi/MY-Climate-Observatory/master/Pictorial-assets/github-icon.png",
                                alt = "Github",
                                style = {"height": "30px",
                                         "width": "30px",
                                         "float": "left",
                                         "position": "static"})],
                            href = "https://github.com/XD-Ooi/MY-Climate-Observatory")],
                        className = "two columns"),
                    
                    html.Div([
                        html.A([
                            html.Img(
                                src = "https://raw.githubusercontent.com/XD-Ooi/MY-Climate-Observatory/master/Pictorial-assets/linkedin-icon.png",
                                alt = "Github",
                                style = {"height": "30px",
                                         "width": "30px",
                                         "float": "left",
                                         "position": "static"})],
                            href = "https://www.linkedin.com/company/my-climate-observatory/")],
                        className = "four columns")])],
                className = "six columns")],
            style = {"margin-left": "5%",
                     "margin-right": "5%"},
            className = "row"),
        
        html.Hr(),
        
        dcc.Markdown(
            """
            © 2020 MY Climate Observatory, All Rights Reserved.
            """,
            style = {"font-family": "Arial",
                     "font-size": 12,
                     "display": "inline-block",
                     "margin-left": "5%"})],
        style = {"background-color": "#E8E8E8",
                 "overflow": "auto"}), #set overflow as auto because the content collapses when the children are floated
    ])

@app.callback(
    Output("area-select", "options"),
    [Input("state-select", "value")])
def update_state_select(selected_state):
    return [{"label": k, "value": k} for k in selection[selected_state]]

@app.callback(
    Output("Multi-area-API", "figure"),
    [Input("state-select", "value")])
def update_multi_area_api(selected_state):
    df_multi_api = df.loc[(df.State == selected_state),
                               ["Datetime", "API_Values", "Area"]]

    multi_api = px.scatter(df_multi_api, x = "Datetime", y = "API_Values",
                           color = "Area", opacity = 0.5)

    multi_api.update_traces(marker = dict(line = dict(width = 0.35,
                                                      color = "black")),
                            selector = dict(mode="markers"))

    multi_api.update_layout(title_text = "Comparing API Values across {}.".format(selected_state))
    multi_api.update_xaxes(title_font=dict(size=1, color = "white"))
    multi_api.update_yaxes(title_font=dict(size=1, color = "white"))
    return multi_api

@app.callback(
    Output("API-time-series", "figure"),
    [Input("area-select", "value"),
     Input("state-select", "value")])
def update_api_ts(selected_area, selected_state):
    df_api_ts = df.loc[(df.Area == selected_area),
                         ["Datetime", "API_Values"]]
    #plot the time series graph
    api_ts = go.Figure()
    
    api_ts.add_trace(go.Scatter(x = list(df_api_ts["Datetime"]), 
                             y = list(df_api_ts["API_Values"]),
                             connectgaps = False))
    
    api_ts.update_layout(title_text = "API Values in {}, {}".format(selected_area, selected_state))
    
    #soured from Plotly Graphing Libraries > Custom Controls > Range Slider and Selector
    api_ts.update_layout(xaxis = 
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
    return api_ts   

@app.callback(
    Output("Pollutant-frequency", "figure"),
    [Input("area-select", "value"),
     Input("state-select", "value")])
def update_pol_freq(selected_area, selected_state):
    df_pol_freq = df.loc[(df.Area == selected_area),
                        ["Area", "Dominant", "Datetime"]]

    # Wrangling 
    df_update = df_pol_freq.set_index(pd.DatetimeIndex(df_pol_freq["Datetime"]))
    df_update.drop(df_update.columns[2], axis = 1, inplace = True)
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
    pol_freq = go.Figure()
    pol_freq.add_trace(go.Bar(x = df_pm2_5.index, 
                         y = df_pm2_5["Frequency"],
                         name = "PM 2.5"))
    pol_freq.add_trace(go.Bar(x = df_pm10.index, 
                         y = df_pm10["Frequency"],
                         name = "PM 10"))
    pol_freq.add_trace(go.Bar(x = df_so2.index, 
                         y = df_so2["Frequency"],
                         name = "SO2"))
    pol_freq.add_trace(go.Bar(x = df_no2.index, 
                         y = df_no2["Frequency"],
                         name = "NO2"))
    pol_freq.add_trace(go.Bar(x = df_o3.index, 
                         y = df_o3["Frequency"],
                         name = "O3"))
    pol_freq.add_trace(go.Bar(x = df_co.index, 
                         y = df_co["Frequency"],
                         name = "CO"))
    pol_freq.update_layout(barmode = "stack", 
                           title_text = "Frequency of Detected Pollutants in {}, {}".format(selected_area, selected_state))
    return pol_freq

if __name__ == '__main__':
    app.run_server(debug = True)
