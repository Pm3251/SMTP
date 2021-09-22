from socket import *
def smtp_client(port=1025, mailserver= '127.0.0.1'):
 msg = "\r\n My message"
 endmsg = "\r\n.\r\n"

 mailserver = ("smtp.nyu.edu", 25)

 # Create socket called clientSocket and establish a TCP connection with mailserver
 clientSocket = socket(AF_INET, SOCK_STREAM)
 clientSocket.connect(mailserver)

 recv = clientSocket.recv(1024)
 print("Message after connection request:" + recv)
 if recv[:3] != '220':
     print('220 reply not received from server.')


 # Send HELO command and print server response.
 heloCommand = 'EHLO Alice\r\n'
 clientSocket.send(heloCommand.encode())
 recv1 = clientSocket.recv(1024)
 print(recv1)
 if recv1[:3] != '250':
     print('250 reply not received from server.')

 # Send MAIL FROM command and print server response.
 MAILFROM = "MAIL FROM: <pm3251@nyu.edu> \r\n"
 clientSocket.send(mailFrom.encode())
 recv2 = clientSocket.recv(1024)
 print("After MAIL FROM command: "+recv2)
 if recv1[:3] != '250':
     print('250 reply not received from server.')

 # Send RCPT TO command and print server response.
 RCPTTO = "RCPT TO: <pm3251@nyu.edu> \r\n"
 clientSocket.send(rcptTo.encode())
 recv3 = clientSocket.recv(1024)
 print("After RCPT TO command: "+recv3)
 if recv1[:3] != '250':
     print('250 reply not received from server.')

 # Send DATA command and print server response.
 DATA = "DATA\r\n"
 clientSocket.send(data.encode())
 recv4 = clientSocket.recv(1024)
 print("After DATA command: "+recv4)
 if recv1[:3] != '250':
     print('250 reply not received from server.')

# Send message data.
 SUBJECT = "Subject: SMTP mail client testing \r\n\r\n"
 clientSocket.send(subject.encode())
 message = input("Enter your message: \r\n")
 clientSocket.send(message.encode())
 clientSocket.send(endmsg.encode())
 recv_msg = clientSocket.recv(1024)
 print("Response after sending message body:"+recv_msg.decode())
 if recv1[:3] != '250':
     print('250 reply not received from server.')

 # Send QUIT command and get server response.
 clientSocket.send("QUIT\r\n".encode())
 message=clientSocket.recv(1024)
 print (message)
 clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

