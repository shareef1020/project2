from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)

my_connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='bomb'
)

my_cursor=my_connection.cursor()

@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/admissiion.html',methods=['GET'])
def admission():
    return render_template('admissiion.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html')


@app.route('/delete',methods=['GET'])
def delete():
    return render_template('delete.html')

@app.route('/register_form',methods=['POST'])
def register_form():
    _id=request.form['id']
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    percentage=request.form['percentage']
    rank=request.form['rank']
    course=request.form['course']
    address=request.form['address']
    query='''
        insert into student
        values(%s,%s,%s,%s,%s,%s,%s,%s);
    '''
    values=(_id,name,email,phone,percentage,rank,course,address)
    
    my_cursor.execute(query,values)
    my_connection.commit()
    return "data inserted"

@app.route('/view',methods=['GET'])
def view():
    query="select * from student"
    my_cursor.execute(query)
    data=my_cursor.fetchall()
    return render_template('view.html', details=data)

@app.route('/update',methods=['Get'])
def update():
    return render_template('update.html')

#hi this is shareef
    
    
app.run()