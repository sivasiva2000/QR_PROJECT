import qrcode


url = input("Enter the URL to generate QR code: ").strip()
# url = https://leetcode.com/u/sivakandhasami/

file_path = "C:\\GitHub\\QR_Project\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)


img = qr.make_image(fill_color="#3A2A85", back_color="white")
img.save(file_path)

print(f"QR code saved successfully!")
