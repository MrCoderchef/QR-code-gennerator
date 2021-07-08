import qrcode
import image
qr=qrcode.QRCode(
  version=15,# 15- it is version of qr code, High the no so bigger the code image and complicated pic
  box_size=10,# size of the qr code where code will displayed
  border=5, # it is white part of image -- border in all 4 sides with white color
)

data="My name is alok singh"
# It is the path (after scane it will open)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_colour="white")
img.save("test.png")
