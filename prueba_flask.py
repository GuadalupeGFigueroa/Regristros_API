from flask import Flask

app = Flask(__name__)

@app.route('/prueba')
def index():
    return "✅ Esta es la la ruta /prueba"

if __name__ == '__main__':
    app.run(debug=True)