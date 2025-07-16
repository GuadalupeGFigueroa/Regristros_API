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
    const codPostal_manualInput = document.getElementById("codPostal_manual");
    
    // Dinámica de bloques por municipio
    const municipioInput = document.getElementById("municipio");
    const bloqueLlanera = document.getElementById("direccion_estructurada");
    const bloqueOtros = document.getElementById("direccion_manual");
    

    const errorNombre = document.getElementById("error-nombre");
    const errorApellido1 = document.getElementById("error-apellido1");
    const errorApellido2 = document.getElementById("error-apellido2");
    const errorCorreo = document.getElementById("error-correo");
    const errorTelefono = document.getElementById("error-telefono");
    const errorCodPostal_manual = document.getElementById("error-codPostal_manual");
    
    const nameRegex = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\- ]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^\d{9}$/; 
    const codPostal_manualRegex = /^\d{5}$/; 

    
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

    codPostal_manualInput.addEventListener("blur", () => {
        validarCampo(codPostal_manualInput, errorCodPostal_manual, codPostal_manualRegex, "Introduce un código postal válido.");
    });
    
    //Validación para pasar al paso 2
    function validarFormulario() { 
        const apellido2Valido = apellido2Input.value.trim() === "" ? true :
                validarCampo(apellido2Input, errorApellido2, apellido2Regex, "Apellido no válido");

        const correoValido = correoInput.value.trim() === "" ? true :
                validarCampo(correoInput, errorCorreo, emailRegex, "Correo no válido.");
            
        const codPostal_manualValido = codPostal_manualInput.value.trim() === "" ? true :
            validarCampo(codPostal_manualInput, errorCodPostal_manual, codPostal_manualRegex, "Codigo postal no válido.");

        const valido =
            validarCampo(nombreInput, errorNombre, nameRegex, "Nombre no válido.") &&
            validarCampo(apellido1Input, errorApellido1, nameRegex, "Apellido no válido.") &&
            apellido2Valido &&
            correoValido &&
            validarCampo(telefonoInput, errorTelefono, phoneRegex, "Teléfono no válido.") &&
            codPostal_manualValido;            
            return valido;
    }
    
    
    document.getElementById("boton-siguiente1").addEventListener("click",function() {
        if (validarFormulario()) {
            mostrarPaso(1);
            actualizarDireccionSegunMunicipio(municipioInput.value.trim().toLowerCase());
        }
    });

    document.getElementById("boton-atras1").addEventListener("click", () => mostrarPaso(0));
    document.getElementById("boton-siguiente2").addEventListener("click", () => mostrarPaso(2));
    document.getElementById("boton-atras2").addEventListener("click", () => mostrarPaso(1));

   
    function actualizarDireccionSegunMunicipio(valor){

        if (valor === "llanera") {
            bloqueLlanera.style.display ="block";
            bloqueOtros.style.display = "none"; 
            cargarCodigosPostales(); 
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
                const select = document.getElementById("tipo_via");
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

    function cargarNombresVia() {
        fetch("/api/via")
            .then(res => res.json())
            .then(vias => {
                const select = document.getElementById("nombre_via");
                vias.forEach(via => {
                    const option = document.createElement("option");
                    option.value = via;
                    option.textContent = via;
                    select.appendChild(option);
                });
            })
            .catch(err => console.error("Error al cargar los nombres de vía.", err));
    }
    cargarNombresVia();

    function cargarCodigosPostales(){
        const municipio = municipioInput.value.trim().toLowerCase();

        if (municipio === "llanera") {
            fetch("/api/codigos-postales?mun_id=35")
                .then(res => res.json())
                .then(codigos => {
                    const select = document.getElementById("codPostal");
                    select.innerHTML = ""; //Limpiar anteriores

                    codigos.forEach(codigo => {
                        const option = document.createElement("option");
                        option.value = codigo;
                        option.textContent = codigo; 
                        select.appendChild(option);
                    });
                })
                .catch(err => console.error("Error al cargar los códigos postales.", err));
        }
    }
    cargarCodigosPostales();

    document.getElementById("boton-siguiente2").addEventListener("click", () => {
        document.getElementById("resumen-nombre").textContent = nombreInput.value.trim();
        document.getElementById("resumen-apellido1").textContent = apellido1Input.value.trim();
        document.getElementById("resumen-apellido2").textContent = apellido2Input.value.trim();
        document.getElementById("resumen-telefono").textContent = telefonoInput.value.trim();
        document.getElementById("resumen-correo").textContent = correoInput.value.trim();
        document.getElementById("resumen-municipio").textContent = municipioInput.value.trim();
        document.getElementById("resumen-observaciones").textContent = document.getElementById("observaciones").value.trim();

        //Dirección según municipio
        let direccion = "";

        if (municipioInput.value.trim().toLowerCase() === "llanera") {
            const tipo = document.getElementById("tipo_via").value;
            const nombreVia = document.getElementById("nombre_via").value;
            const numero = document.getElementById("numero").value;
            const piso = document.getElementById("piso").value;
            const puerta = document.getElementById("puerta").value;
            const codPostal_manual = document.getElementById("codPostal").value;

            direccion = `${tipo} ${nombreVia}, nº ${numero}, ${piso} ${puerta} CP ${codPostal_manual}`;
        } else {
            const tipo = document.getElementById("tipo_via_manual").value;
            const nombreVia = document.getElementById("nombre_via_manual").value;
            const numero = document.getElementById("numero_manual").value;
            const piso = document.getElementById("piso_manual").value;
            const puerta = document.getElementById("puerta_manual").value;
            const codPostal_manual = document.getElementById("codPostal_manual").value;

            direccion = `${tipo} ${nombreVia}, nº ${numero}, ${piso} ${puerta} CP ${codPostal_manual}`;
        }
        
        document.getElementById("resumen-direccion").textContent = direccion.trim();
        mostrarPaso(2);
        
    })

});
