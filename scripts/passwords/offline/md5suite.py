#!usr/bin/python
# -*- coding: cp1253 -*-
#Coded by kwnos100
import hashlib,sys,os
os.system(['clear','cls'][os.name == 'nt'])
print '''\
            <==============================>
            / |      MD5 Hash Suite      | \\
            \\ |    Coded by kwnos100     | /
            <==============================>
'''
try:
   hash_touse= "decrypt"
   whatodo= "a78e19f49cf2dfb019d933a06470ef66"
except:
   print '�����: %s [mode] [word/hash]' % (sys.argv[0])
   print '[mode]\t\t= encrypt � decrypt'
   print '[word/hash]\t= ��� ����(��� encrypt) � �� md5 hash(��� decrypt)'
   sys.exit()
if hash_touse== 'encrypt':
   str = '\t'
   print '\t\tEncrypting: %s' % whatodo
   for x in range(0, ((len(whatodo) * 2) + 20)):
      str += '='
   print str
   print 'Original Word:\t%s' % whatodo
   print 'Word Hash:\t%s' % hashlib.md5(whatodo).hexdigest()
   sys.exit()
if hash_touse!= 'decrypt':
   print '�����: %s [mode] [word/hash]' % (sys.argv[0])
   print '[mode]\t\t= encrypt � decrypt'
   print '[word/hash]\t= ��� ����(��� encrypt) � �� md5 hash(��� decrypt)'
   sys.exit()
print '�������� �� mode ��� wordlist:'
print '1. ���� wordlist �� ���� ��������'
print '2. ���� wordlist �� �������� ��������'
print '3. ���� wordlist �� ���� ��� �������� ��������'
print '4. Wordlist �� �������� ��� ���� ��������'
print '5. Wordlist �� �������� ��� �������� ��������'
print '6. Wordlist �� ��������, �������� ��� ���� ��������'
print '7. Wordlist �� ��������, ���� �������� ��� �������'
print '8. Wordlist �� ��������, �������� �������� ��� �������'
print '9. Wordlist �� ��������, �������� & ���� �������� ��� �������'
mode = raw_input('-> ')
if mode == '1':
   list = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
elif mode == '2':
   list = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
elif mode == '3':
   list = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
elif mode == '4':
   list = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
elif mode == '5':
   list = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
elif mode == '6':
   list = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
elif mode ==  '7':
   list = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ',', '<', '>', '.', '/',\
		'?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|', '=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
elif mode == '8':
   list = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ',', '<', '>', '.', '/',\
		'?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|', '=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
elif mode == '9':
   list = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', \
		'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', \
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ',', '<', '>', '.', '/',\
		'?', '\'', '"', ';', ':', ']', '}', '[', '{', '\\', '|', '=', '+', '-', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
print '������ ��������...'
for c1 in list:
	for c2 in list:
		for c3 in list:
			for c4 in list:
				for c5 in list:
					for c6 in list:
						for c7 in list:
							for c8 in list:
								for c9 in list:
									for c10 in list:
									   for c11 in list:
									      for c12 in list:
									         for c13 in list:
									            for c14 in list:
									               for c15 in list:
									                  for c16 in list:
									                     for c17 in list:
									                        for c18 in list:
									                           for c19 in list:
									                              for c20 in list:
                                                                                                         #print(str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6) + str(c7) + str(c8) + str(c9) + str(c10) + str(c11) + str(c12) + str(c13) + str(c14) + str(c15) + str(c16) + str(c17) + str(c18) + str(c19) + str(c20))
									                                    
									                                 if hashlib.md5(str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6) + str(c7) + str(c8) + str(c9) + str(c10) + str(c11) + str(c12) + str(c13) + str(c14) + str(c15) + str(c16) + str(c17) + str(c18) + str(c19) + str(c20)).hexdigest() == whatodo:
									                                    print '[+] � ������� �������!'
									                                    print 'MD5 Hash: ' + whatodo
									                                    print '������������������� �������: ' + str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6) + str(c7) + str(c8) + str(c9) + str(c10) + str(c11) + str(c12) + str(c13) + str(c14) + str(c15) + str(c16) + str(c17) + str(c18) + str(c19) + str(c20)
									                                    raw_input("Type anything to exit")
									                                    exit()

