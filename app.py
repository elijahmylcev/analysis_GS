import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash
from dash import html
import plotly.io as pol

from rename import rename_columns, re_columns_names
from sum_category import sum_category


pol.renderers.default = 'browser'
app = dash.Dash(__name__)

df = pd.read_csv('./data.csv')
# rename
df = rename_columns(df, re_columns_names)
df.loc[(df['email'] == 0)|(df['email'].isnull()), 'email'] = 'Не оставил'
df.loc[(df['email'] == 1), 'email'] = 'Оставил'

# Целевая аудитория - те, кто тратит больше всего денег на самообразование
data_max_money = df[df['amount_money'] == 'до 10000р']
data_max_money

data_medium_money = df[df['amount_money'] == 'до 5000р']
data_min_money = df[df['amount_money'] == 'до 1000р']

# Они оценивают существующие сервисы в среднем на
med_grade = data_max_money['grade_exist_services'].to_list()
med_grade_sum = sum(med_grade)/len(med_grade)
med_grade_sum
# 2.25
count_categories_df = sum_category(df, re_columns_names[33:41])
# figure
bar_interesting = px.bar(
    count_categories_df,
    x='category', y='count',
    title="Интерес к предметам изучения",
    color='count',
    text_auto='.2s',
)

bar_interesting.update_traces(textposition='outside')

bar_interesting.update_layout(
    barmode='stack',
    xaxis={'categoryorder': 'total descending'},
)

tab1_content = [
    html.Div([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure=bar_interesting
                )
            ], width=4),
            dbc.Col([
                html.Div('Hello')
            ], width=4)
        ])
    ])
]

tab2_content = [
    html.Div('Hello')
]

app.layout = html.Div([
  html.H1(children="Риски по ССЗ Омск"),

  dbc.Tabs([
    dbc.Tab(tab1_content, label="Статистика"),
    dbc.Tab(tab2_content, label="Пациенты в МО"),
  ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
