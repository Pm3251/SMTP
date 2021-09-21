from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Hello How are you?"
    endmsg = "\r\n.\r\n"
    mailserver = ("smtp.nyu.edu", 25)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    recv = clientSocket.recv(1024)
    print("Message after connection request:" + recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')
    heloCommand = 'EHLO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    mailFrom = "MAIL FROM: <pm3251@nyu.edu> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print("After MAIL FROM command: " + recv2)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    rcptTo = "RCPT TO: <pm3251@nyu.edu> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    print("After RCPT TO command: " + recv3)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    print("After DATA command: " + recv4)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())
    message = raw_input("Enter your message: \r\n")
    clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:" + recv_msg.decode())
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    clientSocket.send("QUIT\r\n".encode())
    message = clientSocket.recv(1024)
    print(message)
    clientSocket.send(endmsg.encode())
    clientSocket.close()


