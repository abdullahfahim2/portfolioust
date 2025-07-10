from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Profile(models.Model):
    # Basic Info
    full_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile/')
    short_bio = models.TextField()
    about = RichTextField()
    about_image = models.ImageField(
        upload_to='profile/about/',
        blank=True,
        null=True,
        help_text="Image specifically for the About section"
    )
    
    # Contact
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    cv_file = models.FileField(upload_to='cvs/', blank=True)
    
    # Social Media
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Innovating Education")
    hero_description = RichTextField(default="About my work...")
    show_hero_mobile = models.BooleanField(default=True)
    hero_button_text = models.CharField(max_length=50, default="Contact Me")

    def get_cv_download_url(self):
        if self.cv_file:
            return reverse('download_cv', kwargs={'pk': self.pk})
        return None

    def __str__(self):
        return self.full_name
    
class Journey(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="My Journey")
    description = RichTextField()
    image = models.ImageField(upload_to='journey/')
    
    def __str__(self):
        return f"{self.profile}'s Journey"
    
class CurrentRole(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='current_roles')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_color = models.CharField(max_length=20, default='blue-700')
    duration = models.CharField(max_length=50)
    duration_color = models.CharField(max_length=20, default='blue-800')
    description = RichTextField()
    button_text = models.CharField(max_length=100, default='Visit Site →')
    button_color = models.CharField(max_length=20, default='blue-800')
    button_link = models.URLField(blank=True)
    secondary_button_text = models.CharField(max_length=100, blank=True)
    secondary_button_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    description = RichTextField(blank=True)
    institution_logo = models.ImageField(upload_to='education/', blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"
    
class AcademicThesis(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='theses')
    title = models.CharField(max_length=200)
    university = models.CharField(max_length=100)
    publication_date = models.DateField()
    thesis_link = models.URLField(blank=True)
    description = RichTextField()
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Academic Theses'
        ordering = ['order']

    def __str__(self):
        return f"{self.title} - {self.university}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    description = RichTextField()
    company_logo = models.ImageField(upload_to='experience/', blank=True)

    def __str__(self):
        return f"{self.role} at {self.company}"

class Achievement(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = RichTextField()
    image = models.ImageField(upload_to='achievements/', blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

class Collaboration(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    partner = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='collaborations/', blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} with {self.partner}"

class Publication(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=200)
    media_name = models.CharField(max_length=100)
    media_link = models.URLField()
    image = models.ImageField(upload_to='publications/')
    publish_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.media_name}"

class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    icon = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = RichTextField()
    featured_image = models.ImageField(upload_to='blog/')
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class HomepageSlide(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slides/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Slide {self.order}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-submitted_at']

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    caption = models.TextField(blank=True)
    alt_text = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=20, help_text="Just the video ID (e.g., 'dQw4w9WgXcQ')")
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}?rel=0"