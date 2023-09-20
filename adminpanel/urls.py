from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.adminPanelView, name='admin_panel_dashboard'),
    path('team-member/', views.team_memberView, name='team_member'),
    path('admin-signup-request/', views.admin_signup_requestView.as_view(), name='admin_signup_request'),
    path('admin-signup/<uidb64>/<token>/', views.admin_signupView.as_view(), name='admin_signup'),
    path('admin-request-list/', views.admin_request_listView, name='admin_request_list'),
    path('admin-request-approve/', views.admin_request_approve, name='admin_request_approve'),
    path('admin-request-decline/', views.admin_request_decline, name='admin_request_decline'),
    path('remove-admin/', views.remove_admin, name='remove_admin'),
    path('remove-user/', views.remove_user, name='remove_user'),
    path('customers/', views.customerView, name='customer_list'),
    path('products/', views.productView, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/', views.edit_product, name='edit_product'),
    path('delete-product/', views.delete_product, name='delete_product'),
    path('restock-product/', views.restock_product, name='restock_product'),
    path('individual-product-details/', views.individual_product_details, name='individual_product_details'),
    path('queries/', views.queries, name='queries'),
    path('view-query/', views.view_query, name='view_query'),
    path('reply-query/', views.reply_query, name='reply_query'),
    path('main-category-list/', views.main_categoryView, name='main_category_list'),
    path('category-list/', views.categoryView, name='category_list'),
    path('sub-category-list/', views.sub_categoryView, name='sub_category_list'),
    path('add-main-category/', views.add_main_category, name='add_main_category'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-sub-category/', views.add_sub_category, name='add_sub_category'),
    path('edit-main-category/', views.edit_main_category, name='edit_main_category'),
    path('edit-category/', views.edit_category, name='edit_category'),
    path('edit-sub-category/', views.edit_sub_category, name='edit_sub_category'),
    path('delete-main-category/', views.delete_main_category, name='delete_main_category'),
    path('delete-category/', views.delete_category, name='delete_category'),
    path('delete-sub-category/', views.delete_sub_category, name='delete_sub_category'),
    path('sliders/', views.slidersView, name='sliders'),
    path('add-slider/', views.add_slider, name='add_slider'),
    path('delete-slider/', views.delete_slider, name='delete_slider'),
    path('edit-slider/', views.edit_slider, name='edit_slider'),
    path('slider-details/', views.slider_details, name='slider_details'),
    path('banners/', views.bannersView, name='banners'),
    path('add-banner/', views.add_banner, name='add_banner'),
    path('delete-banner/', views.delete_banner, name='delete_banner'),
    path('edit-banner/', views.edit_banner, name='edit_banner'),
    path('banner-details/', views.banner_details, name='banner_details'),
]