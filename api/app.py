from flask import Flask, jsonify
from flask_cors import CORS
from modules import sections, readdata

host = open("host.txt","r").read()
port = 5000
app = Flask(__name__)
cors = CORS(app)
app.config['JSON_AS_ASCII'] = False

# list of "sections" endponints
sectionsUrls = list(map(lambda item: 'http://' + host +':' + str(port) + '/' + item, sections.names()))

@app.route('/')
def home():
    return jsonify({
        '_meta': "home content",
        'content': readdata.read('sections')
    })

@app.route('/valid-sections')
def valid_sections():
    return jsonify({
        '_meta': "valid sections",
        'content': sections.names()
    })


@app.route("/<string:name>") # http://localhost:5000/section
def get_section(name):
        if ( name in sections.names() ):
                return jsonify({
                    '_meta': name + "'s" + ' folders content',
                    'name': name,
                    'content': readdata.read(name)
                })
        else:
            return jsonify({ 
                '_message': 'this endpoint does not exists',
                'endpoints': sectionsUrls
            })

if __name__ == "__main__":
    app.run(host=host, port=port)
