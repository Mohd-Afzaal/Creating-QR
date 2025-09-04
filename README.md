[![QR Code for Repo](output_QR.png)](https://github.com/Neko0kami/Creating-QR)

# QR Code Generator from URLs

This Python script generates QR codes from a list of URLs stored in `Urls.txt`.  
Each URL is converted into a QR code image and saved in a folder called `qr_codes`.

---

## Workflow

1️⃣ **Load `Urls.txt`**  
⬇️  
2️⃣ **Read each URL & clean whitespace**  
⬇️  
3️⃣ **Generate QR code for each URL using `segno`**  
⬇️  
4️⃣ **Save QR code images in `qr_codes/` folder with simple filenames**  
⬇️  
5️⃣ **Print confirmation messages in terminal**

---

## Features

- Bulk-generate QR codes from a text file.  
- Automatic folder creation (`qr_codes`).  
- Simple output filenames (domain + counter).  
- Custom QR code colors (dark blue background, white QR pattern).

---

## Requirements

- Python 3.7+  
- [segno](https://pypi.org/project/segno/) library

Install `segno`:

```bash
pip install segno
````

---

## Usage

1. Create a file named **`Urls.txt`** in the same folder as the script.
   Example content:

```text
https://github.com/Neko0kami/Creating-QR
www.linkedin.com/in/mohd-afzaal-545122336
https://mail.google.com/mail/u/0/#inbox
```

2. Run the script:

```bash
python script.py
```

3. The QR codes will be saved inside the `qr_codes/` folder:

```
qr_codes/github.com_1.png
qr_codes/linkedin.com_1.png
qr_codes/mail.google.com_1.png
```

---

## Example

Input file (`Urls.txt`):

```text
https://example.com
https://github.com
```

Output folder (`qr_codes/`):

```
example.com_1.png
github.com_1.png
```

---

## License

This project is licensed under the [MIT License](LICENSE).

```

---

✅ **Advantages of this version for GitHub:**

- Fully Markdown-compatible, renders nicely in the repo.  
- Workflow steps use **emojis and arrows** for readability.  
- Code blocks are preserved for commands, URLs, and examples.  
- Users can copy-paste commands easily.

---

If you want, I can also **add a small ASCII-style workflow diagram** inside the Markdown to make the flow more visual.  

Do you want me to add that?
```
