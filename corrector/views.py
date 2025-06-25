from django.shortcuts import render
from textblob import TextBlob

def home(request):
    corrected = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.POST.get('text')
        blob = TextBlob(user_input)
        corrected = str(blob.correct())

    return render(request, 'corrector/home.html', {'input': user_input, 'corrected': corrected})
