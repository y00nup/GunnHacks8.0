import flask, time
import spotifyhook

app = flask.Flask('API')
genres = None
@app.route("/get", methods=['GET'])
def getsongs():
    mood = flask.request.args.get('mood')
    genre = flask.request.args.get('genre')
    try:
        limit = flask.request.args.get('limit')
    except Exception as e:
        limit = 10
    data = {}
    try:
        data = spotifyhook.getsongs(mood,genre,limit)
    except Exception as e:
        print("Error: "+ str(e))
        data["error"] = str(e)
        data["requested_on"] = time.strftime("%m/%d/%Y %H:%M:%S")
    data = flask.jsonify(data)
    return data


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(401)
def error_401(e):
    return "<h1>Error 401</h1><p>Unauthorized</p>", 401

@app.errorhandler(500)
def error_500(e):
    print(e)
    return "<h1>Internal Server Error</h1><p>{}</p>".format(e), 500

app.run(port=80, host="0.0.0.0")


