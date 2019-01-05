from country.models import Dong_data
from django.db.models import Q
from . import views

def sortCity(cityList):
    print('함수실행:', cityList)
    dong = Dong_data.objects.all().filter(city__in=cityList)
    print("---- ", cityList)

    global testtest
    testtest = dong
    print("globaltext" , testtest)
   
    print('함수의 데이터셋:', dong)
