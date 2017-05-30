#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
from common import connect_ssh as conn

app = Flask(__name__)
api = Api(app)


class Reboot(Resource):


	def post(self):

		server = request.form['server']
		user = request.form['user']
		passwd = request.form['passwd']
		command = 'fdisk -l'
		
		sudo_command = "sudo -S %s" % command

		out = conn.connect_ssh(server, user, passwd, sudo_command)
		
		return {'output' : out}




api.add_resource(Reboot, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)