from flask import Flask, render_template
app = Flask('__name__')

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect



import os, datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort



project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Posts(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
   title = db.Column(db.String(80), nullable=False)
   content = db.Column(db.String(200), nullable=False)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)


@app.route('/figura_32')
def figura_32():
    return render_template('figura_32.html')

@app.route('/figura_30')
def figura_30():
    return render_template('index.html')

@app.route('/figura_31')
def figura_31():
    return render_template('figura_31.html')

@app.route('/figura_33')
def figura_33():
    return render_template('figura_33.html')

@app.route('/figura_35')
def figura_35():
    return render_template('figura_35.html')

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)



@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

