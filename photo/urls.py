from django.urls import path
from .views import *

# 2차 URL 파일

app_name = 'photo'

# 함수형 뷰 , 제네릭 뷰에 따라 연결방법이 다르다

urlpatterns = [
    path('', photo_list, name='photo_list'),

]