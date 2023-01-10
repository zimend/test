from django.contrib import admin
from . import models
from django.utils.html import format_html
from django import forms

# Register your models here.
admin.site.register(models.CategoriesPortfolio)
admin.site.register(models.Testimonial)

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    def avatar_preview(self, obj):
        try:
            return format_html('<div class="img"><img src="{}"  style="width: 50px;height: 50px; border-radius: 50%; border: 4px solid #fff; margin: 0 auto;"/>'.format(obj.avatar.url))
        except:
            return format_html('<div class="img"><img src="https://th.bing.com/th/id/OIP.JZBTJtNF8UwcrOQhh-UgogAAAA?pid=ImgDet&rs=1" style="width: 50px;height: 50px; border-radius: 50%; border: 4px solid #fff; margin: 0 auto;"/>')
        
    avatar_preview.short_description = 'Avatar'
    list_display = ['user','first_name','last_name','gender','is_active','avatar_preview']   
    list_filter = ['gender','is_active']
    list_editable = ['is_active']
    search_fields = ['first_name','last_name','user__username']
    fieldsets = (
        ('Générales', {
           'fields': ('user','bg_wallpaper','is_active')
        }),
        ('Personelles', {
           'fields': ('first_name','last_name','gender','birth_date','location','avatar')
        }),
        ('Contact', {
           'fields': (('email','phone'))
        }),
        ('Reseau Sociaux', {
           'fields': ('facebook','twitter','instagram','github','linkedin'),
           'classes': ('collapse',)
        }),
        ('Professionnelles', {
            'fields': ('title', 'degree','description','bio'),
        }),
    )
        
@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title','category','startPeriode','endPeriode','profile']
    list_filter = ['category','profile']
    fields = ['profile','category','title','place', ('startPeriode','endPeriode')]
    search_fields = ['title']


@admin.register(models.I_Am)
class I_AmAdmin(admin.ModelAdmin):
    
    list_display = ['profile','i_am']
    list_filter = ['profile']
    search_fields = ['i_am','profile__first_name','profile__last_name']


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name','profile','is_active']
    list_filter = ['profile','is_active']
    list_editable = ['is_active'] 
    search_fields = ['name','profile__first_name','profile__last_name'] 

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name','level','profile']


@admin.register(models.Fact)
class FactAdmin(admin.ModelAdmin):

    list_display = ['profile','name','score','is_active']
    list_editable = ['is_active']
    list_filter = ['profile']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['profile','name','mailadress','timestamp']
    search_fields = ['name','mailadress']
    
@admin.register(models.ScreenShotsPortfolio)
class ScreenShotsPortfolioAdmin(admin.ModelAdmin):
    def screen_shot_preview(self, obj):
        return format_html('<div class="img"><img src="{}" style="max-width:50px; max-height:50px; "/>'.format(obj.screen_shot.url))

    screen_shot_preview.short_description = 'Aperçu'
    list_display = ['portfolio','screen_shot','screen_shot_preview']
    
@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
        
    list_display = ['profile','date','name', 'client', 'category']
    list_filter = ['category','profile']
    search_fields = ['profile__first_name','profile__last_name',]
    exclude = ('slug',)
    
@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = ['profile','date','title', 'organism', 'is_active']
    list_filter = ['organism','profile','is_active']
    list_editable = ['is_active']


@admin.register(models.Works)
class WorksAdmin(admin.ModelAdmin):
    
    list_filter = ['resume']
    # list_select_related = ['resume']