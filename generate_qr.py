
import qrcode

# Enter your published website link
website_url = "https://ahraskt.github.io/menu_card/"

# Generate the QR code
qr = qrcode.make(website_url)

# Save the QR code as an image
qr.save("calicut_foods_qr.png")

print("QR code created successfully!")
print("Saved as calicut_foods_qr.png")

