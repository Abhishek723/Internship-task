from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import CreateView
from challenges.models import Challenge,Tags
from challenges.forms import ChallengeForm
from django.shortcuts import redirect, render
from .models import Challenge
# Create your views here.

class ChallengeListView(ListView):

    model = Challenge
    template_name='challenges/challenge_list.html'
    class Meta:
       ordering = ['-end_date']


def challenge_new(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST,request.FILES)
        if form.is_valid():
            challenge = form.save(commit=False)
            # challenge.author = request.user
            challenge.published_date = timezone.now()
            challenge.save()
            return redirect('/')
    else:
        form = ChallengeForm()
    return render(request, 'challenges/registration.html', {'form': form})
    
    
