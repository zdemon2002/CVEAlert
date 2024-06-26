from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('login/', views.get_login, name='login'),
    path('sign-up/', views.get_sign_up, name='sign_up'),
    path('log-out/', views.get_logout, name='log_out'),
    path('change-password/<int:pk>/', views.change_password_view, name='change_password'),
    path('profile/', views.profile_detail_view, name='profile'),
    path('list-product', views.list_product_view, name='list_product'),
    #Thêm hàm tại đây!
    path('list-cve-by-product/', views.list_cve_by_product_view, name='list_cve_by_product'),
	path('notification/', views.notification_user_view, name='notification'),
]