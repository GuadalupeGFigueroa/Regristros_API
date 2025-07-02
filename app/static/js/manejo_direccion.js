document.addEventListener("DOMContentLoaded", function () {
    const municipioInput = document.getElementById("municipio");
    const bloqueLlanera = document.getElementById("direccion_estructurada");
    const bloqueOtros = document.getElementById("direccion_manual");
    

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^\d{9}$/; 

    function actualizarDireccionSegunMunicipio(valor){

        if (valor === "llanera") {
            bloqueLlanera.style.display ="block";
            bloqueOtros.style.display = "none"; 
        } else if (valor !== "llanera") {
            bloqueLlanera.style.display = "none";
            bloqueOtros.style.display = "block";
        } else {
            //Si se borra el contenido del campo
            bloqueLlanera.style.display = "none";
            bloqueOtros.style.display = "none";
        }
    }

    function cargarTiposVia() {
        fetch("/api/tipos-via")
            .then(res => res.json())
            .then(tipos => {
                const select = document.getElementById("tipoVia");
                tipos.forEach(tipo => {
                    const option = document.createElement("option");
                    option.value = tipo;
                    option.textContent = tipo;
                    select.appendChild(option);
                });
            })
            .catch(err => console.error("Error al cargar los tipos de vía.", err));
    }

    function validarFormulario(e) {
        const correo = document.getElementById("correoElectronico");
        const telefono = document.getElementById("telefono");
        const errorCorreo = document.getElementById("error-correo");
        const errorTelefono = document.getElementById("error-telefono");

        errorCorreo.textContent = "";
        errorTelefono.textContent ="";

        let esValido = true;

        if (!emailRegex.test(correo.value)) {
        errorTelefono.textContent = "El formato de correo no es válido.";
        esValido = false;
        }
        if (!phoneRegex.test(telefono.value)) {
            errorTelefono.textContent = "El teléfono debe de tener 9 dígitos.";
            esValido = false;
        }
        if (!esValido){
            e.preventDefailt(); 
        }

    }
    municipioInput.addEventListener("input", function () {
        actualizarDireccionSegunMunicipio(this.value.trim().toLowerCase());
    });

    
    actualizarDireccionSegunMunicipio(municipioInput.value.trim().toLowerCase());
    document.querySelector("form").addEventListener("submit", validarFormulario);
    cargarTiposVia();
});
