from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    user_list = [
        {"nome": "Nuno Moreira", "matricula": 17, "idade": 25, "cidade": "Espinho"},
        {"nome": "Coutinho", "matricula": 11, "idade": 33, "cidade": "Rio de Janeiro"},
        {"nome": "Vegetti", "matricula": 99, "idade": 36, "cidade": "Santo Domingo"},
        {"nome": "Léo Jardim", "matricula": 1, "idade": 30, "cidade": "Ribeirão Preto"},
        {"nome": "Rayan", "matricula": 77, "idade": 18, "cidade": "Rio de Janeiro"},
    ]

    context = {
        "usuarios": user_list,
    }
    return render(request, "usuarios.html", context)
