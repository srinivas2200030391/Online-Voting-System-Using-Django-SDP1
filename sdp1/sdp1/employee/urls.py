from django.urls import path, include
from . import views

urlpatterns = [
    path('checkuser', views.checkuser, name="checkuser"),
    path('addvoter', views.addvoter, name="addvoter"),
    path('dashboard', views.dash, name="dashboard"),
    path('addvo1', views.addvo1, name="addvo1"),
    path('delvot1', views.delvot1, name="delvot1"),
    path('forgot', views.forgot, name="forgot"),
    path('check_pw', views.check_pw, name="check_pw"),
    path('send_otp', views.send_otp, name="send_otp"),
    path('validate_otp', views.validate_otp, name="validate_otp"),
    path('dash', views.dash, name="dash"),
    path('logout', views.logout, name="logout"),
    path('updatevote', views.update, name="update"),
    path('dashboard', views.dashb, name="dashb"),
    path('dashboard1', views.dashb1, name="dashb1"),
    path('dash1', views.dash, name="dash1"),
    path('vote',views.vote,name="vote"),
]
