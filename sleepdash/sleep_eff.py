from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


# read the csv files into dataframes
efficiency = pd.read_csv('data/Sleep_Efficiency.csv')
times = pd.read_csv('data/sleepdata_2.csv')
print(efficiency)
app = Dash(__name__)


# layout for the dashboard
app.layout = html.Div([
    html.H1("snoozless", style={'textAlign': 'center'})

    # div for Deep Sleep v. REM Percentages
    html.Div([

    ])

])

@app.callback(
    Output()
    Input()
)
def update_sleep_corr():

x = efficiency['REM sleep percentage']
y = efficiency['Deep sleep percentage']
plt.scatter(x, y)
plt.show()