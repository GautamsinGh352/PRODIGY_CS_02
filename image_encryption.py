from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixel_array = np.array(image)
    
    encrypted_array = (pixel_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)
    
    decrypted_array = (encrypted_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'.")

def main():
    print("Image Encryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
        return
    
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption key (an integer): "))
    
    if choice == 'e':
        encrypt_image(image_path, key)
    else:
        decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
