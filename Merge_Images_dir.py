from qrcode import *
import re, sys
import Image

#Prime Number generator part
def isPrime(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None

N = 249 #students
M = 100              
l = list()           
A=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H',
'I','J','K','L','restart']

while len(l) < N:
    l += filter(isPrime, range(M - 100, M)) 
    M += 100                               
Values=list()
j=0
for i in l:	
	if A[j]=='restart':
		A=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','restart']

	Values.append('scan'+str(i+47)+A[j]+'.png')

	j+=1
flag=0
l=0
for k in Values:
	img=Image.open(k)
	Final_img=Image.new('RGB',(1100,800))

	img.thumbnail((110,110))

	for i in xrange(0,1100,100):
		for j in xrange(0,800,100):
			flag+=1
			Final_img.paste(img,(i,j))
			if flag==88:
				Final_img.save('Final image1.png')
			elif flag==176:
				Final_img.save('Final image2.png')
			elif flag==249:
				Final_img.save('Final image2.png')

	
