import qrcode

# Data to encode
data = "https://www.google.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("my_qrcode.png")

print("QR code generated and saved as 'my_qrcode.png'")
import qrcode

# Data to encode
data = "https://www.google.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("my_qrcode.png")

print("QR code generated and saved as 'my_qrcode.png'")
