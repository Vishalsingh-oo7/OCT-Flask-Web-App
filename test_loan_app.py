import pytest
from loan_status import app
import json

#make something that mimics the server
@pytest.fixture
def client():
    return app.test_client()

#test home page
def test_hello_ping(client):
    resp= client.get('/')
    assert resp.status_code == 200
    #assert resp.json == {'message':'Hi, Welcome to Loan Status Classification Model!'}

def test_pinger(client):
    resp= client.get('/ping')
    assert resp.json == {'message':'Hi, I am Vishal'}

def test_prediction (client):
    test_data = {
    "Gender": "Male",
    "Married": "No",
    "ApplicantIncome": 500,
    "LoanAmount": 5000,
    "Credit_History": 1.0
    }
    resp = client.post('/predict', json = test_data)
    assert resp.status_code== 200
    assert resp.json == {'Loan_approval_status': 0}
