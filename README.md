Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

Explanation

    Import Libraries: We use PIL (Pillow) for image handling and numpy for efficient pixel manipulation.
    Encrypt Image:
        Open the image and convert it to a NumPy array.
        Add the encryption key to each pixel value. Use modulo 256 to ensure the pixel values remain valid (0-255).
        Save the encrypted image.
    Decrypt Image:
        Open the encrypted image and convert it to a NumPy array.
        Subtract the encryption key from each pixel value. Use modulo 256 to handle any potential underflow.
        Save the decrypted image.

Usage

    Replace 'path_to_original_image.jpg' with the path to the image you want to encrypt.
    Replace 'path_to_encrypted_image.jpg' with the path where you want to save the encrypted image.
    Replace 'path_to_decrypted_image.jpg' with the path where you want to save the decrypted image.
    Adjust the key value to whatever integer you prefer as your encryption key.

This simple tool demonstrates basic image encryption and decryption using pixel value manipulation. You can expand it with more complex operations for enhanced security.
