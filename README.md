# Real-Time Stock Price Prediction Using LSTMs

## 📌 Overview
This project implements a real-time stock price prediction system using **Long Short-Term Memory (LSTM) networks**. The model leverages **historical stock data** and integrates **live stock market data** using the **Alpha Vantage API** to provide accurate forecasts.

## 🚀 Features
- **Real-Time Stock Price Prediction** using LSTM-based time-series forecasting.
- **Live Data Integration** from the Alpha Vantage API.
- **Flask Web App** to interact with the prediction model.
- **Automated Model Retraining** using MLOps.
- **Data Visualization** with Matplotlib and Seaborn.

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Libraries:** TensorFlow, Keras, Pandas, NumPy, Matplotlib, Seaborn
- **Web Framework:** Flask
- **API:** Alpha Vantage
- **Deployment:** Flask Server

## 📂 Project Structure
```
📁 Stock-Price_Prediction
│── 📜 app.py                 # Flask API for prediction
│── 📜 dashboard.py           # Dashboard for data visualization
│── 📜 lstm_model.h5          # Trained LSTM model
│── 📜 uber_stock_data.csv     # Stock data for training
│── 📜 requirements.txt       # Required Python packages
│── 📜 README.md              # Project documentation
```

## 📖 How to Run
1. **Clone the Repository**
   ```sh
   git clone https://github.com/richa-saurabh/Real-Time-Stock-Price-Prediction-Using-LSTMs.git
   cd Real-Time-Stock-Price-Prediction-Using-LSTMs
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Flask Server**
   ```sh
   python app.py
   ```

4. **Access the Web App**
   Open your browser and visit: `http://127.0.0.1:5000/`

## 📊 Results
The model effectively predicts stock price trends using past stock data, providing real-time visualizations and forecasts. Sample predictions can be visualized in the Flask dashboard.

## 📝 Future Enhancements
- Improve model accuracy with hyperparameter tuning.
- Deploy the model on cloud platforms like AWS/GCP.
- Enhance UI with interactive stock analysis features.
---
💡 *If you found this project useful, give it a ⭐ on GitHub!*
