from django.shortcuts import render
import random
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'generator/index.html')

def generate_random(request):
    number = random.randint(1, 1000)
    return JsonResponse({'number': number})