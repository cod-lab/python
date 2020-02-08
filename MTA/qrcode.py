import pyqrcode as qr
link = "google.com"
qr1 = qr.create(link)
qr1.svg("mylink.svg")
