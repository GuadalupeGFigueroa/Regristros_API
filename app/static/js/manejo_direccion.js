
document.addEventListener("DOMContentLoaded", function () {
    const municipioInput = document.getElementById("municipio");
    const bloqueLlanera = document.getElementById("direccion_estructurada");
    const bloqueOtros = document.getElementById("direccion_manual");

    municipioInput.addEventListener("input", function () {
        const valor = this.value.trim().toLowerCase();

        if (valor === "llanera") {
            bloqueLlanera.style.display ="block";
            bloqueOtros.style.display = "none"; 
        } else {
            bloqueLlanera.style.display = "none";
            bloqueOtros.style.display = "block";
        }
    });
});
