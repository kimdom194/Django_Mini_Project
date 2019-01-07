from django.db import models

# 강원도지역 병원, 학교, 집값, 주소를 담은 csv파일 데이터 모델 정의
class Dong_data(models.Model):
    dong = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    medical = models.IntegerField(default=0)
    school = models.IntegerField(default=0)
    house = models.IntegerField(default=0)

    def __str__(self):
        return self.dong

# 인덱스에서 선택할 수 있는 선택 데이터
class KangwonCity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 디테일에서 선택할 수 있는 선택 데이터
class Infra(models.Model):
    infraType = models.CharField(max_length=50)

    def __str__(self):
        return self.infraType



