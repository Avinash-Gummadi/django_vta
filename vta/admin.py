from django.contrib import admin
from .models import UploadQuestion
# Register your models here.
class UploadQuestionAdmin(admin.ModelAdmin):
    list_filter = ['subject', 'answer']
    list_display = ['id','subject','answer']
    class Meta:
        model = UploadQuestion
admin.site.register(UploadQuestion, UploadQuestionAdmin)
