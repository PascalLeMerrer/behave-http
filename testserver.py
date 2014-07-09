from flask import Flask, jsonify, make_response, request
import os

app = Flask(__name__)
app.config.from_pyfile('testserver.cfg')
server_name = os.environ.get('SERVER_NAME', None)
if server_name:
    app.config['SERVER_NAME'] = server_name


@app.route('/rest/head', methods=['HEAD'])
def test_head():
    return ''


@app.route('/rest/get', methods=['GET'])
def rest_get():
    return make_response(jsonify({}))


@app.route('/rest/post', methods=['POST'])
def rest_post():
    return make_response(jsonify(request.get_json()), 201)


@app.route('/rest/options', methods=['OPTIONS'])
def rest_options():
    resp = make_response('', 200)
    resp.headers['Allow'] = 'HEAD, GET, OPTIONS'
    return resp


@app.route('/rest/put', methods=['PUT'])
def rest_put():
    return make_response(jsonify(request.get_json()), 200)


@app.route('/rest/patch', methods=['PATCH'])
def rest_patch():
    return make_response(jsonify(request.get_json()), 200)


@app.route('/rest/delete', methods=['DELETE'])
def rest_delete():
    return make_response('', 204)


@app.route('/rest/trace', methods=['TRACE'])
def rest_trace():
    body = '\n'.join(
        ['{0}: {1}'.format(h, v) for h, v in request.headers.items()])
    resp = make_response(body, 200)
    resp.headers['Content-Type'] = 'message/http'
    return resp


@app.route('/rest/get/args', methods=['GET'])
def test_get_args():
    resp = make_response(jsonify(request.args.to_dict(flat=True)))
    return resp


if __name__ == '__main__':
    app.run()
