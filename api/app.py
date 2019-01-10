from flask import Flask, jsonify
from flask_cors import CORS #, cross_origin
from modules import sections, readdata

host = open("host.txt","r").read()
port = 5000
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
    return jsonify({
        'data': 'estoque-de-vetores',
        'sections': sections.list,
        'request-example': 'http://' + host +':' + str(port) + '/section-from-list-of-sections'
    })

@app.route("/<string:name>") # http://localhost:5000/section
def get_section(name):
        if ( name in sections.list ):
                return jsonify({'data': readdata.read(name)})
        else:
            sectionsUrls = list(map(lambda item: 'http://' + host +':' + str(port) + '/' + item, sections.list))
            return jsonify({ 
                'message': 'this end point does not exists',
                'try-this-ones': sectionsUrls
            })

if __name__ == "__main__":
    app.run(host=host, port=port)
