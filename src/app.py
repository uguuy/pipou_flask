from flask import Flask, jsonify
import json
import yaml
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)

@app.route('/api/events', methods=['GET'])
def get_events():
    data = load_data('src/static_content/events.json')
    return jsonify(data)

@app.route('/api/news', methods=['GET'])
def get_news():
    data = load_data('src/static_content/news.yaml')
    return jsonify(data)

if __name__ == '__main__':
    # Tu peux changer le port ici si besoin (par ex. port=5050)
    app.run(host='0.0.0.0', port=5000)
