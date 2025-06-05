from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from main.forms import GamingControllerForm
from main.models import GamingController

def home(request):
    return render(request, 'home.html')

def all_posts(request):
    posts = GamingController.objects.all().order_by('-id')

    return render(request, 'main.html', {
        "posts": posts
    })

def learn_more(request):
    return render(request, 'learn_more.html')

def gamming_controller_detail(request, year):

    controller = get_object_or_404(GamingController, year=year)

    return render(request, 'controller_detail.html', {
        "title": controller.title,
        "description": controller.description,
        "image": controller.image.url
    })

@login_required
def new_post(request):
    form = GamingControllerForm
    if request.method == 'POST':
        form = GamingControllerForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
        
        else :
            messages.error(request, 'Error creating post. Please try again.')
            return redirect('new_post')
    return render(request, 'new_post.html', {'form': form})

def listar_sites(request):
    sites = Site.objects.all()
    output = "\n".join([f"ID: {site.id} - Domain: {site.domain}" for site in sites])
    return HttpResponse(f"<pre>{output}</pre>")


def edit_post(request, post_id):
    pass

def delete_post(request, post_id):
    pass

# controllers = {
    #     1970: {
    #          "title": "The Legendary 1987 Gaming Controller",
    #         "description": "This controller revolutionized gaming...",
    #         "image": "1987_controller.jpg"
    #     },

    #      1980: {
    #          "title": "The Legendary 1980 Gaming Controller",
    #         "description": "This controller revolutionized gaming...",
    #         "image": "1987_controller.jpg"
    #     },
    #      1990: {
    #          "title": "The Legendary 1990 Gaming Controller",
    #         "description": "This controller revolutionized gaming...",
    #         "image": "control-night.jpg"
    #     },
    #     2000: {
    #         "title": "The Evolution of Controllers in 2000",
    #         "description": "The 2000s brought new features like...",
    #         "image": "2000_controller.jpg"
    #     }
    # }