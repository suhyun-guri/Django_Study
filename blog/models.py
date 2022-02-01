from django.db import models
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank = True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m%d/', blank = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author 추후 작성
    
    #제목나오도록 함수 생성
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    #파일명 가져오기
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    #확장자 가져오기
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]