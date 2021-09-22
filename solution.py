from socket import *
def smtp_client(port=1025, mailserver= '127.0.0.1'):
 msg = "\r\n Hello, How are you?"
 endmsg = "\r\n.\r\n"

 mailserver = ("smtp.nyu.edu", 25)

 # Create socket called clientSocket and establish a TCP connection with mailserver
 clientSocket = socket(AF_INET, SOCK_STREAM)
 clientSocket.connect(mailserver)
 recv = clientSocket.recv(1025).decode()
 print(recv)
 if recv[:3] != '220':
     print('220 reply not received from server.')


 # Send HELO command and print server response.
 heloCommand = 'EHLO Alice\r\n'
 clientSocket.send(heloCommand.encode())
 recv1 = clientSocket.recv(1025).decode()
 print(recv1)
 if recv1[:3] != '250':
     print('250 reply not received from server.')

 # Send MAIL FROM command and print server response.
 mailfrom = "MAIL FROM: <pm3251@nyu.edu> \r\n"
 clientSocket.send(mailFrom.encode())
 recv2 = clientSocket.recv(1025).decode()
 print(recv2)
 if recv2[:3] != '250':
     print('250 reply not received from server.')

 # Send RCPT TO command and print server response.
 rcpto = "RCPT TO: <pm3251@nyu.edu> \r\n"
 clientSocket.send(rcptTo.encode())
 recv3 = clientSocket.recv(1025).decode()
 print(recv3)
 if recv3[:3] != '250':
     print('250 reply not received from server.')

 # Send DATA command and print server response.
 data = "DATA\r\n"
 clientSocket.send(data.encode())
 recv4 = clientSocket.recv(1025).decode()
 print(recv4)
 if recv4[:3] != '354':
     print('354 reply not received from server.')

# Send message data.
 subject = "Subject: SMTP mail client testing \r\n\r\n"
 clientSocket.send(subject.encode())
 clientSocket.send(message.encode())
 clientSocket.send(endmsg.encode())
 recv5 = clientSocket.recv(1025).decode()
 print(recv5)
 if recv5[:3] != '250':
     print('250 reply not received from server.')

 # Send QUIT command and get server response.
 clientSocket.send("QUIT\r\n".encode())
 recv6 = clientSocket.recv(1025).decode()
 print (recv6)
 if recv6[:3] != '250':
	print('250 reply not received from server.')
 clientSocket.close()


