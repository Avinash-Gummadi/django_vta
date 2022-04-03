from django.contrib import admin
from .models import UploadQuestion, User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_filter = ['username', 'is_faculty', 'person_name']
    list_display = ['username','is_faculty']
    search_fields = ['username', 'person_name']
    class Meta:
        model = User
class UploadQuestionAdmin(admin.ModelAdmin):
    list_filter = ['subject', 'answer']
    list_display = ['id','subject','answer']
    class Meta:
        model = UploadQuestion
admin.site.register(UploadQuestion, UploadQuestionAdmin)
admin.site.register(User,UserAdmin)
