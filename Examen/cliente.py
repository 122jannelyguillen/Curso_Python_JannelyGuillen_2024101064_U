clientes_registrados = {
    "5611028": {
        "nombre": "Jannely Guillen",
        "ci": "5611028"
    },
    "4712334": {
        "nombre": "Maria Gomez",
        "ci": "4712334"
    }
}

def verificar_cliente(ci):
    if ci in clientes_registrados:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }
    else:
        return {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }
