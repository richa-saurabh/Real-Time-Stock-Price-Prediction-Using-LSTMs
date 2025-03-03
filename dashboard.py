import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import tensorflow as tf
import pandas as pd

# Load CSV and skip the first row to fix column names
df = pd.read_csv("uber_stock_data_fixed.csv", skiprows=1)

# Rename columns correctly
df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

print(df.head())  # Check if the dataframe is correct

df['Date'] = pd.date_range(start="2024-01-01", periods=len(df), freq="D")  # Fake dates
print(df.head())  # Verify the changes

df.sort_values('Date', inplace=True)

# Load your trained LSTM model
model = tf.keras.models.load_model('lstm_model.h5')  # Replace with your model file

# Define a function to predict stock prices
def predict_stock_prices(last_60_days):
    scaled_data = np.array(last_60_days).reshape(1, 60, 1)  # Reshape for LSTM
    predicted_price = model.predict(scaled_data)[0, 0]
    return predicted_price

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Uber Stock Price Prediction Dashboard", style={'textAlign': 'center', 'color': '#333'}),
    
    dcc.Graph(id='stock-price-chart'),
    
    dcc.DatePickerSingle(
        id='date-picker',
        min_date_allowed=df['Date'].min(),
        max_date_allowed=df['Date'].max(),
        date=df['Date'].max(),
        style={'margin': '20px'}
    ),
    
    html.Button('Predict Next Day Price', id='predict-button', n_clicks=0, style={'margin': '10px', 'padding': '10px'}),
    
    html.Div(id='prediction-output', style={'fontSize': '20px', 'margin': '20px'}),
])

# Callback to update stock chart
@app.callback(
    Output('stock-price-chart', 'figure'),
    Input('date-picker', 'date')
)
def update_graph(selected_date):
    selected_date = pd.to_datetime(selected_date)
    
    # Filter data up to selected date
    filtered_df = df[df['Date'] <= selected_date]
    
    # Create figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Close'], 
                             mode='lines', name='Closing Price', line=dict(color='blue')))
    
    fig.update_layout(title='Stock Price Over Time', xaxis_title='Date', yaxis_title='Price',
                      template='plotly_dark', height=500)
    
    return fig

# Callback for prediction
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    Input('date-picker', 'date')
)
def predict_next_price(n_clicks, selected_date):
    if n_clicks > 0:
        selected_date = pd.to_datetime(selected_date)
        
        # Get last 60 days of stock prices
        last_60_days = df[df['Date'] <= selected_date].tail(60)['Close'].values
        
        if len(last_60_days) < 60:
            return "Not enough data for prediction!"
        
        predicted_price = predict_stock_prices(last_60_days)
        return f"Predicted Stock Price for next day: ${predicted_price:.2f}"

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
