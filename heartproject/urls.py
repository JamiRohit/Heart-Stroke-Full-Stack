"""
URL configuration for strokeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usersapp import views as user
from adminsapp import views as admins
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admins/', admin.site.urls),
    path('', user.user_index,name='user_index'),
    path('user/aboutus', user.user_about,name='user_about'),
    path('user/contactus', user.user_contact,name='user_contact'),
    path('user/userlogin', user.user_login,name='user_login'),
    path('user/adminlogin', user.admin_login,name='admin_login'),
    path('user/registration', user.user_registration,name='user_registration'),
    path('user/otp', user.user_otp,name='user_otp'),
    path('user/detectstroke', user.user_detect,name='user_detect'),
    path('user/detectstrokes', user.user_detect_details,name='user_detect_details'),
    path('user/dashboard', user.user_dashboard,name='user_dashboard'),
    path('user/myprofile', user.user_myprofile,name='user_myprofile'),


    path('admin/dashboard', admins.admin_dashboard,name='admin_dashboard'),
    path('admin/pendingusers', admins.admin_pendinguser,name='admin_pendinguser'),
    path('admin/manageuser', admins.admin_manageuser,name='admin_manageuser'),
    path('admin/uploaddata', admins.admin_data,name='admin_data'),
    path('admin/viewdata', admins.admin_viewdata,name='admin_viewdata'),
    path('admin/viewdetails', admins.admin_viewdetails,name='admin_viewdetails'),
    path('algorithm/logistic', admins.algorithm_logistic,name='admin_logistic'),
    path('algorithm/svm', admins.algorithm_svm,name='admin_svm'),
    path('algorithm/decision', admins.algorithm_decision,name='admin_decision'),
    path('algorithm/random', admins.algorithm_random,name='admin_random'),
    path('algorithm/knn', admins.algorithm_knn,name='admin_knn'),
    path('algorithm/gradient', admins.algorithm_gradient,name='admin_gradient'),
    path('algorithm/ada', admins.algorithm_ada,name='admin_ada'),
    path('algorithm/xg', admins.algorithm_xg,name='admin_xg'),
    path('KNN_btn', admins.KNN_btn, name='KNN_btn'),
    path('svm_btn', admins.svm_btn, name='svm_btn'),
    path('decision_btn', admins.decision_btn, name='decision_btn'),
    path('random_btn', admins.random_btn, name='random_btn'),
    path('gradient_btn', admins.gradient_btn, name='gradient_btn'),
    path('ada_btn', admins.ada_btn, name='ada_btn'),
    path('xg_btn', admins.xg_btn, name='xg_btn'),
    path('logistic_btn', admins.logistic_btn, name='logistic_btn'),

    path('admin/graph', admins.admin_graph,name='admin_graph'),

    path('admin-rejectbtn/<int:x>',admins.admin_reject_btn, name='admin_reject_btn'),
    path('admin-acceptbtn/<int:x>',admins.admin_accept_btn, name='admin_accept_Btn'),
    path('admin-change-status/<int:id>',admins.Change_Status, name ='change_status'),
    path('admin-delete/<int:id>',admins.Delete_User, name ='delete_user'),
    path('delete-dataset/<int:id>', admins.delete_dataset, name = 'delete_dataset'),
    path('admin_dataset_btn',admins.admin_dataset_btn, name ='admin_dataset_btn'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)