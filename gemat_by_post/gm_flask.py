from flask import Flask, request
from flask_cors import CORS, cross_origin
from gemat import *
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST'])
@cross_origin()
def index():
    name_from_ng = request.form.get('my_name')
    print(name_from_ng)
    logging.warning(name_from_ng)
    name = Output(name_from_ng).get_name()

    data = {'success': True, 'answer from Flask': name * 3}
    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
