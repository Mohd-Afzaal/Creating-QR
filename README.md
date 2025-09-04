<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QR Code Generator from URLs</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      color: #333;
    }
    h1, h2, h3 {
      color: #2F3961;
    }
    code {
      background: #f4f4f4;
      padding: 2px 5px;
      border-radius: 4px;
    }
    pre {
      background: #f4f4f4;
      padding: 10px;
      border-radius: 6px;
      overflow-x: auto;
    }
    .folder {
      background: #eef;
      padding: 10px;
      border-left: 4px solid #2F3961;
      margin: 10px 0;
    }
    .workflow {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 30px 0;
    }
    .step {
      background: #2F3961;
      color: white;
      padding: 15px 25px;
      margin: 10px;
      border-radius: 8px;
      width: 80%;
      text-align: center;
      position: relative;
    }
    .arrow {
      font-size: 24px;
      margin: 0;
    }
  </style>
</head>
<body>
  <h1>QR Code Generator from URLs</h1>
  <p>
    This Python script generates QR codes from a list of URLs stored in <code>Urls.txt</code>.  
    Each URL is converted into a QR code image and saved in a folder called <code>qr_codes</code>.
  </p>

  <h2>Workflow</h2>
  <div class="workflow">
    <div class="step">1. Load Urls.txt</div>
    <div class="arrow">⬇️</div>
    <div class="step">2. Read each URL & clean whitespace</div>
    <div class="arrow">⬇️</div>
    <div class="step">3. Generate QR code for each URL using <code>segno</code></div>
    <div class="arrow">⬇️</div>
    <div class="step">4. Save QR code images in <code>qr_codes/</code> folder with simple filenames</div>
    <div class="arrow">⬇️</div>
    <div class="step">5. Print confirmation messages in terminal</div>
  </div>

  <h2>Features</h2>
  <ul>
    <li>Bulk-generate QR codes from a text file.</li>
    <li>Automatic folder creation (<code>qr_codes</code>).</li>
    <li>Simple output filenames (domain + counter).</li>
    <li>Custom QR code colors (dark blue background, white QR pattern).</li>
  </ul>

  <h2>Requirements</h2>
  <p>Python 3.7+ and the <a href="https://pypi.org/project/segno/" target="_blank">segno</a> library.</p>
  <pre><code>pip install segno</code></pre>

  <h2>Usage</h2>
  <ol>
    <li>
      Create <strong>Urls.txt</strong> in the same folder as the script.<br>
      Example:
      <pre><code>https://github.com/Neko0kami/Creating-QR
www.linkedin.com/in/mohd-afzaal-545122336
https://mail.google.com/mail/u/0/#inbox</code></pre>
    </li>
    <li>Run the script:
      <pre><code>python script.py</code></pre>
    </li>
    <li>QR codes are saved in <code>qr_codes/</code> folder:
      <div class="folder">
        github.com_1.png<br>
        linkedin.com_1.png<br>
        mail.google.com_1.png
      </div>
    </li>
  </ol>

  <h2>Example</h2>
  <p>Input file:</p>
  <pre><code>https://example.com
https://github.com</code></pre>

  <p>Output folder:</p>
  <div class="folder">
    example.com_1.png<br>
    github.com_1.png
  </div>

  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
