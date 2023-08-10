# from flask import Flask, request, jsonify
# import pickle
#
# app = Flask(__name__)
#
# # Load the trained model
# model = pickle.load(open('predict_diseases.pkl', 'rb'))
#
#
# @app.route('/predict', methods=['POST'])
# def predict():
#     Temperature = float(request.json['Temperature'])
#     pH = float(request.json['pH'])
#     turbidity = float(request.json['Turbidity (NTU)'])
#     Hour = int(request.json['Hour'])
#     Minute = int(request.json['Minute'])
#     Day = int(request.json['Day'])
#     Month = int(request.json['Month'])
#     Year = int(request.json['Year'])
#
#     # Make a prediction using the loaded model
#     prediction = model.predict([[Temperature, pH, turbidity, Hour, Minute, Day, Month, Year]])
#
#     # Convert the prediction to an integer and return it as a JSON response
#     disease = prediction.tolist()
#     print(disease)
#     return jsonify(disease=disease), 200
#
#
# if __name__ == '__main__':
#     app.run()
#
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('predict_diseases.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify(error="Invalid JSON data"), 400

        Temperature = float(data.get('Temperature'))
        pH = float(data.get('pH'))
        turbidity = float(data.get('Turbidity (NTU)'))
        Hour = int(data.get('Hour'))
        Minute = int(data.get('Minute'))
        Day = int(data.get('Day'))
        Month = int(data.get('Month'))
        Year = int(data.get('Year'))

        # Make a prediction using the loaded model
        prediction = model.predict([[Temperature, pH, turbidity, Hour, Minute, Day, Month, Year]])

        # Convert the prediction to an integer and return it as a JSON response
        disease = prediction.tolist()
        return jsonify(disease=disease), 200

    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run()
