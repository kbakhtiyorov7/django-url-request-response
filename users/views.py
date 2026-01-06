from django.http import HttpRequest, HttpResponse


def login_view(request: HttpRequest) -> HttpResponse:
    print(request.path)
    print(request.method)

    if request.method == 'GET':
        pass

    return HttpResponse('login page')


def orders_view(request: HttpRequest) -> HttpResponse:
    query_params = request.GET

    min_value = query_params.get('min')
    max_value = query_params.get('max')
    
    return HttpResponse(f'orders page: [{min_value}, {max_value}]')


def calculators_view(request: HttpRequest) -> HttpResponse:

    # ?num1=3&num2=7&op=+
    
    return HttpResponse(f'result: ') # 'result: 3+7=10

