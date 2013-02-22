#!/usr/bin/env python
__author__ = "Dr4rqua"
__copyright__ = "Copyright (c) 2012-2013 Py-Hack developers"
__licence__ = "Revised BSD License"
__version__ = "1.1.0"
"""
Configure
"""
MIN_LENGTH_OF_PASSWORD = 6
MAX_LENGTH_OF_PASSWORD = 12
"""
Import Important modules
"""
import argparse, os, sys, re, hashlib, string, random, threading, time, urllib2
"""
Set some important Values
"""
global COMMAND
global CANCEL
global LOCK
CANCEL = "CANCEL"
COMMAND = "KEEPUP"
LOCK = threading.Lock()

"""
Define Password generator
"""
def passmaker(pass_min_length, pass_max_length):
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	count_chars = 1
	random_password =''
	while count_chars <= random.randint(pass_min_length, pass_max_length):
		random_password = random_password + chars[random.randint(0, len(chars) - 1)]
		count_chars = count_chars + 1
	return random_password

"""
Password Cracking Class
"""
Crack_dict = {}


class break_the_hash(threading.Thread):
    def __init__(self, encrypted_hash, hash_type_of_hash, number):
        threading.Thread.__init__(self)
        self.encrypted_hash = encrypted_hash
        self.number = number + 1
        self.count = 0
        self.hash_type_of_hash = hash_type_of_hash
    def run(self):
        global COMMAND
        global CANCEL
        global LOCK
        Crack_dict[str(self.number)]= self.count
        LOCK.acquire()
        LOCK.release()
        while COMMAND != CANCEL:
            """
            Encodes the random passwords and
            checks if they fit
            """
            self.count += 1
            Crack_dict[str(self.number)]= self.count
            password = passmaker(MIN_LENGTH_OF_PASSWORD, MAX_LENGTH_OF_PASSWORD)
            if args.hash_type.lower() == 'md5':
                gen_hash = hashlib.md5(password).hexdigest()
            elif args.hash_type.lower() == 'sha1':
                gen_hash = hashlib.sha1(password).hexdigest()
            if gen_hash == self.encrypted_hash:
                print "\n[+] Your hashed just got cracked"
                print "[+] Password : "+ password + "\n"
                COMMAND = CANCEL
                break
        LOCK.acquire()
        LOCK.release()

"""
Google Attack
"""
class google_attack():
    def __init__(self):
        google_wordlist = []
        try:
            google_opener = urllib2.build_opener()
            google_opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            page_handle = google_opener.open('http://www.google.com/search?q=%s' % (args.hash))
        except urllib2.URLError as Urle:
            print "[-]Error :"+str(Urle)
            time.sleep(3)
            sys.exit("[-] Exiting...")
        else:
            word_gatherer = re.split(r"\s+", str(page_handle.read()))
            
            for password in word_gatherer:
                if args.hash_type.lower() == 'md5':
                    gen_hash = hashlib.md5(password).hexdigest()
                elif args.hash_type.lower() == 'sha1':
                    gen_hash = hashlib.sha1(password).hexdigest()
                if gen_hash == args.hash:
                    print "[+] Your hashed just got cracked"
                    print "[+] Password : "+ password
                    break
            else:
                print "[-]Hash not found."
            time.sleep(3)
            sys.exit("[-] Exiting...")
            
            
"""
Tries Calculator
"""
def get_attacks():
    sumup = 0
    for p in Crack_dict:
        sumup += Crack_dict[p]
    return sumup

"""
Main Menu
"""

ascii_logo = """ __  __     _   _           _     
 \ \/ /    | | | | __ _ ___| |__  
  \  /_____| |_| |/ _` / __| '_ \ 
  /  \_____|  _  | (_| \__ \ | | |
 /_/\_\    |_| |_|\__,_|___/_| |_|
"""
#print hashlib.md5("aaaa").hexdigest()
#--google --hash 74b87337454200d4d33f80c4663dc5e5 --type md5 

"""
Argument Parsing
"""
if __name__ == '__main__':
                
    parser = argparse.ArgumentParser(
        description=ascii_logo,
        add_help=True,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Examples: %(prog)s --hash a78e19f49cf2dfb019d933a06470ef66 --hash_type md5 --threads 100')

    parser.add_argument('-t', '--hash', dest='hash', help='Add the hash you want to crack')
    parser.add_argument('-d', '--type', dest='hash_type', help='Define if your hash is md5 or sha1')
    parser.add_argument('-n', '--threads', dest='threads_limit', help='Define how many threads you want to use')
    parser.add_argument('-b', '--bruteforce', action="store_true", dest="brute", help='Bruteforce the hash')
    parser.add_argument('-g', '--google', action="store_true", dest="google_search", help='Use google in order to find the hash')
    args = parser.parse_args()
    if args.hash and args.hash_type and args.threads_limit and args.brute:
        if args.hash_type.lower() == 'md5':
            if len(args.hash) != 32:
                sys.exit('[-] Error: "%s" doesn\'t \n    seem to be a valid MD5 hash "32 bit hexadecimal"' % args.hash)
        elif args.hash_type.lower() == 'sha1':
            pass
        else:
            usage()
        print '[*] Hash Cracker is starting ...'
        print '[*] hash_type {Ctrl + C} to stop the cracker'
        thread_check = '[*] Starting threads [%s/%s]' % ("0", args.threads_limit)
        sys.stdout.write(thread_check)
        sys.stdout.flush()
        try:
            for i in range(int(args.threads_limit)):
                break_the_hash(args.hash, args.hash_type, i).start()
                thread_check = '[*] Starting threads [%s/%s]' % (str(i+1), args.threads_limit)
                sys.stdout.write('\b'*len(thread_check))
                sys.stdout.write(thread_check)
                sys.stdout.flush()
        except KeyboardInterrupt:
            print '\n[*] Stopping threads ...'
            COMMAND = CANCEL
            time.sleep(3)
            sys.exit("[-] Exiting...")
        print '\n[*] Threads Started ...'
        attack = 0
        line = "[*] Tries against the hash #%s" %(attack)
        sys.stdout.write(line)
        sys.stdout.flush()
        try:
            while COMMAND != CANCEL:
                attack = get_attacks()
                line = "[*] Tries against the hash #%s" %(attack)
                sys.stdout.write('\b'*len(line))
                sys.stdout.write(line)
                sys.stdout.flush()
                
        except KeyboardInterrupt:
            print '\n[*] Stopping threads ...'
            COMMAND = CANCEL
            time.sleep(3)
            sys.exit("[-] Exiting...")
    elif args.hash and args.hash_type and args.google_search:
        if args.hash_type.lower() == 'md5':
            if len(args.hash) != 32:
                sys.exit('[-] Error: "%s" doesn\'t \n    seem to be a valid MD5 hash "32 bit hexadecimal"' % args.hash)
        elif args.hash_type.lower() == 'sha1':
            pass
        else:
            usage()
        print '[*] Hash Cracker is starting ...'
        google_attack()
    else:
        parser.print_help()
        time.sleep(3)
        sys.exit("[*] Exiting...")
