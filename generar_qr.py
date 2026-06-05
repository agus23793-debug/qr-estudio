import qrcode

# REEMPLAZA ESTE LINK POR EL TUYO DE GITHUB PAGES
link_estudio = "https://agus23793-debug.github.io/qr-estudio/"

# Configuración estética del QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link_estudio)
qr.make(fit=True)

# Generar la imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar el archivo en tu computadora
img.save("qr_estudio_contable.png")

print("¡Código QR generado con éxito como 'qr_estudio_contable.png'!")