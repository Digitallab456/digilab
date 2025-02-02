
from django.urls import path

from .views import *


urlpatterns = [
    # ///////////////////////////// admin ///////////////////////////////////////
    path("", LoginPage.as_view(), name="login"),
    path("addstudent", StudentPage.as_view(), name="addstudent"),
    path("add_faculty",FacultyPage.as_view(),name="add faculty"),
    path("complaint/<int:id>/", ComplaintPage.as_view(),name="complaint"),
    path("editstudent/<int:id>/", StudentEdit.as_view(),name="editstudent"),
    path("removestudent/<int:id>/", StudentRemove.as_view(),name="removestudent"),
    path("editfaculty/<int:id>/", facultyEdit.as_view(),name="editfaculty"),
    path("removefaculty/<int:id>/", facultyRemove.as_view(),name="removefaculty"),
    path("adminhome_page",Adminp.as_view(),name="admin_homepage"),
    path("select_class",select_class.as_view(),name="select_class"),
    path("select_class1",select_class1.as_view(),name="select_class1"),
    path("manage_timetable",manage_timetable.as_view(),name="manage_timetable"),
    path("add_timetable_action",add_timetable_action.as_view(),name="add_timetable_action"),
    path("view_timetable",view_timetable.as_view(),name="view_timetable"),
    path("student",stdp.as_view(),name="student"),
    path("reply",Reply.as_view(),name="reply"),
    path("faculty",Facpage.as_view(),name="faculty"),
    path("postnotification",notificationp.as_view(),name="notification"),
    path("insert_timetable/",insert_timetable.as_view(), name='insert_timetable'),
    path("logout",logout.as_view(), name='logout'),
    

    
    
    

    # //////////////////////////////faculty ////////////////////////////////////////

    path("editstudent", editpage.as_view(), name="edit student"),
    path("homepage", homepage.as_view(), name="faculty_homepage"),
    path("markupload/<int:id>/", markupp.as_view(), name="mark_upload"),
    path("notification", notificationpage.as_view(), name="notification"),
    path("studentList", studentListp.as_view(), name="studentList"),
    path("fac_reg", regpage.as_view(), name="registration"),
    path("post", postcomplaintpage.as_view(), name="post"),
    path("marklist",marklistPage.as_view(), name="marklist"),
    path("logout",logout.as_view(), name='logout'),
    path("f_reply",viewcomplaint.as_view(), name='f_reply'),
    path("task",task.as_view(), name='task'),
    path("taskman",taskman.as_view(), name='taskman'),
    #path("viewcomplaint",.as_view(), name='viewcomplaint'),

   
   
    #//////////////////////////////student//////////////////////////////////////////
    path("postcomplaint", postcomplaintpage.as_view(), name="complaintpage"),
    path("studenthomepage", studpage.as_view(), name="homepage"),
    # path("timetbl", timetblpage.as_view(), name="timetbl"),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('Taskanswerupload/<int:id>/',Taskanswerupload.as_view(),name="Taskanswerupload")
    #////////////////////////////// 
    
    


    
]


