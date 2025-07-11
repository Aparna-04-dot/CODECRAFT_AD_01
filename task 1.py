<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f3f3f3;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .calculator {
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    #display {
      width: 260px;
      height: 40px;
      font-size: 1.5rem;
      margin-bottom: 10px;
      text-align: right;
      padding: 5px;
    }

    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 60px);
      gap: 10px;
    }

    button {
      padding: 20px;
      font-size: 1.2em;
      border: none;
      background-color: #eee;
      cursor: pointer;
      border-radius: 5px;
      transition: background 0.3s;
    }

    button:hover {
      background-color: #ccc;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <input type="text" id="display" disabled>
    <div class="buttons">
      <button onclick="clearDisplay()">C</button>
      <button onclick="appendValue('/')">/</button>
      <button onclick="appendValue('*')">*</button>
      <button onclick="appendValue('-')">-</button>

      <button onclick="appendValue('7')">7</button>
      <button onclick="appendValue('8')">8</button>
      <button onclick="appendValue('9')">9</button>
      <button onclick="appendValue('+')">+</button>

      <button onclick="appendValue('4')">4</button>
      <button onclick="appendValue('5')">5</button>
      <button onclick="appendValue('6')">6</button>
      <button onclick="calculateResult()">=</button>

      <button onclick="appendValue('1')">1</button>
      <button onclick="appendValue('2')">2</button>
      <button onclick="appendValue('3')">3</button>
      <button onclick="appendValue('0')">0</button>
      <button onclick="appendValue('.')">.</button>
    </div>
  </div>

  <script>
    function appendValue(value) {
      document.getElementById('display').value += value;
    }

    function clearDisplay() {
      document.getElementById('display').value = '';
    }

    function calculateResult() {
      try {
        const result = eval(document.getElementById('display').value);
        document.getElementById('display').value = result;
      } catch {
        document.getElementById('display').value = 'Error';
      }
    }
  </script>
</body>
</html>
