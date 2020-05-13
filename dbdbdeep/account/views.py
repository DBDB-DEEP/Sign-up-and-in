from django.shortcuts import render
from django.views import View
from .models import Account
from django.http import HttpResponse, JsonResponse
from .models import *

def signUp(request):
    return render(request, 'sign_up.html')

def doSignUp(request):
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        nickname = request.POST['nickname']

        new_user = Account(
            email=email,
            password = password,
            name = name,
            nickname = nickname
            )
        new_user.save()
        
    return render(request, 'signupSuccess.html')



# class SignUpView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Account(
#             email    = data['email'],
#             name     = data['name'],
#             password = data['password'],
#             gender = data['gender'],
#             birth_year = data['birth_year'],
#             birth_month = data['birth_month'],
#             birth_date= data['birth_date'],
#             nickname = data['nickname']
#         ).save()						# 받아온 데이터를 DB에 저장시켜줌

#         return HttpResponse(status=200) 

# class SignInView(View):
#     def post(self, request):
#         data = json.loads(request.body)

#         if Account.objects.filter(email = data['email']).exists() :
#             user = Account.objects.get(email = data['email'])

#             if user.password == data['password'] :
#                 return HttpResponse(status=200)
#             else :
#                 return HttpResponse(status = 401)

#         return HttpResponse(status=400)


# def signin(request):
#     return render(request,'sign_in.html')

# Create your views here.
