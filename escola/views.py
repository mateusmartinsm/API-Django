from django.http import JsonResponse # Biblioteca para renderizar um JSON

def aluno(request):
    if request.method == 'GET':
        aluno = {'id':1, 'nome':'Guilherme'}
        return JsonResponse(aluno)