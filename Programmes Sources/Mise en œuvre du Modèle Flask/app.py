from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from joblib import load
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the pre-trained KNN model
knn_model = load(r'C:\Users\dell\Downloads\projet sma\Programmes Sources\Mise en œuvre du Modèle Flask\model.joblib')

# Define the StandardScaler and MinMaxScaler
ss = StandardScaler()
mms = MinMaxScaler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.json['data']
        
        # Convert data to numpy array
        input_data = np.array(list(data.values())).reshape(1, -1)
        
        # Apply transformations similar to df2
        input_data[:, 2] = ss.fit_transform(input_data[:, 2].reshape(-1, 1))
        for i in range(input_data.shape[1]):
            if i != 2:  # Skip 'health' column
                input_data[:, i] = mms.fit_transform(input_data[:, i].reshape(-1, 1))
        
        # Make prediction
        prediction = knn_model.predict(input_data)
        
        # Return prediction
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=3007)
