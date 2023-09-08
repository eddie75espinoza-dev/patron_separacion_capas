# Acá se puede controlar el manejo de errores con los métodos especiales de flask

from flask import Blueprint, Response, jsonify
from ..models.exeptions import (
    InvalidParametersError,
    InvalidMobileNumberError,
    IdentityNotFoundError,
    CarrierNotSopportedError,
    BeneficiaryDupError
)


errors_scope = Blueprint('errors', __name__)

# definición de manejadores de excepciones, esto sustituye el uso de endpoints 

# funcion auxiliar para formatear el mensaje
def __generate_errors_response(error:Exception) -> Response:
    message = {
        'ErrorType': type(error).__name__,
        'Message': str(error) # el mensaje es el que se define al lanzar el error (helpers)
    }
    return jsonify(message)


# Estas funciones se ejecutan cuando tengamos un error específico generando consistencia 
# con los errores HTTP
@errors_scope.app_errorhandler(InvalidParametersError)
def handle_invalid_parameters_error(error:InvalidParametersError) -> Response:
    response = __generate_errors_response(error)
    response.status_code = 422
    return response


@errors_scope.app_errorhandler(InvalidMobileNumberError)
def handle_invalid_mobile_number_error(error:InvalidMobileNumberError) -> Response:
    response = __generate_errors_response(error)
    response.status_code = 422
    return response


@errors_scope.app_errorhandler(IdentityNotFoundError)
def handle_identity_not_found_error(error:IdentityNotFoundError) -> Response:
    response = __generate_errors_response(error)
    response.status_code = 422
    return response


@errors_scope.app_errorhandler(CarrierNotSopportedError)
def handle_carrier_not_sopported_error(error:CarrierNotSopportedError) -> Response:
    response = __generate_errors_response(error)
    response.status_code = 422
    return response


@errors_scope.app_errorhandler(BeneficiaryDupError)
def handle_beneficiary_dup_error(error:BeneficiaryDupError) -> Response:
    response = __generate_errors_response(error)
    response.status_code = 422
    return response