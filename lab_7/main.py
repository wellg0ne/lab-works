from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
students = {}


@app.route('/')
def root():
    return '<pre>Hello World!</pre>'


@app.route('/new_std')
def add():
    args = request.args
    students[args.get('name')] = {'group': args.get('group'), 'marks': args.get('marks').split(',')}
    return redirect(url_for('student', name=args.get('name')))


@app.route('/student/<name>')
def student(name):
    return render_template('student.html', name=name, group=students[name]['group'], marks=students[name]['marks'])
