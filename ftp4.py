import ftplib


ftp = ftplib.FTP("127.0.0.1")
ftp.login()

entries = ftp.nlst()

for entry in entries :
    f = open(entry, "w")
    res = ftp.retrbinary("RETR "+ entry, f.write("This is file download!!"))
    print(res)
    f.close()

ftp.quit()