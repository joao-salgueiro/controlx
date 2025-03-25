from django.shortcuts import render, get_object_or_404

from main.models import GamingController

def home(request):
    return render(request, 'home.html')

def learn_more(request):
    return render(request, 'learn_more.html')

def gamming_controller_detail(request, year):

    controller = get_object_or_404(GamingController, year=year)

    return render(request, 'controller_detail.html', {
        "title": controller.title,
        "description": controller.description,
        "image": controller.image.url
    })


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