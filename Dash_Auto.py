import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
app = dash.Dash(__name__)
# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True
# Read the automobiles data into pandas dataframe
auto_data =  pd.read_csv('automobileEDA.csv', 
                            encoding = "ISO-8859-1",
                            )
#Layout Section of Dash
app.layout = html.Div(children=[
    html.H1('Car Automobile Components', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 24}),#TASK 3A
     #outer division starts
     html.Div([
                   # First inner divsion for  adding dropdown helper text for Selected Drive wheels
                    html.Div(
                            [
                                html.H2('Drive Wheels Type:', style={'margin-right': '2em'}),
                                ]#TASK 3B
                     ),
                    
                    #TASK 3C
                     dcc.Dropdown(
                            id='demo-dropdown',
                        options=[
                             {'label': 'Rear Wheel Drive', 'value': 'rwd'},
                            {'label': 'Front Wheel Drive', 'value': 'fwd'},
                             {'label': 'Four Wheel Drive', 'value': '4wd'}
        ],
        value='rwd'
        ),
                    #Second Inner division for adding 2 inner divisions for 2 output graphs 
                    html.Div([
                
                        html.Div([ ], id='plot1'),
                         html.Div([ ], id='plot2')#TASK 3D
                        
                    ], style={'display': 'flex'}),
    ])
    #outer division ends
])
#layout ends
#Place to add @app.callback Decorator
@app.callback([Output(component_id='plot1', component_property='children'),
               Output(component_id='plot2', component_property='children')],
               Input(component_id='demo-dropdown', component_property='value'))#TASK 3E
   
#Place to define the callback function .
def display_selected_drive_charts(value):
   
   
   filtered_df = auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels','body-style'],as_index=False). \
            mean()
        
   filtered_df = filtered_df
   
   fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
   fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')
    
   return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2) ]#TASK 3F
   
   
if __name__ == '__main__':
    app.run_server()