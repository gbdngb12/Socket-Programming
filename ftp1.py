import ftplib

ftp = ftplib.FTP("127.0.0.1")
ftp.login()
print(ftp.getwelcome())

entries = ftp.nlst()
for entry in entries :
    res = ftp.retrbinary("RETR " + entry, open(entry,"wb").write)
    print(res)
#ftp.retrbinary("RETR file1.txt", open('file1.txt', 'wb').write)

#target = "file1.txt"
#copy = "myfile.txt"
#with open(copy, "wb") as f:
#    res = ftp.retrbinary("RETR " + target, f.write)

ftp.quit()