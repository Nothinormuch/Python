from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def getDBConnection():
    conn = sqlite3.connect('passwords.db')
    #conn.row_factory = sqlite3.Row
    return conn

def initializeDB(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE passwords(id int, service varchar(50), username varchar(30), email varchar(30), password varchar(50));")

def testDB(conn):
    cur = conn.cursor()
    cur.execute("PRAGMA table_info('passwords');")
    print(cur.fetchall())


testDB(getDBConnection())