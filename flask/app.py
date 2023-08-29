from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    print("app.py running on flask\n")
    app.run(debug=True, port=8080, host="0.0.0.0")