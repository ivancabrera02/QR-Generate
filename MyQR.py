#GENERATE YOUR QR CODES

import qrcode

img = qrcode.make("https://github.com/ivancabrera02/Manual-para-hackers")
img.save("miqr.jpg")