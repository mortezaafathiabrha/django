from django.http import HttpResponse
from django.urls import path


def hello_world(request):
    return HttpResponse('''<!DOCTYPE html>
<html>
<head>
    <title>Hello World - Django</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: linear-gradient(135deg, #00b4db 0%, #0083b0 100%); }
        .container { text-align: center; color: white; }
        h1 { font-size: 3em; margin: 0; }
        p { font-size: 1.2em; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World!</h1>
        <p>Welcome to Django</p>
    </div>
</body>
</html>''')


urlpatterns = [
    path('', hello_world),
]
