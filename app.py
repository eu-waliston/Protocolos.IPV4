from flask import Flask, jsonify, render_template
from modules import trabalho_1
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/origem/data')
@cross_origin()
def get_top_origem():
    return jsonify(trabalho_1.top_10_origem)


@app.route('/api/destino/data')
@cross_origin()
def get_top_destino():
    return jsonify(trabalho_1.top_10_destino)


if __name__ == '__main__':
    app.run()
