from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import dong_data
    

# 인덱스 화면을 띄우는 함수
def index(request):
    print("---------index()-------------")

    return render(request, 'country/index.html')

"""
def detail(request):
    print("---------detail()-------------")
    dong = dong_data.objects.all()
    dong = dong.filter(Q(city='강릉시') | Q(city='동해시') | Q(city='춘천시'))
    context = {'dong':dong}
    return render(request, 'country/detail.html', context)
"""

def detail(request):
    print("---------detail()-------------")
    try:
        form = request.POST['selectedCity']
        print('입력된 값 : ', form)
        cityList = form.split(',')
        print('변환된 값 : ', cityList)

    except(KeyError):
        return render(request, 'country/detail.html',{'error_message' : '값 오류입니다.'} )
    
    args = {'cityList':cityList}

    #dong = dong_data.objects.all()
    #dong = dong.filter(city==cityList)
    #context = {'dong':dong}

    # 받아온 지역이름에 해당하는 데이터만 갖고오는 sortCity()함수 호출
    dong = dong_data.objects.all()
    dong = dong.filter(city__in= cityList)
    context = {'dong':dong}
    global testtest
    testtest = dong
    print("globaltext" , testtest)
    return render(request, 'country/detail.html', context)
    # request.session['selectedCity'] = cityList


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

    print("dong data print : ",dong)

    context = {'dong':dong}

    # return render(request, 'country/result.html')
    return render(request, 'country/result.html', context)




# 인덱스 화면에서 값 입력 받고 시별로 정렬 한 후 디테일로 넘기는 함수(세션 유지)


# 디테일 화면에서 값 입력 받고 결과창으로 넘기는 함수


# 로직 함수 결과 받아서 결과 창에서 지도로 시각화해 보여주는 함수
