!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>QR Code Scanner</title>
  <script src="https://unpkg.com/html5-qrcode" type="text/javascript"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f9f9f9;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
    }

    h1 {
      color: #333;
    }

    #reader {
      width: 300px;
      margin: 20px 0;
    }

    #result {
      background: #fff;
      padding: 10px;
      border: 1px solid #ccc;
      width: 300px;
      word-wrap: break-word;
    }

    #openLink {
      margin-top: 10px;
      display: none;
    }

    button {
      padding: 10px 20px;
      background: #007bff;
      border: none;
      color: white;
      border-radius: 5px;
      cursor: pointer;
    }

    button:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>

  <h1>QR Code Scanner</h1>
  <div id="reader"></div>
  <div id="result">Scanned data will appear here</div>
  <a id="openLink" href="#" target="_blank"><button>Open Link</button></a>

  <script>
    function isValidUrl(string) {
      try {
        new URL(string);
        return true;
      } catch (_) {
        return false;
      }
    }

    const resultElement = document.getElementById('result');
    const openLink = document.getElementById('openLink');

    function onScanSuccess(decodedText, decodedResult) {
      // Show result
      resultElement.textContent = decodedText;

      // If it's a valid URL, show the "Open Link" button
      if (isValidUrl(decodedText)) {
        openLink.href = decodedText;
        openLink.style.display = 'inline-block';
      } else {
        openLink.style.display = 'none';
      }

      // Optional: stop scanning after first scan
      html5QrcodeScanner.clear();
    }

    const html5QrcodeScanner = new Html5QrcodeScanner(
      "reader", { fps: 10, qrbox: 250 }
    );
    html5QrcodeScanner.render(onScanSuccess);
  </script>
</body>
</html>
