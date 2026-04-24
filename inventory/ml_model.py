import numpy as np
from sklearn.linear_model import LinearRegression

class StockPredictor:
    def __init__(self):
        self.model = LinearRegression()
    
    def train(self, data):
        # Assume data is a list of tuples (past_sales, future_sales)
        X = np.array([d[0] for d in data]).reshape(-1, 1)
        y = np.array([d[1] for d in data])
        self.model.fit(X, y)
    
    def predict(self, current_stock):
        return self.model.predict(np.array([[current_stock]]))[0]

# Mock training
data = [(10, 15), (15, 20), (20, 25)]  # past_sales, future_sales
predictor = StockPredictor()
predictor.train(data)