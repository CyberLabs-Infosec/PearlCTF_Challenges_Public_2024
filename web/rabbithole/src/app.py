from flask import Flask, request, Response, make_response

app = Flask(__name__)


@app.route("/")
def intro():
    response = make_response("<p>You're on your own:)</p>")
    response.set_cookie('userID', 'guest')
    return response


@app.route('/robots.txt')
def robot():
    return open('robots.txt').read()


@app.route('/w0rk_h4rd')
def work():
    return open('w0rk_h4rd/flag.html').read()


strong_method = ['s3cr3t1v3_m3th0d']


@app.route('/hardworking', methods=strong_method)
def flag():
    name = request.cookies.get('userID')
    if name == 'admin':
        return open('reward.txt').read()
    else:
        return "<p>You're not privileged enough ;)</p>"


if __name__ == "__main__":
    app.run("0.0.0.0", 9000)
