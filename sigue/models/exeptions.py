class InvalidParametersError(Exception):
    """INVALID_PARAMETERS_ERROR"""
    

class InvalidMobileNumberError(Exception):
    """INVALID_MOBILE_NUMBER_ERROR"""


class CarrierNotSopportedError(Exception):
    """CARRIER_NOT_SUPPORTED_ERROR"""


class BeneficiaryDupError(Exception):
    """BENEFICIARY_DUP_ERROR"""


class IdentityNotFoundError(Exception):
    """IDENTITY_NOT_FOUND_ERROR"""