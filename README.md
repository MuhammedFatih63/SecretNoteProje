# SecretNotes Application

SecretNotes is a Python application that allows users to create a text file with a given title and content, then encrypt it securely. Users can also decrypt previously encrypted files to access their content. The application uses the `cryptography` library for encryption and `Tkinter` for the user interface.

## Features

- Encrypts user input (file title, content, and password) and saves it as a `.txt` file.
- Allows users to decrypt an encrypted file and view its content.
- Provides a user-friendly interface.

## Requirements

To run this project, you will need the following libraries:

- Python 3.x
- `cryptography`: Used for encryption operations. Install it with the following command:

    ```bash
    pip install cryptography
    ```

- `Pillow`: Used for displaying the icon in the application. Install it with:

    ```bash
    pip install pillow
    ```

## Usage

1. **Save and Encrypt:**
    - Enter the file name in the "Enter File Title" field.
    - Enter the text you want to encrypt in the "Enter File Content" field.
    - Enter a password in the "Enter File Password" field.
    - Click the "Save and Encrypt" button. The file will be encrypted and saved with the provided password.

2. **Decrypt:**
    - Click the "Decrypt" button to select an encrypted file.
    - Enter the password.
    - If the password is correct, the file content will be decrypted and displayed on the screen.

## Functions

### `create_key(password)`
- Generates a key based on the given password.

### `encrypt_file(file_name, data, password)`
- Encrypts the provided text with the given password and saves it as the specified file name.

### `decrypt_file(file_name, password)`
- Decrypts the content of the specified file using the provided password and returns the decrypted text.

### `save_and_encrypt()`
- Collects user input and calls the encryption function to save the encrypted file.

### `select_and_decrypt()`
- Selects an encrypted file and decrypts its content, displaying it on the screen.

### `clear_form()`
- Clears all input fields.
