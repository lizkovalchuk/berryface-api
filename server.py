import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Testing Git Pull</h1><p>Testing if I can push from laptop and pull on server</p>"



