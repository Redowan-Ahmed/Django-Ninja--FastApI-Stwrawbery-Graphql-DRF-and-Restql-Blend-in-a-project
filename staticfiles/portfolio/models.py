from api.basemodels import BaseModel
from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField


class Project(BaseModel):
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#0a1647", "black", ),
        ("#ff4b1f", "ORange", ),
        ("#ff9068", "ORangeLight", ),
        ("#40c9ff", "Sky", ),
        ("#adfda2", "Litegreen", ),
        ("#e81cff", "Purple", ),
        ("#ffd200", "Yellow", ),
        ("#f7971e", "Golden", ),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    short_description = models.TextField(max_length=500)
    icon = models.FileField(upload_to='icons')
    color_primary = ColorField(samples=COLOR_PALETTE)
    color_secondary = ColorField(samples=COLOR_PALETTE)
    link = models.URLField(blank=True, default='mercegrower.com')

    def __str__(self):
        return self.title


class Skill(BaseModel):
    name = models.CharField(max_length=30)
    percentage = models.IntegerField(blank=True, default=0)
    image = models.FileField(upload_to='skills')

    def __str__(self):
        return self.name


class WorkExperience(BaseModel):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company_url = models.URLField(blank=True)
    present = models.BooleanField(default=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = RichTextField()
    logo = models.ImageField(upload_to='company-logo')
    strock_color = ColorField()

    def __str__(self):
        return self.company_name


class Contact(BaseModel):
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=100)
    massage = models.TextField(max_length=5000)

    def __str__(self):
        return self.email


class SocialMedia(BaseModel):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    icon = models.FileField(upload_to="socialmedia")

    def __str__(self):
        return self.name
