from .models import dong_data
from django.db.models import Q
from . import views

def sortCity(cityList):
    dong = dong_data.objects.all()
    dong = dong.filter(city__in= cityList )
    context = {'dong':dong}
   
    print(dong)




'''
*** 구현할 함수 ***

1.(선택) 시군구 선택하기:
사용자가 클릭한 '시' 데이터와 
db에 저장되있는 '시' 컬럼의 데이터가 같을 경우 
해당 테이블 데이터 가져오기

2.(필수) 우선순위 별로 정렬 하기
- 1순위, 2순위, 3순위 별로 정렬
    경우의 수 
             가격 병원 학교
             가격 학교 병원
             병원 가격 학교
             병원 학교 가격
             학교 병원 가격
             학교 가격 병원
             :   경우의 수 = 6개

    frist_con
    second_con
    third_con  

    frist_con : '가격' or '병원' or '학교' 
    second_con : '가격' or '병원' or '학교' 
    third_con : '가격' or '병원' or '학교' 





3.(선택) 정렬 된 수를 입력받은 개수(5개, 10개, 15개, 20개) 까지 잘라서 보여주기


'''


def select_si(siName):
    pass




