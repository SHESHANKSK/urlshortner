from enum import unique
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_minify import minify, decorators
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urlshortnerdb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
minify(app=app, html=True, js=True, cssless=True, passive=True)


def generate_uuid_short_del():
    delete_key = str(uuid.uuid4())[:13]
    short_key = delete_key[:8]
    return short_key, delete_key


class UrlShortner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(), nullable=False)
    short_url_id = db.Column(db.String(), nullable=False)
    delete_url_id = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'UrlShortner {self.short_url_id}'


@app.route('/')
@decorators.minify(html=True, js=True, cssless=True)
def index():
    return render_template('index.html')


@app.route('/shorturl', methods=['POST'])
def shorturl():
    long_url = request.form.get('long_url')
    short_url_id, delete_url_id = generate_uuid_short_del()
    url_record = UrlShortner(long_url=long_url,
                             short_url_id=short_url_id, delete_url_id=delete_url_id)
    db.session.add(url_record)
    db.session.commit()
    short_url_id = "http://127.0.0.1:5000/" + short_url_id
    delete_url_id = "http://127.0.0.1:5000/delete/" + delete_url_id
    return render_template('result.html', short_url=short_url_id, delete_url=delete_url_id)


@app.route('/<string:short_url_key>')
@decorators.minify(html=True, js=True, cssless=True)
def short_minify(short_url_key):
    shortner = UrlShortner.query.filter_by(short_url_id=short_url_key).first()
    redirect_link = str(shortner.long_url)
    return redirect(redirect_link)


@app.route('/delete/<string:delete_url_key>', methods=['GET'])
def deleteuser(delete_url_key):
    shortner = UrlShortner.query.filter_by(
        delete_url_id=delete_url_key).first()
    db.session.delete(shortner)
    db.session.commit()
    return redirect("/")


@app.route('/api')
@decorators.minify(html=True, js=True, cssless=True)
def api():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
