def ResponseModel(data, message, code = 200):
    return {
        "data": data,
        "code": code,
        "message": message
    }

def ErrorResponseModel(error, message, code):
    return {
        "error": error,
        "code": code,
        "message": message
    }