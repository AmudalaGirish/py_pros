import qrcode 
from PIL import Image

# add fuctionality for qr_code
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

# add data or link
qr.add_data("https://github.com/AmudalaGirish/py_pros")
qr.make(fit=True)

# image of qr
img = qr.make_image(fill_colour="yellow", back_colour="black")
img.save("github_qr2.png")
