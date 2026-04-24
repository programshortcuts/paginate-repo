async function loadSidebar() {
    const res = await fetch("http://127.0.0.1:8000/api/sidebar");
    const data = await res.json();

    const sidebar = document.getElementById("sidebar");

    sidebar.innerHTML = data.sidebar.map(item => {
        return `
      <div>
        <h3>${item.title}</h3>
        <ul>
          ${item.children.map(child => `<li>${child.title}</li>`).join("")}
        </ul>
      </div>
    `;
    }).join("");
}

loadSidebar();