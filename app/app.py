from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.run(debug=True)


