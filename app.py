from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/blog_post', methods = ["POST"])
def blog_post():
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()
	if request.content_type == 'application/json':
		post_data = request.get_json()
		title = post_data.get("title")
		author = post_data.get("author")
		body = post_data.get("body")
		cur.execute("INSERT INTO BLOGS VALUES (null,?,?,?)", (title, author, body))
		conn.commit()
		return jsonify("Completed Transaction")
	return home()


@app.route('/view_blogs')
def view_blogs():
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	all_blogs = cur.execute('SELECT * FROM blogs').fetchall()
	return render_template('view.html', data = all_blogs)


@app.route('/return_blogs', methods=["GET"])
def return_blogs():
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	all_blogs = cur.execute('SELECT * FROM blogs').fetchall()
	return jsonify(all_blogs)

@app.route('/return_blog/<id>', methods=["GET"])
def return_single_blog(id):
	conn = sqlite3.connect("data.db")
	cur = conn.cursor()
	one_blog = cur.execute('SELECT * FROM blogs WHERE id = ?', (id,)).fetchall()
	return jsonify(one_blog)

@app.route('/update_blog/<id>', methods=["PUT"])
def blog_update(id):
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()
	if request.content_type == 'application/json':
		post_data = request.get_json()
		title = post_data.get("title")
		author = post_data.get("author")
		body = post_data.get("body")		
		cur.execute("""UPDATE BLOGS SET blog_title = ?, author= ?, body= ? WHERE id = ?""", (title, author, body, id,))
		conn.commit()
		return jsonify("Completed Update")
	return home()

@app.route('/delete/<id>', methods=["DELETE"])
def blog_delete(id):
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()
	if request.content_type == 'application/json':
		post_data = request.get_json()
		cur.execute("""DELETE FROM BLOGS WHERE id = ?""", (id,))
		conn.commit()
		return jsonify("Completed Deletion")
	return home()


if __name__ == '__main__':
	app.debug = True
	app.run()