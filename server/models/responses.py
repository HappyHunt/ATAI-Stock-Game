def response_model(data, message, code=200):
    return {
        "data": data,
        "code": code,
        "message": message
    }


def error_response_model(error, message, code):
    return {
        "error": error,
        "code": code,
        "message": message
    }
