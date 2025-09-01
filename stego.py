from PIL import Image
def encode_image(image_path, output_path, secret_text):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0
    secret_text += "###"
    binary_secret = ''.join([format(ord(i), "08b") for i in secret_text])

    for row in range(height):
        for col in range(width):
            if index < len(binary_secret):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_secret[index])
                encoded.putpixel((col, row), (r, g, b))
                index += 1
            else:
                break
        else:
            continue
        break

    encoded.save(output_path)
    print("\n✅ Message successfully hidden inside:", output_path)

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""
    
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for c in chars:
        message += chr(int(c, 2))
        if message.endswith("###"):
            break
    return message[:-3] 


# Main Program
if __name__ == "__main__":
    print("🔒 Image Steganography Tool (Text in Image)\n")

    # Ask user for inputs
    input_image = input("Enter the name of the image (e.g., input.png): ").strip()
    secret_message = input("Enter the secret message: ")
    output_image = input("Enter the output image name (e.g., encoded.png): ").strip()

    # If user didn’t add extension, force .png
    if not (output_image.lower().endswith(".png") or output_image.lower().endswith(".jpg")):
        output_image += ".png"

    # Encode
    encode_image(input_image, output_image, secret_message)

    # Decode
    print("\n🔍 Decoding from output image...")
    hidden_msg = decode_image(output_image)
    print("📩 Hidden message extracted:", hidden_msg)
