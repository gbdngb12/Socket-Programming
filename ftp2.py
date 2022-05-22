import ftplib

ftp = ftplib.FTP("127.0.0.1")
ftp.login()


data = "download.txt"

ftp.cwd("pub/")

lists = []
ftp.dir(lists.append)
print("put before")
for line in lists :
    print(line)

res = ftp.storbinary("STOR down2.txt", open(data,"rb"))
print(res)

print("put after")
lists = []
ftp.dir(lists.append)
for line in lists:
    print(line)


ftp.quit()