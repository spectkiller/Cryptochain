from django.urls import path
from . import views


urlpatterns = [
  path("index/", views.index, name="index"),
  path("index_dark/", views.index_dark, name="index_dark"),
  path ("add/", views.add, name="add" ),
  path("add_dark/", views.add_dark, name="add_dark"),
  path("add/addrecord/", views.addrecord, name="addrecord"),
  path("add_dark/addrecord1/", views.addrecord1, name="addrecord1"),
  path('index/delete/<int:id>',views.delete,name='delete'),
  path('index/update/<int:id>',views.update,name='update'),
  path('index/update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
  path('index_dark/delete1/<int:id>',views.delete1,name='delete1'),
  path('index_dark/update/<int:id>',views.update,name='update'),
  path('index_dark/update/updaterecord1/<int:id>',views.updaterecord1,name='updaterecord1'),
  path('pjkt3/', views.send_email, name='send_email'),
  path('pjkt4/', views.pjkt4, name='pjkt4'),
  path('pjkt1/', views.pjkt1, name='pjkt1'),
  path('pjkt2/', views.pjkt2, name='pjkt2'),
  path('pjkt3_dark/', views.send_email1, name='send_email1'),
  path('pjkt4_dark/', views.pjkt4_dark, name='pjkt4_dark'),
  path('pjkt1_dark/', views.pjkt1_dark, name='pjkt1_dark'),
  path('pjkt2_dark/', views.pjkt2_dark, name='pjkt2_dark'),
  path('signup/', views.signup, name='signup'),
  path('', views.login, name='login'),
]