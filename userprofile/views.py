from django.shortcuts import render,redirect,get_object_or_404
from django.http import FileResponse, HttpResponseNotFound
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Or add success message
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'slides': HomepageSlide.objects.filter(is_active=True).order_by('order'),
        'journey' : Journey.objects.filter(profile=profile).first(),
        'educations': Education.objects.all().order_by('-end_year'),
        'theses' : AcademicThesis.objects.filter(is_published=True).order_by('order'),
        'experiences': Experience.objects.filter(profile=profile).order_by('-start_date'),
        'achievements': Achievement.objects.filter(profile=profile).order_by('-year'),
        'roles' : CurrentRole.objects.filter(profile=profile).order_by('order'),
        'collaborations': Collaboration.objects.filter(profile=profile).order_by('-start_date'),
        'publications' : Publication.objects.filter(is_featured=True).order_by('-publish_date'),
        'services': Service.objects.filter(profile=profile),
        'blog_posts': BlogPost.objects.filter(profile=profile, is_published=True).order_by('-published_date')[:3],
        'form': form,
    }
    
    return render(request, 'profile/index.html', context)

def download_cv(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if profile.cv_file:
        response = FileResponse(profile.cv_file.open('rb'))
        response['Content-Disposition'] = f'attachment; filename="{profile.cv_file.name.split("/")[-1]}"'
        return response
    return HttpResponseNotFound("CV not available")

def blog_details(request,slug):
    profile = Profile.objects.first()
    blog = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'profile/blogdetails.html', {'blog':blog,'profile':profile})

def imagegallery(request):
    profile = Profile.objects.first()
    images = GalleryImage.objects.all()
    return render(request, 'profile/image.html', {'images': images,'profile':profile})

def videogallery(request):
    profile = Profile.objects.first()
    videos = Video.objects.all()
    return render(request, 'profile/video.html', {'videos': videos,'profile':profile})

def service(request,pk):
    profile = Profile.objects.first()
    service = Service.objects.get(pk=pk)
    context = {
        'profile': profile,
        'service': service,
    }
    return render(request, 'profile/service.html', context)