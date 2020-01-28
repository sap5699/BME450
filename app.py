import os
import pathlib
import re

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import cufflinks as cf

app = dash.Dash(
        __name__
        )

mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNqdnBvNDMyaTAxYzkzeW5ubWdpZ2VjbmMifQ.TXcBE-xg9BFdV2ocecc_7g"

df_lat_lon = pd.read_csv(
        "lat_lon_counties.csv"
        )
df_lat_lon["FIPS "] = df_lat_lon["FIPS "].apply(lambda x: str(x).zfill(5))

df_full_data = pd.read_csv("age_adjusted_death_rate_no_quotes.csv")
df_full_data["County Code"] = df_full_data["County Code"].apply(lambda x: str(x).zfill(5))
df_full_data["County"] = (df_full_data["Unnamed: 0"] + ", " + df_full_data.County.map(str))

server = app.server

header = html.Div(
        id="header",
        children=[
            html.H1("MONKEY TRACKER")
            ]
        )

graph = dcc.Graph(
        id = "heatmap",
        figure=dict(
                data=[
                    dict(
                        lat=df_lat_lon["Latitude "],
                        lon=df_lat_lon["Longitude"],
                        text=df_lat_lon["Hover"],
                        type="scattermapbox",
                        )
                    ],
                    layout=dict(
                            mapbox=dict(
                                layers=[],
                                accesstoken=mapbox_access_token,
                                style=mapbox_style,
                                center=dict(lat=38.72490, lon=-95.61446),
                                pitch=0,
                                zoom=3.5
                                ),
                            autosize=True
                        ),
            )
        )

app.layout = html.Div(
        id="root",
        children=[
            header,
            graph
            ]
        )


if __name__ == "__main__":
    app.run_server(debug=True)
