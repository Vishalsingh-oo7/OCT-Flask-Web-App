from flask import Flask, request,  jsonify
import pickle
import pandas as pd

app = Flask(__name__)

#Reading and saving the model
model_pickle = open("./classifier.pkl", "rb")
clf = pickle.load(model_pickle)

#home page
@app.route("/")
def hello_ping():
    return {'message':'Hi, Welcome to Loan Status Classification Model!'}

#ping page
@app.route("/ping")
def pinger():
    return {'message':'Hi, I am pinging'}


@app.route("/predict", methods=['POST'])
def prediction():
    loan_req = request.get_json()

    # Map categorical variables to numeric
    gender = 0 if loan_req['Gender'] == "Male" else 1
    married = 0 if loan_req['Married'] == "No" else 1

    # Extract numerical values
    app_income = float(loan_req['ApplicantIncome'])
    loan_amt = float(loan_req['LoanAmount'])
    credit_hist = float(loan_req['Credit_History'])

    # Create DataFrame with correct column names
    input_df = pd.DataFrame([{
        'Gender': gender,
        'Married': married,
        'ApplicantIncome': app_income,
        'LoanAmount': loan_amt,
        'Credit_History': credit_hist
    }])

    print("CHECK 1")
    result = clf.predict(input_df)
    print("CHECK 2")

    # Return a proper JSON response

    return jsonify({"Loan_approval_status": int(result[0])})