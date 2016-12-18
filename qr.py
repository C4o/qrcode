import qrcode
from sys import argv
a = argv[1]
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
)
qr.add_data(a)
qr.make(fit=True)
img = qr.make_image()
img.save("caokefan.png")
