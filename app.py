import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd

# Load Data
df = pd.read_csv("uber_stock_data.csv")
df["Date"] = pd.to_datetime(df["Date"])  # Ensure Date is in datetime format

# Colors and Theme Settings
dark_background = "#121212"
card_background = "#1E1E1E"
text_color = "#E0E0E0"
primary_color = "#FF4081"

# Dash App Initialization
app = dash.Dash(__name__)

app.layout = html.Div(
    style={"backgroundColor": dark_background, "color": text_color, "padding": "20px"},
    children=[
        html.H1("Stock Price Dashboard", style={"textAlign": "center", "color": primary_color}),

        # Dropdown for Selecting Stock Feature (only for the first plot)
        dcc.Dropdown(
            id="price-type",
            options=[
                {"label": "Close Price", "value": "Close"},
                {"label": "Open Price", "value": "Open"},
                {"label": "High Price", "value": "High"},
                {"label": "Low Price", "value": "Low"}
            ],
            value="Close",
            style={"width": "50%", "margin": "auto", "color": "black"},
        ),

        # Stock Line Chart (Dynamic)
        dcc.Graph(id="stock-chart"),

        # Candlestick Chart (Static)
        dcc.Graph(
            id="candlestick-chart",
            figure={
                "data": [
                    go.Candlestick(
                        x=df["Date"],
                        open=df["Open"],
                        high=df["High"],
                        low=df["Low"],
                        close=df["Close"],
                        increasing=dict(line=dict(color="lime")),
                        decreasing=dict(line=dict(color="red")),
                    )
                ],
                "layout": go.Layout(
                    title="Candlestick Chart",
                    paper_bgcolor=card_background,
                    plot_bgcolor=card_background,
                    font=dict(color=text_color),
                    xaxis_rangeslider_visible=False,
                ),
            },
        ),

        # Trading Volume Bar Chart (Static)
        dcc.Graph(
            id="volume-chart",
            figure={
                "data": [
                    go.Bar(
                        x=df["Date"],
                        y=df["Volume"],
                        marker=dict(color="skyblue"),
                    )
                ],
                "layout": go.Layout(
                    title="Trading Volume",
                    paper_bgcolor=card_background,
                    plot_bgcolor=card_background,
                    font=dict(color=text_color),
                ),
            },
        ),
    ],
)

# Callback for updating only the stock line chart
@app.callback(
    Output("stock-chart", "figure"),
    Input("price-type", "value"),
)
def update_stock_chart(selected_price):
    figure = {
        "data": [
            go.Scatter(
                x=df["Date"],
                y=df[selected_price],
                mode="lines",
                line=dict(width=2, color=primary_color),
                name=selected_price,
            )
        ],
        "layout": go.Layout(
            title=f"{selected_price} Stock Price",
            paper_bgcolor=card_background,
            plot_bgcolor=card_background,
            font=dict(color=text_color),
            xaxis_title="Date",
            yaxis_title="Stock Price",
        ),
    }
    return figure


# Run Server
if __name__ == "__main__":
    app.run_server(debug=True)
