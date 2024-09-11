document.addEventListener("DOMContentLoaded", function() {
    // Funcionalidad de desplazamiento suave para enlaces internos
    const links = document.querySelectorAll("nav ul li a");
    for (const link of links) {
        link.addEventListener("click", function(event) {
            const href = this.getAttribute("href");
            // Verificar si el enlace es interno (empieza con "#")
            if (href.startsWith("#")) {
                // Prevenir el comportamiento predeterminado solo para enlaces internos
                event.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: "smooth"
                });
                // Cierra el menú en móviles
                document.querySelector("nav ul").classList.remove("show");
            }
        });
    }

    // Funcionalidad del menú desplegable
    const dropdowns = document.querySelectorAll(".dropdown");
    dropdowns.forEach(dropdown => {
        const dropbtn = dropdown.querySelector(".dropbtn");
        const dropdownContent = dropdown.querySelector(".dropdown-content");

        dropbtn.addEventListener("mouseenter", function() {
            dropdownContent.style.display = "block";
        });

        dropdown.addEventListener("mouseleave", function() {
            dropdownContent.style.display = "none";
        });
    });

    // Funcionalidad del menú hamburguesa en móviles
    const menuToggle = document.createElement("button");
    menuToggle.className = "menu-toggle";
    menuToggle.textContent = "☰";
    document.querySelector("header").appendChild(menuToggle);

    menuToggle.addEventListener("click", function() {
        document.querySelector("nav ul").classList.toggle("show");
    });
});
