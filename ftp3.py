import ftplib

ftp = ftplib.FTP("127.0.0.1")

ftp.login()

target = "file2.txt"
copy = "mydownload.txt"

with open(copy,"wb") as f:
    res = ftp.retrbinary("RETR "+target, f.write)

ftp.quit()