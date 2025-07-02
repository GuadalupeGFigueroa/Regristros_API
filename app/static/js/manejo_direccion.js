document.addEventListener("DOMContentLoaded", function () {
    const municipioInput = document.getElementById("municipio");
    const bloqueLlanera = document.getElementById("direccion_estructurada");
    const bloqueOtros = document.getElementById("direccion_manual");

    const nombre = document.getElementById("nombre");
    const apellido = document.getElementById("apellido1");
    const correo = document.getElementById("correoElectronico");
    const telefono = document.getElementById("telefono");
    const errorNombre = document.getElementById("error-nombre");
    const errorCorreo = document.getElementById("error-correo");
    const errorTelefono = document.getElementById("error-telefono");
    
    const nameRegex = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\- ]+$/;
    const apellido1 = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\- ]+$/;
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

        correoInput.addEventListener("blur", function () {
            if (!emailRegex.test(correoInput.value.trim())) {
            errorNombre.textContent = "El formato de correo no es válido.";
            } else {
                errorCorreo.textContent = "";
            }
        });

         correoInput.addEventListener("blur", function () {
            if (!emailRegex.test(correoInput.value.trim())) {
            errorApellido1.textContent = "El formato de correo no es válido.";
            } else {
                errorCorreo.textContent = "";
            }
        });

        correoInput.addEventListener("blur", function () {
            if (!emailRegex.test(correoInput.value.trim())) {
            errorCorreo.textContent = "El formato de correo no es válido.";
            } else {
                errorCorreo.textContent = "";
            }
        });

        telefonoInput.addEventListenerr("blur", function () {
            if (!phoneRegex.test(telefonoInput.value.trim())) {
                errorTelefono.textContent = "El teléfono debe de tener 9 dígitos.";
            } else {
                errorCorreo.textContent = "";
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
