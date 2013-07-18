import Image

img=Image.open("scan1.png")
new_img=Image.new('RGB',(1100,800))

img.thumbnail((110,110))

for i in xrange(0,1100,100):
	for j in xrange(0,800,100):
		new_img.paste(img,(i,j))
		new_img.save('new scan1.png')
new_img.show()

