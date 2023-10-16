from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('teacherclick', views.teacherclick_view),
    path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
    path('teachersignup', views.teacher_signup_view,name='teachersignup'),
    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
    path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
    path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
    path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


    path('teacher-question', views.teacher_question_view,name='teacher-question'),
    path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
    path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
    path('see-question/<int:pk>', views.see_question_view,name='see-question'),
    path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),


    path('teacher-aptitude-exam', views.teacher_aptitude_exam_view,name='teacher-aptitude-exam'),
    path('teacher-add-aptitude-exam', views.teacher_add_aptitude_exam_view,name='teacher-add-aptitude-exam'),
    path('teacher-view-aptitude-exam', views.teacher_view_aptitude_exam_view,name='teacher-view-aptitude-exam'),
    path('delete-aptitude-exam/<int:pk>', views.delete_aptitude_exam_view,name='delete-aptitude-exam'),
    path('teacher-aptitude-question', views.teacher_aptitude_question_view,name='teacher-aptitude-question'),
    path('teacher-add-aptitude-question', views.teacher_add_aptitude_question_view,name='teacher-add-aptitude-question'),
    path('teacher-view-aptitude-question', views.teacher_view_aptitude_question_view,name='teacher-view-aptitude-question'),
    path('see-aptitude-question/<int:pk>', views.see_aptitude_question_view,name='see-aptitude-question'),
    path('remove-aptitude-question/<int:pk>', views.remove_aptitude_question_view,name='remove-aptitude-question'),

]

