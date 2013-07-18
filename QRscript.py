from qrcode import *
qr = QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=10,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image()

file_name=raw_input("Enter the file name:")
file_name=file_name+'.png'

img_file=open(file_name,'w+')

img.save(img_file,'png')
img_file.close()
