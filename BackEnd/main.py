# import main Flask class and request object
from flask import Flask, request
from dao.temperaturaDao import TemperaturaDAO

# create the Flask app
app = Flask(__name__)
dao = TemperaturaDAO()

@app.route('/temperatura')
def query_example():
    return dao.findAllTemp()

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)