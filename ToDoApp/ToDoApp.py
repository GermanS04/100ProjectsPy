from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #everything gets stored in the database test.db
database = SQLAlchemy(app) #initialize database with settings of the app

class ToDo(database.Model):
    id = database.Column(database.Integer, primary_key = True)              #unique id column
    task = database.Column(database.String(200), nullable = False)          #task column with a string of 200 characters and cannot be empty
    date = database.Column(database.DateTime, default = datetime.utcnow)    #date and time column

    def __repr__(self):
        return '<Task %r>' % self.id #put an id to every task we create Task 1, Task 2...
    
    # to create database -> python shell "import from the project database, app", create "app.app_context().push()" and then create database by "database.create_all()"

@app.route("/", methods = ['POST', 'GET'])

def index():
    if request.method == 'POST':
        task_content = request.form['task'] #requesting the input of the HTML and assigning to a variable
        new_task = ToDo(task = task_content)
        try:
            database.session.add(new_task) #add task to the database
            database.session.commit() 
            return redirect('/')  #redirect to route
        except:
            return 'There was an error'
    else:
        tasks = ToDo.query.order_by(ToDo.date).all() #return all the database in order from date they were created
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')

def delete(id):
    task2delete = ToDo.query.get_or_404(id) #try to get content of the id if not gives 404

    try:
        database.session.delete(task2delete)
        database.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the task'
    
@app.route('/update/<int:id>', methods = ['GET', 'POST']) #use methods because we are going to post

def update(id):
    taska = ToDo.query.get_or_404(id)

    if request.method == 'POST':
        taska.task = request.form['task']

        try:
            database.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=taska)

if __name__ == "__main__":
    app.run(debug=True)
