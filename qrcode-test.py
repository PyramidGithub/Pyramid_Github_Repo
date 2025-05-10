import qrcode
import pytest
from PIL import Image
import io

def generate_qrcode(data):
    # Create qr code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("qrcode.png")
    print(f"The QR code from {data} is successfully saved to qrcode.png file.")

def test_qrcode_output():
    data = "https://example.com"
    expected_img_path = "expected_qrcode.png"

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    generated_img = qr.make_image()

    # Load expected QR code image
    expected_img = Image.open(expected_img_path)

    # Convert both images to bytes for comparison
    generated_bytes = io.BytesIO()
    expected_bytes = io.BytesIO()
    generated_img.save(generated_bytes, format="PNG")
    expected_img.save(expected_bytes, format="PNG")

    assert generated_bytes.getvalue() == expected_bytes.getvalue(), "QR code output does not match the expected image."

if __name__ == "__main__":
    # Example of using the generate_qrcode function
    generate_qrcode(""https://pyramidconsultingnet.sharepoint.com/:b:/g/EbZ7vTAzI51LnUqN8ohL-18BG_5m8OZFeBdM8jycZP4fzg?e=gmHBHZ"")
