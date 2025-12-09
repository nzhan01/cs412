# forms.py
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