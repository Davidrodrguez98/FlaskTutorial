from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)


