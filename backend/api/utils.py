from rest_framework.exceptions import ErrorDetail
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if response.status_code == 400:
            for error in response.data:
                if response.data[error] == [
                    ErrorDetail(
                        string='This field is required.', code='required'
                    )
                ]:
                    response.data[error] = 'Обязательное поле.'
        if response.status_code == 401:
            response.data['detail'] = 'Учетные данные не были предоставлены.'
        if response.status_code == 403:
            response.data[
                'detail'
            ] = 'У вас недостаточно прав для выполнения данного действия.'
        if response.status_code == 404:
            response.data['detail'] = 'Страница не найдена.'

    return response
