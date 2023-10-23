from django.urls import path
from . import views


# FOR URL & FOR NEW PAGES , MUST DECLARE PATH 
urlpatterns = [
    path('', views.home, name='home'),
    #LOGIN AUTHENTICATION IS ALREADY IN HOME SCREEN
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/', views.customer, name='customer'),
    path('category/', views.category, name='category'),
    path('brand/', views.brand, name='brand'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('brand/view/<int:brand_id>/', views.view_brand, name='view_brand'),
    path('brand/edit/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    path('brand/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('add_categpry/', views.add_category, name='add_category'),
    path('category/view/<int:category_id>/', views.view_category, name='view_category'),
    path('category/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('product/', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/view/<int:product_id>/', views.view_product, name='view_product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    path('add_role/', views.add_role, name='add_role'),
    path('user_list/', views.user_list, name='user_list'),
    



]