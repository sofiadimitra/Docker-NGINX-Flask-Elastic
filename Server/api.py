''' Docker + python 3.6.3 and Elasticsearch 6.0.1 '''

from flask import Flask, jsonify
from elasticsearch import Elasticsearch
from datetime import datetime
import os


es_host = os.environ['ELASTICSEARCH_HOST'] # 127.0.0.1
es_port = os.environ['ELASTICSEARCH_PORT'] # 9200

# IF ENV DONT WORK TRY THIS.
# es_host = 'elasticsearch'
# es_port = 9200

print('Elastic host is {}'.format(es_host))
print('Elastic port is {}'.format(es_port))

es = Elasticsearch([{'host': es_host, 'port': es_port}])

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/api')
def api_root():
    ''' This is the default api route '''

    print('Elastic host is {}'.format(es_host))
    print('Elastic port is {}'.format(es_port))

    return jsonify({
        'status': 1,
        'route': 'api',
        'api version': 'v1.0',
        'Elastic host is': es_host,
        'Elastic port is': es_port 
    })

@app.route('/api/users')
def api_users():
    ''' Users api '''

    return jsonify([
        {
            'id': 1,
            'fname': 'User1',
            'created': '17/2/2021'
        },
        {
            'id': 2,
            'fname': 'User2',
            'created': '18/2/2021'
        },
        {
            'id': 3,
            'fname': 'User3',
            'created': '18/2/2021'
        },
    ])



@app.route('/api/info')
def api_info():
    ''' Get the elasticsearch info '''
    return jsonify(es.info())

@app.route('/api/health')
def api_health():
    ''' Get the elasticsearch cluster health '''
    return jsonify(es.cluster.health())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
