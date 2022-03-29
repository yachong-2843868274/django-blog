# 进行users子应用的路由

from django.urls import path
from users.views import RegisterView


urlpatterns =[
    # path的第一个参数:路由
    # path的第一个参数:视图函数名

    # namespace命名空间
    path('register/',RegisterView.as_view(),name='register'),

]