import os
from datetime import datetime
from flask import Flask, jsonify, Response, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

host = 'localhost' 
port = 5432 
username = 'apitest' 
password = 'apitest' 
database = 'apidb' 

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{username}:{password}@{host}:{port}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class BirthdayModel(db.Model):
    __tablename__ = 'birthday'

    name = db.Column(db.String(), primary_key=True)
    date1 = db.Column(db.Date())

    def __init__(self, name, model, doors):
        self.name = name
        self.date1 = date1

    def __repr__(self):
        return f"<Name {self.name}>"


@app.route('/hello/<name_id>', methods=['GET', 'PUT'])
def handle_name(name_id):
    if name_id.isalpha() == False:
        return {"message": f"Name must only contain letters."}

    name_id = BirthdayModel.query.get_or_404(name_id)


    if request.method == 'GET':
        response = {
            "name": name_id.name,
            "dateOfBirth": name_id.date1,
        }
        curr_time = datetime.now()
        var_date = name_id.date1
        delta1 = datetime(curr_time.year, var_date.month, var_date.day)
        delta2 = datetime(curr_time.year+1, var_date.month, var_date.day)
        days2bd = ((delta1 if delta1 > curr_time else delta2) - curr_time).days + 1
        if days2bd > 0:
            return {"message": f"Hello, {name_id.name}! Your birthday is in {days2bd} day(s)."}
        else: 
            return {"message": f"Hello, {name_id.name}! Happy birthday!"}

    elif request.method == 'PUT':
        curr_time = datetime.today() 
        data = request.get_json()
        var_date = datetime.strptime(data['dateOfBirth'], '%Y-%m-%d')
        if var_date.date() >= curr_time.date():
            return {"message": f"Value must be a date before the today date."}            

        name_id.date1 = data['dateOfBirth']
        db.session.add(name_id)
        db.session.commit()
        return ('', 204)




