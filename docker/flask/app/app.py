from flask import Flask, render_template, request
from werkzeug.utils import redirect
import mariadb
import json

app = Flask(__name__)

config = {
    'host': 'mariadb',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'sandbox'
}


@app.route('/sandbox')
def hello_world():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form.get('first_name')
    email = request.form.get('email')
    password = request.form.get('password')
    print("ON EST AU BON ENDROIT : {} / {} / {}".format(first_name, email, password))

    try:
        conn = mariadb.connect(**config)
        cur = conn.cursor()
        insert_stmt = (
            "INSERT INTO users (first_name, email, password) "
            "VALUES (%s, %s, %s)"
        )
        data = (first_name, email, password)
        cur.execute(insert_stmt, data)
        cur.execute("SELECT * from users")
    except mariadb.connector.Error as err:
        print("Something went wrong: {}".format(err))
    return "OK"


@app.route('/mariadb')
def index():
    # connection for MariaDB
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    # execute a SQL statement
    cur.execute("select * from users")

    # serialize results into JSON
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results
    return json.dumps(json_data)
