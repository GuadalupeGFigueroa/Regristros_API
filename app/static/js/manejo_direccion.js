document.addEventListener("DOMContentLoaded", function () {
    const pasos = ["paso1", "paso2", "paso3"];
    let pasoActual = 0; 

    function mostrarPaso(nuevoPaso) {
        pasos.forEach((id, i) => {
            document.getElementById(id).style.display = i === nuevoPaso ? "block" : "none";
        });
        document.getElementById("etapa-actual").textContent = nuevoPaso+1;
        pasoActual = nuevoPaso;
    }

    const nombreInput = document.getElementById("nombre");
    const apellido1Input = document.getElementById("apellido1");
    const apellido2Input = document.getElementById("apellido2");
    const correoInput = document.getElementById("correoElectronico");
    const telefonoInput = document.getElementById("telefono");

    const errorNombre = document.getElementById("error-nombre");
    const errorApellido1 = document.getElementById("error-apellido1");
    const errorApellido2 = document.getElementById("error-apellido2");
    const errorCorreo = document.getElementById("error-correo");
    const errorTelefono = document.getElementById("error-telefono");
    
    const nameRegex = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\- ]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^\d{9}$/; 

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
        
        //Validación campos paso 1
        nombreInput.addEventListener("blur", () => {
            validarCampo(nombreInput, errorNombre, nameRegex, "Nombre no válido.");
        });

        apellido1Input.addEventListener("blur", () => {
            validarCampo(apellido1Input, errorApellido1, nameRegex, "Apellido no válido.");
        });

        apellido2Input.addEventListener("blur", () => {
            validarCampo(apellido2Input, errorApellido2, nameRegex, "Apellido no válido.");
        });

        telefonoInput.addEventListener("blur", () => {
            validarCampo(telefonoInput, errorTelefono, phoneRegex, "Teléfono no válido.");
        });

        correoInput.addEventListener("blur", () => {
            validarCampo(correoInput, errorCorreo, emailRegex, "Introduce un correo válido.");
        });
    
    //Validación para pasar al paso 2
    function validarFormulario() { 
        const valido =
            validarCampo(nombreInput, errorNombre, nameRegex, "Nombre no válido.") &
            validarCampo(apellido1Input, errorApellido1, nameRegex, "Apellido no válido.") &
            validarCampo(apellido2Input, errorApellido2, nameRegex, "Apellido no válido.") &
            validarCampo(correoInput, errorCorreo, emailRegex, "Correo no válido.") &
            validarCampo(telefonoInput, errorTelefono, phoneRegex, "Teléfono no válido.");
            return !!valido;
    }
     
    document.getElementById("boton-siguiente1").addEventListener("click",function() {
        if (validarFormulario()) {
            mostrarPaso(1);
        }
    });

    document.getElementById("boton-atras1").addEventListener("click", () => mostrarPaso(0));
    document.getElementById("boton-siguiente2").addEventListener("click", () => mostrarPaso(2));
    document.getElementById("boton-atras2").addEventListener("click", () => mostrarPaso(1));

    document.getElementById("boton-enviar").addEventListener("click", function(){
        if (confirm("¿Desea enviar el registro?")) {
            document.querySelector("form").submit();
            }
        });
        mostrarPaso(0);
    
    // Dinámica de bloques por municipio
    const municipioInput = document.getElementById("municipio");
    const bloqueLlanera = document.getElementById("direccion_estructurada");
    const bloqueOtros = document.getElementById("direccion_manual");

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
    
    municipioInput.addEventListener("input", function () {
        actualizarDireccionSegunMunicipio(this.value.trim().toLowerCase());
    });

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

    cargarTiposVia();
});
