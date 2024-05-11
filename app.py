from flask import Flask, render_template
from mangum import Mangum

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Wrap Flask application with Mangum
handler = Mangum(app)
