#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from common import connect_ssh as conn
import paramiko
from socket import error, gaierror

app = Flask(__name__)
api = Api(app)

# add arguments 

options = reqparse.RequestParser()
options.add_argument(
    'user', dest='user',
    location='form', required=True,
    help='The username is required',
)
options.add_argument(
	'server', dest='server',
	location='form', required=True,
	help='The server name is required',
)
options.add_argument(
	'passwd', dest='passwd',
	location='form', required=True,
	help='The user password is required',
)

class Reboot(Resource):


	def post(self):

		args = options.parse_args()

		server = args.server
		user = args.user
		passwd = args.passwd
		command = 'fdisk -l'
		
		sudo_command = "sudo -S %s" % command

		try:
			out = conn.connect_ssh(server, user, passwd, sudo_command)
		except paramiko.ssh_exception.AuthenticationException as e:
			out = str(e)
		except gaierror as e:
			out = str(e)
		except error as e:
			out = str(e)

		return {'response' : out}




api.add_resource(Reboot, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
