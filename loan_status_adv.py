from flask import Flask, request, jsonify
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load model once (not inside route to save time)
with open("classifier.pkl", "rb") as f:
    clf = pickle.load(f)

# Home route
@app.route("/")
def home():
    return "Loan Approval Predictor API is running! 🚀"

# Health check route
@app.route("/ping", methods=['GET'])
def pinger():
    return {"message": "Everything is working fine!"}

# Prediction route
@app.route("/predict", methods=['POST'])
def prediction():
    try:
        # Get JSON data from request
        loan_req = request.get_json()
        print("Request Data:", loan_req)

        # Encode Gender
        Gender = 0 if loan_req['Gender'] == "Male" else 1

        # Encode Married
        Married = 1 if loan_req['Married'] == "Yes" else 0

        # Convert to numeric (important!)
        Applicant_Income = int(loan_req['ApplicantIncome'])
        Loan_Amount = int(loan_req['LoanAmount'])
        Credit_History = int(loan_req['Credit_History'])

        # Make prediction
        result = clf.predict([[Gender, Married, Applicant_Income, Loan_Amount, Credit_History]])

        # Convert prediction to readable response
        prediction_value = int(result[0])
        status = "Loan Approved ✅" if prediction_value == 1 else "Loan Rejected ❌"

        return jsonify({
            "prediction": prediction_value,
            "status": status
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# Run app
if __name__ == "__main__":
    app.run(debug=True)