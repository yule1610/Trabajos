import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("Yuleisi Montero")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())