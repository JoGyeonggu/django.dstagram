from django.urls import path
from django.views.generic.detail import DetailView
from .views import *

# 2차 URL 파일

app_name = 'photo'

# 함수형 뷰 , 제네릭 뷰에 따라 연결방법이 다르다

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),

]