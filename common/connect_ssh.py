import paramiko

def connect_ssh(server, user, passwd, command):

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username=user, password=passwd)

	sudo_command = "sudo -S %s" % command

	stdin, stdout, stderr = ssh.exec_command(sudo_command)

	stdin.write(passwd + '\n')
	#stdin.flush()

	#print 'This is output =',stdout.readlines()
	#print 'This is error =',stderr.readlines()

	output = stdout.readlines()

	ssh.close()

	return output