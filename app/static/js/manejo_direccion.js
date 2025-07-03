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

    function validarFormulario(e) {        

        errorNombre.textContent = "";
        errorApellido1.textContent = "";
        errorCorreo.textContent = "";
        errorTelefono.textContent ="";   

        nombreInput.addEventListener("blur", function () {
            if (!nameRegex.test(nombreInput.value.trim())) {
            errorNombre.textContent = "El formato no es válido.";
            } else {
                errorNombre.textContent = "";
            }
        });

        apellido1Input.addEventListener("blur", function () {
            if (!nameRegex.test(apellido1Input.value.trim())) {
            errorApellido1.textContent = "El formato no es válido.";
            } else {
                errorApellido1.textContent = "";
            }
        });

        correoInput.addEventListener("blur", function () {
            if (!emailRegex.test(correoInput.value.trim())) {
            errorCorreo.textContent = "El formato de correo no es válido.";
            } else {
                errorCorreo.textContent = "";
            }
        });

        telefonoInput.addEventListener("blur", function () {
            if (!phoneRegex.test(telefonoInput.value.trim())) {
                errorTelefono.textContent = "El teléfono debe de tener 9 dígitos.";
            } else {
                errorTelefono.textContent = "";
            }
        });        
    }
    municipioInput.addEventListener("input", function () {
        actualizarDireccionSegunMunicipio(this.value.trim().toLowerCase());
    });

    
    actualizarDireccionSegunMunicipio(municipioInput.value.trim().toLowerCase());
    document.querySelector("form").addEventListener("submit", validarFormulario);
    cargarTiposVia();
});
