def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
print('250 reply not received from server.')


mailFrom = "MAIL FROM: <example12 (at the rate) xyz(dot)com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command: "+recv2)
if recv1[:3] != '250':
print('250 reply not received from server.')


rcptTo = "RCPT TO: <destination12(at the rate) xyz(dot)com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print("After RCPT TO command: "+recv3)
if recv1[:3] != '250':
print('250 reply not received from server.')


data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
print("After DATA command: "+recv4)
if recv1[:3] != '250':
print('250 reply not received from server.')

message = raw_input("Enter your message: \r\n")

mailMessageEnd='\r\n.\r\n'
clientSocket.send(message + mailMessageEnd)
print(recv1)
if recv1[:3] != '250':
print('250 reply not received from server.')


clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024)
print (message)
clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')