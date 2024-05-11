from flask import Flask, render_template
from mangum import Mangum

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Create a Mangum handler instance
handler = Mangum(app)

if __name__ == '__main__':
    app.run(debug=False)
