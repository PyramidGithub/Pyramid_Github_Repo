# Pyramid_Github_Repo - Tested Python Code Snippets

## QR-Code 

```{python}

import qrcode

# Data to be encoded
data = "https://pyramidconsultingnet.sharepoint.com/:b:/g/EbZ7vTAzI51LnUqN8ohL-18BG_5m8OZFeBdM8jycZP4fzg?e=gmHBHZ"

# Create qr code instance
qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save the QR code as "qrcode.png"
img.save("qrcode.png")

# Print a success message
print(f"The QR code from {data} is successfully saved to qrcode.png file.")

```
### Result-See the Repo for Test Workflow Code

![image](https://github.com/user-attachments/assets/d423e489-4e68-426e-a9fd-76df834f8ad2)
