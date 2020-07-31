import os

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import utils
import speech


app = Flask(__name__)

CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    req_data = request.get_json()
    message = utils.normalize_string((req_data['message']))
    try:
        indices = utils.get_batched_indices(message)
    except KeyError:
        reply = "I did not understand your language!!, check the spelling perhaps"
    else:
        numpy_array = utils.list2numpy(indices)
        reply = speech.generate_sentence()

    resp = jsonify(reply=reply)
    return resp


@app.route('/<path:filepath>')
def ui_components(filepath):
    return send_from_directory('static', filepath)


@app.route('/')
def ui():
    return send_from_directory('static', 'index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='0.0.0.0')