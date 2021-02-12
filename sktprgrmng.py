#SOCKET Programming
#how to send mail and all......
#FTP SERVER: File transfer protocol
#index of movie name
#DB vs SERVER
#....server is addition of database and network.in server there is request sended by user in server. in server we can create more than one database.
#connection less and connection orieneted....connection less is like we use bandwidht till they give us a databse path.and connection oriented is like call.
"""
from pyftpdlib.authorizer import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user("Himanshu","1234","F:\Music","elradfmw")
handler=FTPHandler
handler.authorizer = authorizer

server= FTPServer(("192.168.43.94",1237).handler)
server.serve_forever()
"""

#send email

import smtplib
con= smtplib.SMTP("smtp.gmail.com",587)
con.starttls()
con.login("himanshur1998@gmail.com","emmiehrthacker")
msg="Hello Testing"
con.sendmail("himanshur1998@gmail.com","himmupurohit1998@gmail.com",msg)
con.quit()
