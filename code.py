# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Погода": ["Хабаровск", "Комсомольск-на-Амуре", "Амурск", "Хабаровск", "Комсомольск-на-Амуре", "Амурск"],
    "Показатели": [40, 10, 20, 20, 40, 50],
    "Обозначения": ["Влажность %", "Влажность %", "Влажность %", "Температура C", "Температура C", "Температура C"]
})

fig = px.bar(df, x="Погода", y="Показатели", color="Обозначения", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Показатели погоды'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)