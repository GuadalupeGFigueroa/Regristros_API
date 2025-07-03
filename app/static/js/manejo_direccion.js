document.addEventListener("DOMContentLoaded", function () {
    const municipioInput = document.getElementById("municipio");
    const bloqueLlanera = document.getElementById("direccion_estructurada");
    const bloqueOtros = document.getElementById("direccion_manual");

    const nombreInput = document.getElementById("nombre");
    const apellido1Input = document.getElementById("apellido1");
    const correoInput = document.getElementById("correoElectronico");
    const telefonoInput = document.getElementById("telefono");

    const errorNombre = document.getElementById("error-nombre");
    const errorApellido1 = document.getElementById("error-apellido1");
    const errorCorreo = document.getElementById("error-correo");
    const errorTelefono = document.getElementById("error-telefono");
    
    const nameRegex = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\- ]+$/;
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

    function validarCampo(input, errorElem, regex, mensaje) {        
        const valor = input.value.trim();
        if (!regex.test(valor)) {
            errorElem.textContent = mensaje;
            return false;
        } else {
            errorElem.textContent = "";
            return true;
            }
        }
        
        nombreInput.addEventListener("blur", () => {
            validarCampo(nombreInput, errorNombre, nameRegex, "Nombre no válido.");
        });

        apellido1Input.addEventListener("blur", () => {
            validarCampo(apellido1Input, errorApellido1, nameRegex, "Apellido no válido.");
        });

        telefonoInput.addEventListener("blur", () => {
            validarCampo(telefonoInput, errorTelefono, phoneRegex, "Teléfono no válido.");
        });

        correoInput.addEventListener("blur", () => {
            validarCampo(correoInput, errorCorreo, emailRegex, "Introduce un correo válido.");
        });

    function validarFormulario(e) { 
        const esValido = 
            validarCampo(nombreInput, errorNombre, nameRegex, "Nombre no válido.") &
            validarCampo(apellido1Input, errorApellido1, nameRegex, "Apellido no válido.") &
            validarCampo(correoInput, errorCorreo, emailRegex, "Correo no válido.") &
            validarCampo(telefonoInput, errorTelefono, phoneRegex, "Teléfono no válido.");

            if (!esValido) e.preventDefault();
    }
       
    
    municipioInput.addEventListener("input", function () {
        actualizarDireccionSegunMunicipio(this.value.trim().toLowerCase());
    });

    actualizarDireccionSegunMunicipio(municipioInput.value.trim().toLowerCase());
    document.querySelector("form").addEventListener("submit", validarFormulario);
    cargarTiposVia();
});
