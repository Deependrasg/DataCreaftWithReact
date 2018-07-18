from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views

from DataSearch.views import PublishDataViewSet,SubDepartmentViewSet,SubDepartmentCodeViewSet,SearchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'publish', PublishDataViewSet, base_name='publish')
router.register(r'sub-department', SubDepartmentViewSet, base_name='sub_department')
router.register(r'inventry-code', SubDepartmentCodeViewSet, base_name='inventry-code')
router.register(r'search-data', SearchViewSet, base_name='search-data')




urlpatterns = router.urls

urlpatterns = [
    
    #Start Ddjango Rest FrameWork URLs
    path('data-catalog/', views.DataCatalog.as_view()),
    path('data-catalog/<int:pk>/', views.DetailDataCatalog.as_view()),
    # path('data-search',views.PublisherDataSearch.as_view()),
    url(r'^api/', include(router.urls)),
    
    # Start Django URLs
    path('', views.index, name='index'),
    url(r'^account-signup/$', views.account_signup, name="account_signup"),
    url(r'^user_login/$', views.user_login, name="user_login"),
    url(r'^home/$', views.home, name="home"),
    url(r'^validate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.validate, name='validate'),
    url(r'^userlist/$', views.userlist, name="userlist"),
    url(r'^userlist/show-all-userlist/$', views.all_userlist, name="all_userlist"),
    url(r'^userlist/delete-user/(?P<user_id>[0-9A-Za-z_\-]+)/$', views.delete_user, name="delete_user"),
    url(r'^userlist/validate-user/(?P<user_id>[0-9A-Za-z_\-]+)/$', views.validate_user, name="validate_user"),
    url(r'^userlist/user-role/$', views.user_role, name="user_role"),
    url(r'^all-admin/$', views.all_admin, name="all_admin"),
    url(r'^all-admin/show-all-admin/$', views.show_all_admin, name="show_all_admin"),
    url(r'^all-admin/delete-admin/(?P<user_id>[0-9A-Za-z_\-]+)/$', views.delete_admin, name="delete_admin"),
    url(r'^publisher/$', views.publisher, name="publisher"),
    url(r'^publisher/show-all-publisher/$', views.show_all_publisher, name="show_all_publisher"),   
    url(r'^consumer/$', views.consumer, name="consumer"),
    url(r'^consumer/show-all-consumer/$', views.show_all_consumer, name="show_all_consumer"),   
    url(r'^search-result/$', views.search_result, name="search_result"),
    url(r'^publisher-form/$', views.publisher_form, name="publisher_form"),
    url(r'^publisher-form/get-sub-department/(?P<d_id>[0-9A-Za-z_\-]+)/$', views.get_sub_department, name="get_sub_department"),
    url(r'^publisher-form/get-sub-department-code/(?P<d_id>[0-9A-Za-z_\-]+)/$', views.get_sub_department_code, name="get_sub_department_code"),    
    url(r'^search-result/searching/$', views.searching, name="searching"),
    url(r'^service-data/(?P<d_id>[0-9A-Za-z_\-]+)/$', views.service_data, name="service_data"),
    url(r'^consumer/manage-consumer-type/$', views.manage_consumer, name="manage_consumer"),
]