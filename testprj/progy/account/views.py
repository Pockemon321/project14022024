from django.shortcuts import render
from django.http import HttpResponse
from models import Name

def hello_world(request):
    return HttpResponse("Hello World!")


def add_numbers(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        sum = num1 + num2
        return HttpResponse(f"Сумма чисел {num1} и {num2} равна {sum}")
    else:
        return HttpResponse("Введите 2 числа и нажмите Submit")

def name_list(request):
    names = Name.object.all()
    return render(request, 'account/name_list.html', {'names': names})