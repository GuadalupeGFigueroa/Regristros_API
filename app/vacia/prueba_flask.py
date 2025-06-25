from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Flask responde correctamente a la ruta raíz"

if __name__ == '__main__':
    app.run(debug=True)