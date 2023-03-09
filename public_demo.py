from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://bassam:ubility#07@demotest.postgres.database.azure.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma = Marshmallow(app)


class persons(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    address=db.Column(db.String)
    phone=db.Column(db.Integer)

    def __init__(self,name,email,address,phone):
        self.name = name
        self.email=email
        self.address=address
        self.phone=phone

class User(ma.Schema):
     class Meta:
        fields = ("name","email","address","phone")

user_schema = User()
users_schema = User(many=True)



@app.route('/get_users_data',methods=['GET'])
def get_users():
    all_users = persons.query.all()
    data=users_schema.dump(all_users)
    return jsonify(data)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    