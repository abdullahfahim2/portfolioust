from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'email')
    fieldsets = (
        ('Basic Info', {
            'fields': ('full_name', 'designation', 'profile_image', 'short_bio', 'about','about_image')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone', 'address', 'cv_file')
        }),
        ('Social Media', {
            'fields': ('facebook', 'linkedin', 'twitter', 'instagram', 'medium')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_description', 'show_hero_mobile', 'hero_button_text')
        }),
    )

@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(CurrentRole)
class CurrentRoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'order')
    list_editable = ('order',)
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'start_year')
    list_filter = ('institution', 'start_year')
    search_fields = ('degree', 'institution', 'field_of_study')

@admin.register(AcademicThesis)
class AcademicThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'university', 'publication_date', 'order', 'is_published')
    list_editable = ('order', 'is_published')
    search_fields = ('title', 'university', 'description')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'currently_working')
    list_filter = ('company', 'currently_working')
    search_fields = ('role', 'company', 'description')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'year')
    list_filter = ('year', 'organization')
    search_fields = ('title', 'organization', 'description')

@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner', 'start_date')
    list_filter = ('partner', 'start_date')
    search_fields = ('title', 'partner', 'description')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_name', 'publish_date', 'is_featured')
    list_filter = ('is_featured', 'publish_date')
    search_fields = ('title', 'media_name')
    list_editable = ('is_featured',)
    
    fields = [
        'profile',
        'title',
        'media_name',
        'media_link',
        'image',
        'publish_date',
        'is_featured'
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk','title',)
    search_fields = ('title', 'description')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published')
    list_filter = ('is_published', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(HomepageSlide)
class HomepageSlideAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order')
    list_editable = ('order',)
    ordering = ('order',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'submitted_at'

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title','caption')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'order')
    list_editable = ('featured', 'order')
    search_fields = ('title', 'description')
    list_filter = ('featured', 'category')
