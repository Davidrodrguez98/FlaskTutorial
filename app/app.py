from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ucasalud'

connection = MySQL(app)

@app.before_request
def before_request():
    print("Before Request")

@app.after_request
def after_request(response):
    print("After Request")
    return response

@app.route('/')
def index():
    # return "<h1>weee</h1>"
    courses = ['PHP', 'Django', 'Python', 'Flask', 'Java']
    data = {
        'title': 'Index',
        'welcome': 'Hi!',
        'courses': courses,
        'n_courses': len(courses)
    }
    return render_template('index.html', data=data)

@app.route('/user/<name>/<int:age>')
def user(name, age):
    data = {
        'title': 'User',
        'name': name,
        'age': age
    }
    return render_template('user.html', data=data)

def query_string():
    # http://127.0.0.1:5000/query_string?Param1=David
    print(request)
    print(request.args)
    print(request.args.get('Param1'))
    return "Ok"

@app.route('/users')
def list_players():
    data = {}
    try:
        db = connection.connection.cursor()
        sql = "SELECT name, dtype FROM users"
        db.execute(sql)
        users = db.fetchall()
        # print(users)
        data['users'] = users
        data['message'] = 'Success'
    except Exception as ex:
        data['message'] = 'Error'
    return jsonify(data)

def pageNotFound(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pageNotFound)
    app.run(debug=True)


