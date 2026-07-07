import qrcode as qr

data = input("Enter text or URL: ")
filename = input("Enter file name (without .png): ")

img = qr.make(data)
img.save(f"{filename}.png")

print(f"QR Code saved as {filename}.png")