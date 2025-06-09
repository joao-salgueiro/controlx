from django.shortcuts import get_object_or_404, render

from texts.models import LocalTexts

# Create your views here.
def learn_more(request):
    text = get_object_or_404(LocalTexts, key='learn_more_text')
    return render(request, 'learn_more.html', {
        'text': text.text
    })