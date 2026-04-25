async function loadSidebar() {
  const res = await fetch("http://127.0.0.1:8000/api/sidebar");
  const data = await res.json();

  const sidebar = document.getElementById("sidebar");

  sidebar.innerHTML = data.map(item => {
    return `<div>${item.title}</div>`;
  }).join("");
}

async function addItem() {
  const title = prompt("New sidebar item name:");

  if (!title) return;

  await fetch("http://127.0.0.1:8000/api/sidebar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title })
  });

  loadSidebar(); // refresh UI
}

document.getElementById("addBtn").addEventListener("click", addItem);

loadSidebar();