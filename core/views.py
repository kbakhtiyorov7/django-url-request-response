from django.http import HttpRequest, HttpResponse

def home_view(request:HttpRequest) -> HttpResponse:
    return HttpResponse("Siz home bo'limidasiz")



def users_view(request:HttpRequest, username:str) -> HttpResponse:
    return HttpResponse(f'Salom {username.title()}')

def find_products_by_id_view(request:HttpRequest, product_id:int) -> HttpResponse:
    return HttpResponse(f"Siz izlagan product_id = {product_id}")


def search_with_slug_view(request:HttpRequest, title:str) -> HttpResponse:
    return HttpResponse(f"title: {title}")

def uuid_view(request:HttpRequest, uuid:str) -> HttpResponse:
    return HttpResponse(f"UUID: {uuid}")

def path_converters_view(request:HttpRequest, path:str) -> HttpResponse:
    return HttpResponse(f"Path: {path}")