from django.contrib import admin
from .models import Project, Contact, Skill, SocialMedia, WorkExperience
from django.utils.html import format_html


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    actions_on_bottom = True
    list_display_links = ['full_name','email']
    actions_on_top = True
    list_per_page = 30
    search_fields = ['full_name', 'email']
    save_on_top = True
    save_as_continue = True
    save_as = True
    list_max_show_all = 100
    date_hierarchy = "created_at"
    list_filter = ['created_at', 'updated_at']

class SkillAdmin(admin.ModelAdmin):
    list_display = ('Logo', 'name','created_at')
    actions_on_bottom = True
    list_display_links = ['Logo','name']
    actions_on_top = True
    list_per_page = 30
    search_fields = ['name']
    save_on_top = True
    save_as_continue = True
    save_as = True
    list_max_show_all = 100
    date_hierarchy = "created_at"
    list_filter = ['created_at', 'updated_at']
    fields = ['name','Image_preview', 'image','percentage']
    readonly_fields = ('Image_preview',)

    def Logo(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="50px" height="50px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

    def Image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="200px" height="200px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('Icon', 'name','url','created_at')
    actions_on_bottom = True
    list_display_links = ['Icon','name']
    actions_on_top = True
    list_per_page = 30
    search_fields = ['name','url']
    save_on_top = True
    list_editable = ['url']
    save_as_continue = True
    save_as = True
    list_max_show_all = 100
    date_hierarchy = "created_at"
    list_filter = ['created_at', 'updated_at']
    fields = ['name','Icon_preview', 'icon','url']
    readonly_fields = ('Icon_preview',)

    def Icon(self, obj):
        if obj.icon:
            return format_html(f'<img src="{obj.icon.url}" width="50px" height="50px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

    def Icon_preview(self, obj):
        if obj.icon:
            return format_html(f'<img src="{obj.icon.url}" width="200px" height="200px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Thumbnail', 'title','color_primary','link','created_at')
    actions_on_bottom = True
    list_display_links = ['Thumbnail','title']
    actions_on_top = True
    list_per_page = 30
    search_fields = ['title']
    save_on_top = True
    save_as_continue = True
    save_as = True
    list_editable = ['link', 'color_primary']
    list_max_show_all = 100
    date_hierarchy = "created_at"
    list_filter = ['created_at', 'updated_at']
    fields = ['title','description', 'short_description','thumbnail_preview', 'icon','color_primary', 'color_secondary','link']
    readonly_fields = ('thumbnail_preview',)

    def Thumbnail(self, obj):
        if obj.icon:
            return format_html(f'<img src="{obj.icon.url}" width="50px" height="50px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

    def thumbnail_preview(self, obj):
        if obj.icon:
            return format_html(f'<img src="{obj.icon.url}" width="200px" height="200px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('Logo', 'company_name','position','present','start_date','created_at')
    actions_on_bottom = True
    list_display_links = ['Logo','company_name']
    actions_on_top = True
    list_per_page = 30
    search_fields = ['company_name', 'position']
    save_on_top = True
    save_as_continue = True
    save_as = True
    list_editable = ['present']
    list_max_show_all = 100
    date_hierarchy = "created_at"
    list_filter = ['created_at', 'updated_at','present','start_date','end_date']
    fields = ['company_name','company_url','position','present', 'description','logo_preview', 'logo','start_date', 'end_date','strock_color']
    readonly_fields = ('logo_preview',)

    def Logo(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" width="50px" height="50px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(f'<img src="{obj.logo.url}" width="200px" height="200px" />')
        return format_html(f'<div style="display:flex;flex-wrap:wrap;align-content:center;justify-content:center;align-items:center;width:50px;font-size:10px;height:50px;background:red;color: white;border-radius: 3px;"> No Image </div>')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
