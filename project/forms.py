

# file: project/forms.py
 #   Nicholas Zhang
  #  nzhan01@bu.edu
   # created: 12/2/2025
    # py file for the forms of the final project

from django import forms
from .models import *

class ProfessorForm(forms.ModelForm):
    ''' a form for creating a professor'''
    class Meta:
        '''associate the form with the Professor model'''
        model = Professor
        fields = [
            "Firstname",
            "Lastname",
            "email",
            "department",
            "availability"
        ]


    
class RoomRequestForm(forms.ModelForm):
    ''' a form for creating a room request'''
    class Meta:
        '''associate the form with the RoomRequest model'''
        model = RoomRequest
        fields = [
            'course_section',
            'room',
            'size',
            'day_of_week',
            'start_time',
            'end_time',
        ]


class CourseSectionForm(forms.ModelForm):
    ''' a form for creating a course section'''
    class Meta:
        '''associate the form with the CourseSection model'''
        model = CourseSection
        fields = [
            'course',
            'professor',
            'section_code',
        ]

class RoomForm(forms.ModelForm):
    ''' a form for creating a room'''
    class Meta:
        '''associate the form with the Room model'''
        model = Room
        fields = [
            'room_number',
            'room_type',
            'building',
            'capacity',
            'availability',
        ]

class CourseForm(forms.ModelForm):
    ''' a form for creating a course'''
    class Meta:
        '''associate the form with the Course model'''
        model = Course
        fields = [
            'name',
            'code',
            'description',
        ]

class UpdateProfessorForm(forms.ModelForm):
    ''' a form for updating a professor'''
    class Meta:
        '''associate the form with the Professor model'''
        model = Professor
        fields = [
            "Firstname",
            "Lastname",
            "email",
            "department",
            "availability"
        ]