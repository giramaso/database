from flask import Flask, request, jsonify
import sqlite3

conn = sqlite3.connect("data.db")

conn.execute('''CREATE TABLE BLOGS
			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
			BLOG_TITLE	TEXT NOT NULL,
			AUTHOR TEXT NOT NULL,
			BODY TEXT NOT NULL);''')
print("Created table successfully")

conn.close()