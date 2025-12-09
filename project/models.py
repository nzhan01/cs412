# file: project/models.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 12/1/2025
# models file containing all the models for the final project app


from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

''' Choices for days of the week'''
DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
]

class Course(models.Model):
    '''model for course information'''

    name = models.TextField()
    code = models.TextField()
    description = models.TextField( default='' )
    credits = models.IntegerField(default= 4)

    def __str__(self):
        '''return a string representation of the Course'''
        return f'{self.code} - {self.name}'
    

    def get_sections(self):
        '''return all sections for this course'''
        return CourseSection.objects.filter(course=self)

class Professor(models.Model):
    '''model for professor information'''
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    Firstname = models.TextField()
    Lastname = models.TextField()
    email = models.TextField()
    department = models.TextField()
    availability = models.TextField()
    def __str__(self):
        '''return a string representation of the Professor'''
        return f'{self.Firstname} {self.Lastname}'


class Room(models.Model):
    '''model for room information'''

    room_number = models.TextField()
    room_type = models.TextField()
    building = models.TextField()
    capacity = models.IntegerField()
    availability = models.TextField()

    def __str__(self):
        '''return a string representation of the Room'''
        return f'{self.building} {self.room_number}'
    
    def get_meetings(self):
        '''return all class meetings for this room'''
        return ClassMeeting.objects.filter(room=self)

class CourseSection(models.Model):
    '''model for course section information'''

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    section_code = models.TextField()

    def __str__(self):
        '''return a string representation of the CourseSection'''
        return f'{self.course.code} - {self.section_code}'
    
    def get_meetings(self):
        '''return all class meetings for this course section'''
        return ClassMeeting.objects.filter(course_section=self)

class ClassMeeting(models.Model):
    '''model for a single class meeting information'''

    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    size = models.IntegerField()
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    request = models.ForeignKey('RoomRequest', null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        '''return a string representation of the ClassMeeting'''
        return f'{self.course_section} in {self.room.room_number} with {self.professor.Lastname} on {self.day_of_week} from {self.start_time} to {self.end_time}'
    

class RoomRequest(models.Model):
    '''model for a room request'''
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)
    start_time = models.TimeField(default='00:00')
    end_time = models.TimeField(default='00:00')
    timestamp = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = [
        ('Approved','Approved'),
        ('Denied','Denied'),
        ('Pending','Pending')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    denial_reason = models.TextField(blank=True, default='')

    def __str__(self):
        '''return a string representation of the RoomRequest'''
        return f'Request for {self.course_section} in {self.room.room_number} with {self.professor.Lastname} on {self.day_of_week} from {self.start_time} to {self.end_time} - Status: {self.status}'