from qrcode import *
import re, sys
import Image

#Prime Number generator part
def isPrime(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None

N = 249 #students
M = 100              
l = list()           
A=['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L']

while len(l) < N:
    l += filter(isPrime, range(M - 100, M)) 
    M += 100                               
j=0
for i in l:
#QRcode Generator part
	qr = QRCode(
	    version=1,
	    error_correction=constants.ERROR_CORRECT_L,
	    box_size=10,
	)	
	qr.add_data(str(i+47)+'#'+A[j])
	qr.make(fit=True)
	
	img = qr.make_image()

	#file_name=raw_input("Enter the file name:")
	file_name='scan'+str(i+47)+A[j]+'.png'
	
	j=j+1
	
	img_file=open(file_name,'w+')
	img.save(img_file,'png')
	img_file.close()

