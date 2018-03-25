from flask import Flask, jsonify, redirect, render_template, request, url_for, Response
from main import App

app = Flask(__name__)
app2 = App()

@app.route('/sw')
def sw():
    sw_file = open(file='static/service-worker.js',mode='r')
    return Response(response=sw_file,mimetype="text/javascript")


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect("http://127.0.0.1:5000")


@app.errorhandler(403)
def forbidden(e):
    return redirect("http://127.0.0.1:5000")


@app.errorhandler(410)
def gone(e):
    return redirect("http://127.0.0.1:5000")


@app.errorhandler(500)
def internal_error(e):
    return redirect("http://127.0.0.1:5000")

@app.route('/', methods = ["POST"])
def form():
    form_user = request.form
    print(form_user)
    user_word = request.form['word']
    user_count = request.form['count']
    tweets_sentiment = app2.get_tweet_sentiment(user_word,user_count)
    return render_template('response.html',tweets_sentiment= tweets_sentiment)

if __name__ == '__main__':
    app.run()
