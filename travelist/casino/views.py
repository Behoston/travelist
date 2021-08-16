# Create your views here.
# Create your views here.
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from casino import models


class UsersList(ListView):
    model = models.User


class GiveawayForm(forms.Form):
    user = forms.ModelChoiceField(queryset=models.User.objects.all())
    amount = forms.IntegerField(min_value=1)


def giveaway(request):
    if request.method == 'POST':
        form = GiveawayForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            amount = form.cleaned_data['amount']
            user.balance += amount
            user.save()
            return HttpResponseRedirect('/giveaway/?status=ok')
    else:
        form = GiveawayForm()
    return render(request, 'casino/giveaway.html', {'form': form, 'status': request.GET.get('status') == 'ok'})
