from django.urls import path,include
from myapp.views import *
urlpatterns=[
#    path('list_employee_old/',list_employee_old),
#   path('add_employee_old/',add_employee_old),
#    path('edit_employee_old/<int:emp_id>/',edit_employee_old),
#    path('del_employee_old/<int:emp_id>/',delete_employee_old),

    #部门数据表路由
    path('add_dep_old/',add_dep_old),
    path('list_dep_old/',list_dep_old),
#    path('del_dep_old/<int:dep_id>/',del_dep_old),
##   path('edit_dep_old/<int:dep_id>/',edit_dep_old),

    #操作团体数据表路由
#    path('add_group_old/',add_group_old),
#    path('list_group_old/',list_group_old),
#    path('del_group_old/<int:group_id>',del_group_old),
#    path('edit_group_old/<int:group_id>/',edit_grou_old),
    #补充数据信息表
#    path('add_employeeinfo_old/',add_employeeinfo_old),
#    path('list_employeeinfo_old/',list_employeeinfo_old),
#    path('del_employeeinfo_old/<int:info_id>/',del_employeeinfo_old),
#    path('edit_employeeinfo_old/<int:info_id>/',edit_employeeinfo_old),
     ]