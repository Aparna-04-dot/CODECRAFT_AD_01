<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Stopwatch App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f5f5f5;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .stopwatch {
      font-size: 3rem;
      margin-bottom: 20px;
    }

    .buttons button {
      font-size: 1rem;
      padding: 10px 20px;
      margin: 0 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    .buttons button:hover {
      opacity: 0.9;
    }

    #start { background-color: #4CAF50; color: white; }
    #pause { background-color: #f0ad4e; color: white; }
    #reset { background-color: #d9534f; color: white; }
  </style>
</head>
<body>

  <div class="stopwatch" id="display">00:00:000</div>
  <div class="buttons">
    <button id="start">Start</button>
    <button id="pause">Pause</button>
    <button id="reset">Reset</button>
  </div>

  <script>
    let startTime = 0;
    let elapsedTime = 0;
    let timerInterval;
    let running = false;

    const display = document.getElementById("display");

    function updateTime() {
      const time = Date.now() - startTime + elapsedTime;
      const minutes = Math.floor(time / 60000);
      const seconds = Math.floor((time % 60000) / 1000);
      const milliseconds = time % 1000;

      display.textContent = 
        `${String(minutes).padStart(2, '0')}:` +
        `${String(seconds).padStart(2, '0')}:` +
        `${String(milliseconds).padStart(3, '0')}`;
    }

    document.getElementById("start").addEventListener("click", () => {
      if (!running) {
        running = true;
        startTime = Date.now();
        timerInterval = setInterval(updateTime, 10);
      }
    });

    document.getElementById("pause").addEventListener("click", () => {
      if (running) {
        running = false;
        elapsedTime += Date.now() - startTime;
        clearInterval(timerInterval);
      }
    });

    document.getElementById("reset").addEventListener("click", () => {
      running = false;
      clearInterval(timerInterval);
      startTime = 0;
      elapsedTime = 0;
      display.textContent = "00:00:000";
    });
  </script>

</body>
</html>
