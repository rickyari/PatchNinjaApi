import paramiko

def connect_ssh(server, user, passwd, command):

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username=user, password=passwd)

	stdin, stdout, stderr = ssh.exec_command(command)

	stdin.write(passwd + '\n')
	
	stdin.flush()

	output = stdout.readlines()

	ssh.close()

	return output