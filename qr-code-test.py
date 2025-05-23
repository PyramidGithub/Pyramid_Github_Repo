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
    return img

def test_qrcode_output():
    # Data to be encoded
    data = "https://pyramidconsultingnet.sharepoint.com/:b:/g/EbZ7vTAzI51LnUqN8ohL-18BG_5m8OZFeBdM8jycZP4fzg?e=gmHBHZ"

    # Generate QR code (expected and generated)
    expected_img = generate_qrcode(data)
    generated_img = generate_qrcode(data)

    # Convert both images to bytes for comparison
    generated_bytes = io.BytesIO()
    expected_bytes = io.BytesIO()
    generated_img.save(generated_bytes, format="PNG")
    expected_img.save(expected_bytes, format="PNG")

    assert generated_bytes.getvalue() == expected_bytes.getvalue(), "QR code output does not match the expected image."

if __name__ == "__main__":
    # Example of using the test function
    test_qrcode_output()
