import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://aman231217.github.io/Personal-Website--using-CSS-HTML/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("mysite.svg", scale = 8) 