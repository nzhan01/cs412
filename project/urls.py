
# file: project/urls.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 12/2/2025
# models file containing all the urls for the final app

from django.urls import path


from .views import * 
from django.contrib.auth import views as auth_views 
from django.urls import  include



urlpatterns =[
    path('', HomePageView.as_view(), name='home'),
    path('course/list', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>', CourseView.as_view(), name='show_course'),
    path('course/create', CreateCourseView.as_view(), name='create_course'),
    path('course/section/<int:pk>', CourseSectionView.as_view(), name='show_section'),
    path('course/<int:pk>/section/create', CreateCourseSectionView.as_view(), name='create_section'),
    path('course/meeting/<int:pk>', ClassMeetingView.as_view(), name='show_meeting'),
    path('course/section/<int:pk>/meeting/delete', DeleteClassMeetingView.as_view(), name='delete_meeting'),
    path('professor/<int:pk>', ProfessorDetailView.as_view(), name='show_professor'),
    path('professor/list', ProfessorListView.as_view(), name='professor_list'),
    path('professor/<int:pk>/update', UpdateProfessorView.as_view(), name='update_professor'),
    path('professor/create', CreateProfessorView.as_view(), name='create_professor'),
    path('login/', login_view, name="login"),   
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path("accounts/", include("allauth.urls")), # Google OAuth routes
    path('room/list', RoomListView.as_view(), name='room_list'),
    path('room/create', CreateRoomView.as_view(), name='create_room'),
    path('room/<int:pk>', RoomDetailView.as_view(), name='show_room'),
    path('room/request', RoomRequestCreateView.as_view(), name="create_room_request"),
    path('room/request/<int:pk>/denied', RoomRequestDeniedView.as_view(), name='request_denied'),
    path('feed/', AssignmentFeedView.as_view(), name='feed')
]