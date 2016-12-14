
from flask import Flask, jsonify
from flask import request
from model import db
from model import createdb
from model import Expenses
from sqlalchemy.exc import IntegrityError
import json


# initate flask app
app = Flask(__name__)
# Creating Data Base if not created already
createdb()
# creating table if not already created
db.create_all()
# Base Route for Welcome Page
@app.route('/')
def index():
	return 'Hello from Docker-Compose for Flask & Mysql\n'
#  Route for GET / PUT / DELETE
@app.route('/v1/expenses/<int:expense_id>', methods= ['GET', 'PUT', 'DELETE'])
def expense(expense_id):
    #Creating a object of class Expenses that is the database table reference first_or_404 is for returing 404 
    #if no row is found in the table for the passed value of expense id
    db_obj = Expenses.query.filter_by(id=expense_id).first_or_404()
    if request.method == 'GET':
        return jsonify({'id' : db_obj.id,
                           'name': db_obj.name,
                           'email': db_obj.email,
                           'category': db_obj.category,
                           'description': db_obj.description,
                           'link': db_obj.link,
                           'estimated_costs': db_obj.estimated_costs,
                           'submit_date': db_obj.submit_date,
                           'status': db_obj.status,
                           'decision_date': db_obj.decision_date
                        })

        '''
                # Another Way of returning json object with explicit mime type defined as json
                ret = '{"data": "JSON string example"}'
                resp = Response(response=ret,
                        status=200,
                        mimetype="application/json")
        '''
    if request.method == 'PUT':

           json_obj = request.get_json(force=True)
           db_obj.estimated_costs = json_obj['estimated_costs']
           db.session.commit()
           return jsonify({'status': True}), 202
    if request.method == 'DELETE':
        db.session.delete(db_obj)
        db.session.commit()
        return jsonify({'status': True}), 204

# Route for POST request
@app.route('/v1/expenses', methods=['POST'])

def insert_to_expense():
    try:
        json_obj = request.get_json(force=True)
        db_obj = Expenses(id=json_obj['id'], name=json_obj['name'], email=json_obj['email'], category=json_obj['category'],
                        description=json_obj['description'], link=json_obj['link'],
                        estimated_costs=json_obj['estimated_costs'], submit_date=json_obj['submit_date'],
                        status="Pending", decision_date= "")
        db.session.add(db_obj)
        db.session.flush()
        db.session.commit()

        return jsonify({'id': db_obj.id,
                        'name': db_obj.name,
                        'email': db_obj.email,
                        'category': db_obj.category,
                        'description': db_obj.description,
                        'link': db_obj.link,
                        'estimated_costs': db_obj.estimated_costs,
                        'submit_date': db_obj.submit_date,
                        'status': db_obj.status,
                        'decision_date': db_obj.decision_date
                        }), 201
    except IntegrityError as e:
        db.session.rollback()
        return json.dumps({'status': False}, e)

# run app service in debug mode
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=5002)

