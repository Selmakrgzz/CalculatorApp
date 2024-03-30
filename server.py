from flask import Flask, render_template, request, jsonify
from calculate import calculate
from waitress import serve

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_route():
    equation = request.json.get('equation')
    result = calculate(equation)
    return jsonify({ 'result': result })

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)