import pyqrcode 
from pyqrcode import QRCode
from pyqrcode import create
import png


#the string taht the Qr code will represetn 
ulr_string = "https://www.hawkeye.ca/images/blog-lifespan-ducks.webp"
#generating the qr code
qr_code = create(ulr_string)

#save the qr as a png file 
qr_code.png("Attempt.png",scale=10)