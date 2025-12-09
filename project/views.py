from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, RedirectView, View
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
from django.contrib.auth.forms import UserCreationForm ## NEW
from django.contrib.auth.models import User ## NEW
from django.contrib.auth import login # NEW
from .forms import ProfessorForm

# Create your views here.

#change it class view
def login_view(request):
    """
    Render the custom Google-only login page.
    """
    return render(request, "project/login.html")


class HomePageView( TemplateView):
    '''View for the home page'''
    template_name = 'project/home.html'



class CreateProfessorView( CreateView):
    '''View to create a new professor'''
    model = Professor
    form_class = ProfessorForm
    template_name = 'project/create_professor.html'

    def get_success_url(self):
        return reverse('show_professor', kwargs={'pk': self.object.pk})
    
class RoomRequestCreateView(LoginRequiredMixin, CreateView):
    '''View to create a new room request'''
    model = RoomRequest
    form_class = RoomRequestForm
    template_name = 'project/room_request_form.html'

    def get_form(self, *args, **kwargs):
        """Filter the form so the professor only sees *their* course sections."""
        form = super().get_form(*args, **kwargs)
        professor = self.request.user.professor
        form.fields['course_section'].queryset = professor.coursesection_set.all()
        return form

    def form_valid(self, form):
        request_obj: RoomRequest = form.save(commit=False)
        request_obj.professor = self.request.user.professor

        #check for capacity constraint

        if request_obj.size > request_obj.room.capacity:
            request_obj.status = "Denied"
            request_obj.denial_reason = (
                f"Requested room capacity of {request_obj.room.capacity} is less than class size of {request_obj.size}."
            )
            request_obj.save()

            return redirect(reverse("request_denied", kwargs={'pk': request_obj.id}))
        

        # Else, Get all existing ClassMeetings in that room on the same day
        same_day_meetings = ClassMeeting.objects.filter(
            room=request_obj.room,
            day_of_week=request_obj.day_of_week,
        )

        conflict_meeting = None

        # Manual time overlap check using < comparisons
        for meeting in same_day_meetings:
            if (meeting.start_time < request_obj.end_time and
                meeting.end_time > request_obj.start_time):
                conflict_meeting = meeting
                break

        # If conflict → store denial reason inside RoomRequest
        if conflict_meeting:
            request_obj.status = "Denied"
            request_obj.denial_reason = (
                f"Conflict with {conflict_meeting.course_section} in "
                f"{conflict_meeting.room.building} {conflict_meeting.room.room_number} on {conflict_meeting.day_of_week} "
                f"from {conflict_meeting.start_time} to {conflict_meeting.end_time}."
            )
            request_obj.save()

            return redirect(reverse("request_denied", kwargs={'pk': request_obj.id}))


        # Otherwise → approve and create ClassMeeting
        request_obj.status = "Approved"
        request_obj.denial_reason = ""
        request_obj.save()

        self.object = ClassMeeting.objects.create(
            course_section=request_obj.course_section,
            professor=request_obj.professor,
            room=request_obj.room,
            size=request_obj.size,
            day_of_week=request_obj.day_of_week,
            start_time=request_obj.start_time,
            end_time=request_obj.end_time,
            request=request_obj,
        )

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('show_meeting', kwargs={'pk': self.object.id})

    




    
class RoomRequestDeniedView(TemplateView):
    template_name = 'project/request_denied.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_id = self.kwargs.get('pk')  
        room_request = RoomRequest.objects.get(id=request_id)
        context['room_request'] = room_request
        context['denial_reason'] = room_request.denial_reason
        return context



class CourseListView( ListView):
    '''View to list all courses'''
    model = Course
    template_name = 'project/course_list.html'
    context_object_name = 'courses'

class RoomListView( ListView):
    '''View to list all rooms'''
    model = Room
    template_name = 'project/room_list.html'
    context_object_name = 'rooms'

class ProfessorListView( ListView):
    '''View to list all professors'''
    model = Professor
    template_name = 'project/professor_list.html'
    context_object_name = 'professors'


class CourseView( DetailView):
    '''View to see course info'''
    model = Course
    template_name = 'project/course_view.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sections'] = Course.get_sections(self.object)
        return context
    

class AssignmentFeedView( ListView):
    '''View to see all assignments'''
    model = RoomRequest
    template_name = 'project/assignment_feed.html'
    context_object_name = 'roomrequests'

    def get_queryset(self):
        '''override get_queryset to return all assignments ordered by date'''
        results = super().get_queryset().order_by('-timestamp')
        return results
    
class CourseSectionView( DetailView):
    '''View to see course section info'''
    model = CourseSection
    template_name = 'project/course_section_view.html'
    context_object_name = 'course_section'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetings'] = CourseSection.get_meetings(self.object)
        return context
    
class ClassMeetingView( DetailView):
    '''View to see class meeting info'''
    model = ClassMeeting
    template_name = 'project/class_meeting_view.html'
    context_object_name = 'class_meeting'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfessorDetailView( DetailView):
    '''View to see professor info'''
    model = Professor
    template_name = 'project/professor_view.html'
    context_object_name = 'professor'

    def get_context_data(self, **kwargs):
        '''retrieve all course sections that this professor teaches'''
        context = super().get_context_data(**kwargs)

        context['sections'] = CourseSection.objects.filter(professor=self.object)
        return context
    
class UpdateProfessorView( UpdateView):
    '''View to update professor info'''
    model = Professor
    form_class = UpdateProfessorForm
    template_name = 'project/update_professor.html'

    def get_success_url(self):
        return reverse('show_professor', kwargs={'pk': self.object.pk})
    


class CreateCourseView(CreateView):
    '''view to create a new class '''
    model = Course
    form_class= CourseForm
    template_name= 'project/create_course.html'

    def get_success_url(self):
        return reverse('show_course', kwargs={'pk': self.object.pk})

class RoomDetailView(DetailView):
    ''' View to see room info'''
    model = Room
    template_name = 'project/room_view.html'
    context_object_name = 'room'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetings'] = Room.get_meetings(self.object)
        return context
    
class CreateRoomView(CreateView):
    '''view to create a new room '''
    model = Room
    form_class= RoomForm
    template_name= 'project/create_room.html'

    def get_success_url(self):
        return reverse('show_room', kwargs={'pk': self.object.pk})
    

class CreateCourseSectionView(CreateView):
    '''view to create a new class section '''
    model = CourseSection
    form_class= CourseSectionForm
    template_name= 'project/create_course_section.html'

    def get_form(self, *args, **kwargs):
        """Filter the form so only the specificed course are shown."""
        form = super().get_form(*args, **kwargs)
        course_id = self.kwargs.get('pk')
        form.fields['course'].queryset = Course.objects.filter(id=course_id)
        return form
        
    def get_context_data(self, **kwargs):
        course_id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(id=course_id)
        return context
    

    def get_success_url(self):
        return reverse('show_section', kwargs={'pk': self.object.pk})
    

class DeleteClassMeetingView(DeleteView):
    '''view to delete a class meeting'''
    model = ClassMeeting
    template_name = 'project/delete_class_meeting.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_meeting'] = self.object
        return context
    
    def get_success_url(self):
        return reverse('show_section', kwargs={'pk': self.object.course_section.pk})