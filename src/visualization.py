import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

class Visualization:
    
    def grafico_dispersao(df, y, x, label_y, label_x, hover_data):
        fig = px.scatter(df, x=x, y=y, hover_data=hover_data)
        fig.update_layout(xaxis_title=label_x, yaxis_title=label_y)
        fig.show()
        correlation = df[x].corr(df[y])
        print("Coeficiente de correlação:", correlation)
    
    def grafico_area(df, var_grupo, var_1, var_2, label_1, label_2, x_label, y_label):
        grouped_df = df.groupby(df[var_grupo])[[var_1, var_2]].sum().reset_index()

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=grouped_df[var_grupo], y=grouped_df[var_1],
                                mode='lines',
                                name=label_1,
                                fill='tozeroy'))  # preencher até o eixo y

        fig.add_trace(go.Scatter(x=grouped_df[var_grupo], y=grouped_df[var_2],
                                mode='lines',
                                name=label_2,
                                fill='tozeroy'))  # preencher até o eixo y

        fig.update_layout(xaxis_title=x_label, yaxis_title=y_label)
        fig.show()
    
    def plot_line_chart(df, grupo, var, x_label, y_label):
        data = df.groupby(grupo)[var].mean().reset_index()
        fig = px.line(data, x=grupo, y=var)
        fig.update_layout(xaxis_title=x_label, yaxis_title=y_label)
        fig.update_yaxes(range=[0, data[var].max()*1.1])
        fig.show()
        