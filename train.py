# -*- coding: utf-8 -*-

dict ={}
words=[]
text = open('HSWN_WN.txt', 'r').read()    
sense = text.split('\n')


for line in sense:
#	print line
	if line != '[Decode error - output not utf-8]':
		# temp = line.split()
		try:
			allwords = line.split()[4]
			allwords = allwords.split(',')
		#	pass
		except Exception, e:
			print 'hello'
			for word in allwords:
				try:
					#pass
			 		dict[word]['pos'] = line.split()[2]
			 		dict[word]['neg'] = line.split()[3]
				except Exception, e:
					print 'hello2'
		#print allwords
for key,value in dict.items():
	print key,value['pos'],value['neg'] 
	


    # print words.decode('utf-8')
