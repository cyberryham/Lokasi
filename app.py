from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location', methods=['POST'])
def get_location():
    ip_address = request.form.get('ip_address')
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
