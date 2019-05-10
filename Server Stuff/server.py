import bottle
import json
import storage


@bottle.route('/')
def index():
    return bottle.static_file("index.html", root="")


@bottle.route('/Test.js')
def static():
    return bottle.static_file("Test.js", root="")


@bottle.route('/storage')
def get_movement():
    return json.dumps(storage.getTest())


@bottle.post('/send')
def take_movement():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    storage.addTest(content['action'])
    return json.dumps(storage.getTest())


bottle.run(host="0.0.0.0", port=8080, debug=True)