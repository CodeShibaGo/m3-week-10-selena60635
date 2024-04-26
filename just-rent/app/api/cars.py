from app import db
from app.api import bp
from flask import jsonify
from sqlalchemy import text
from flask import Blueprint,request

@bp.route('/api/cars', methods=['GET'])
def get_cars():
    sql = text('SELECT * FROM cars')
    result = db.session.execute(sql)

    cars_list = [dict(row._mapping) for row in result]

    return jsonify(cars_list)