import paramiko
from socket import error, gaierror

def connect_ssh(server, user, passwd, command):

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	try:
		ssh.connect(server, username=user, password=passwd)


		stdin, stdout, stderr = ssh.exec_command(command)

		stdin.write(passwd + '\n')
	
		stdin.flush()

		output = stdout.readlines()
		err = stderr.readlines()
		response = {'output': output, 'err': err}
		ssh.close()

		return response

	except paramiko.ssh_exception.AuthenticationException as e:
		response = {'err': str(e)}
		return response

	except gaierror as e:
		response = {'err': str(e)}
		return response

	except error as e:
		response = {'err': str(e)}
		return response