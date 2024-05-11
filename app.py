from flask import Flask, render_template
from aws_lambda_wsgi import adapter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# AWS Lambda handler
def lambda_handler(event, context):
    return adapter.handle_request(app, event, context)
