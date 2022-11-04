import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
from dash import html

from rename import rename_columns, re_columns_names

pio.renderers.default='notebook'

df = pd.read_csv('./data.csv')
# rename
df = rename_columns(df, re_columns_names)
print(df)
