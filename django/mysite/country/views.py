from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from country.func import sortCity
from country.models import KangwonCity, Infra, Dong_data


# 인덱스 화면을 띄우는 함수
def index(request):
    print("---------index()-------------")
    city_list = KangwonCity.objects.all()
    print(city_list)
    context = {'city_list': city_list}
    return render(request, 'country/index.html', context)


# 인덱스에서 비동기로 값 넘기기
def searching(request):
    print("------searching()-------")
    try:
         form = request.POST['data']
         print('입력된 값 : ', form)
         cityList = form.split(',')
         print('변환된 값 : ', cityList)
    except(KeyError):

         return render(request, {'error_message' : '값 오류입니다.'} )

    dong = Dong_data.objects.all()
    dong = dong.filter(city__in= cityList)
    context = {'dong': dong}
    global testtest

    testtest = dong
    print("global 데이터" , testtest)
    return HttpResponse(request, content_type="text/plain")


# 디테일 화면에서 값 입력 받고 결과창으로 넘기는 함수


def result(request):
    print("infotest", testtest)
    print("---------result()-------------")
    rank1 = request.POST['rankForm1']
    print('입력된 1순위 : ', rank1)

    rank2 = request.POST['rankForm2']
    print('입력된 2순위 : ', rank2)

    rank3 = request.POST['rankForm3']
    print('입력된 3순위 : ', rank3)

    dong = testtest.order_by(rank1, rank2, rank3)[:10]
    
    context = {'dong':dong}
    print(context)
    # return render(request, 'country/result.html')
    return render(request, 'country/result.html', context)
