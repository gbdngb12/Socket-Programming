import ftplib

ftp = ftplib.FTP("192.168.166.63")

print(ftp.getwelcome())

ftp.quit()