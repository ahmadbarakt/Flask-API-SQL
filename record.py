from flask import Flask,request, jsonify
from flask_restful import Resource, Api, reqparse
import json

import psycopg2 as pg2

class Record(Resource):
	#@app.route('/record',methods=['POST','GET'])
	def get(student_id):
		mydb = pg2.connect(database='Assignt_1_Flask',user='postgres',password='admin')
		mycursor = mydb.cursor()
		sql="""SLECT FROM students_account WHERE student_id='%d' """ % int(student_id)
		mycursor.execute(sql)
		return "Successfully Deleted"

class RecordList(Resource):
	def get(self):
		mydb = pg2.connect(database='Assignt_1_Flask',user='postgres',password='admin')
		mycursor = mydb.cursor()

		sql="SELECT * FROM students_account"
		mycursor.execute(sql)
		myresult = mycursor.fetchall()

		row_headers=[x[0] for x in mycursor.description]
		json_data=[]
		for result in myresult:
			json_data.append(dict(zip(row_headers,result)))
		mydb.close()

		result = {'data': json_data}

		return jsonify(result)	