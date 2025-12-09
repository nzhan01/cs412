from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Room)
admin.site.register(CourseSection)
admin.site.register(ClassMeeting)
admin.site.register(RoomRequest)
