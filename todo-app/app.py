# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    """ Method to render the index page """
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """ Method to add a new todo item """
    todo = request.form.get('todo')
    if todo:
        todos.append({'id': len(todos), 'text': todo, 'completed': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    """ Method to toggle the completion status of a todo item """
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    """ Method to delete a todo item """
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)