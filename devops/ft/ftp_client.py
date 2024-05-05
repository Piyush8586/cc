from ftplib import FTP

def ftp_client():
    ftp = FTP("127.0.0.1")
    ftp.login(user="user", passwd="password")

    ftp.cwd("/")  

    
    files = ftp.nlst()
    print("Files in the current directory:")
    for file in files:
        print(file)

    
    filename = "uptime.tsv"
    with open(filename, "wb") as file:
        ftp.retrbinary("RETR " + filename, file.write)

    
    # filename = "example.txt"
    # with open(filename, "rb") as file:
    #     ftp.storbinary("STOR " + filename, file)

    ftp.quit()

if __name__ == "__main__":
    ftp_client()