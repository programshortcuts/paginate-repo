async function loadSidebar() {
  const res = await fetch("http://127.0.0.1:8000/api/sidebar");
  const data = await res.json();

  console.log("DATA:", data);

  const sidebar = document.getElementById("sidebar");

  sidebar.innerHTML = data.map(item => {
    return `
            <div class="item">
                <h3>${item.title}</h3>
            </div>
        `;
  }).join("");

  console.log("APP JS LOADED");
}

loadSidebar();