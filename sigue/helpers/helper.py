# funciones para validar el formateo de teléfonos, entre otros
# Acá se pueden usar las excepciones para que se ejecuten en la ultima capa
# y evitar usar try-except en los controladores salvo que el error pueda ser corregido


# Acá podría ir argephone

from ..models.exeptions import InvalidParameterError

def is_validate_mobile_number(mobile_number):
    # validación de teléfono
    if mobile_number is None:
        raise InvalidParameterError('INVALID PARAMETERS')