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


@app.route('/api')
@decorators.minify(html=True, js=True, cssless=True)
def api():
    return render_template('index.html')


@app.route('/result')
@decorators.minify(html=True, js=True, cssless=True)
def result():
    short_url_id = "http://127.0.0.1:5000/"
    delete_url_id = "http://127.0.0.1:5000/"
    return render_template('result.html', short_url=short_url_id, delete_url=delete_url_id)


@app.route('/result')
@decorators.minify(html=True, js=True, cssless=True)
def short_url():
    short_url_id = "http://127.0.0.1:5000/"
    delete_url_id = "http://127.0.0.1:5000/"
    return render_template('result.html', short_url=short_url_id, delete_url=delete_url_id)


@app.route('/shorturl', methods=['POST'])
def shorturl():
    long_url = request.form.get('long_url')
    short_url_id, delete_url_id = generate_uuid_short_del()
    url_record = UrlShortner(long_url=long_url,
                             short_url_id=short_url_id, delete_url_id=delete_url_id)
    db.session.add(url_record)
    db.session.commit()
    short_url_id = "http://127.0.0.1:5000/" + short_url_id
    delete_url_id = "http://127.0.0.1:5000/" + delete_url_id
    return render_template('result.html', short_url=short_url_id, delete_url=delete_url_id)


# @app.route('/delete/<int:id>', methods=['GET'])
# def deleteuser(id):
#     recipient = Recipient.query.filter_by(id=id).first()
#     db.session.delete(recipient)
#     db.session.commit()
#     return redirect("/contacts")
if __name__ == '__main__':
    app.run(debug=True)
