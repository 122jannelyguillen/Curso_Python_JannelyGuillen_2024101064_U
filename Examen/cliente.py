from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def llamarServicioSet():
    ci = request.json.get('ci')

    
    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': 5611028,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(ci):
    cilocal = "5611028"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    try:
        if cilocal == ci:
            accion = "Success"
        else:
            print("CI incorrecto")
            accion = "CI incorrecto"
            codRes = 'ERROR'
            menRes = 'CI incorrecto'


    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion