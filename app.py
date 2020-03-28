from flask import Flask
from flask_restful import Resource, Api
from record import RecordList, Record

import psycopg2 as pg2

app = Flask(__name__)

api = Api(app)

api.add_resource(Record, '/record/<student_id>')
api.add_resource(RecordList, '/readall')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True