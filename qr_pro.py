import qrcode as qr

# Generate qr image
img = qr.make("https://github.com/AmudalaGirish/py_pros")

# save this image
img.save("github_qr.png")



