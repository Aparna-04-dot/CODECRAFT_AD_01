<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>To-Do List App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      justify-content: center;
      padding-top: 50px;
    }
    .container {
      background: white;
      padding: 20px;
      border-radius: 8px;
      width: 300px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h2 {
      text-align: center;
    }
    input[type="text"] {
      width: 80%;
      padding: 10px;
      margin-bottom: 10px;
    }
    button {
      padding: 10px;
      margin-left: 5px;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      padding: 8px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .actions button {
      margin-left: 5px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>To-Do List</h2>
    <input type="text" id="taskInput" placeholder="Add new task...">
    <button onclick="addTask()">Add</button>
    <ul id="taskList"></ul>
  </div>

  <script>
    function addTask() {
      const input = document.getElementById("taskInput");
      const taskText = input.value.trim();
      if (taskText === "") return;

      const li = document.createElement("li");
      const span = document.createElement("span");
      span.textContent = taskText;

      const actions = document.createElement("div");
      actions.className = "actions";

      const editBtn = document.createElement("button");
      editBtn.textContent = "Edit";
      editBtn.onclick = () => editTask(span);

      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Delete";
      deleteBtn.onclick = () => li.remove();

      actions.appendChild(editBtn);
      actions.appendChild(deleteBtn);

      li.appendChild(span);
      li.appendChild(actions);

      document.getElementById("taskList").appendChild(li);
      input.value = "";
    }

    function editTask(span) {
      const newTask = prompt("Edit task:", span.textContent);
      if (newTask !== null && newTask.trim() !== "") {
        span.textContent = newTask.trim();
      }
    }
  </script>
</body>
</html>
