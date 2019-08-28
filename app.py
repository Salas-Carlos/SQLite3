from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


def users():
  t=[]
  resultado= db.engine.execute('select * from users;')
  for row in resultado:
    t.append(row)
  

  return t

@app.route('/')
def inicio():
 
  return render_template('lista.html')

@app.route('/users/list')
def usersJ():
 
  lista=users()
  return render_template('index.html',lista=lista)

@app.route('/api/v1/users')
def usersJson():
  datos=[]
  lista=users()

  for i in range(len(lista)):
    datos.append({'Firstname':lista[i][0],'Lastname':lista[i][1],'Username':lista[i][2],'Email':lista[i][3],'Password':lista[i][4]})
  return jsonify(datos)
 
app.run(debug=True,  host='0.0.0.0', port=80)
