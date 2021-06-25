from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
from .models import DataModel
import random, string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
import urllib


def home(request):
    if request.method == 'POST':
        form = DataForm(request.POST )
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for x in range(8))
            url  = form.cleaned_data['url']
            if request.user.is_authenticated:
                new_url = DataModel(user=request.user, url=url, slug=slug)
                new_url.clicked = (new_url.clicked  + 1)
                new_url.save()
                context = {
                'form': form,
                'new_url': f'http://127.0.0.1:8000/u/{new_url.slug}',
                'clicked': new_url.clicked
                }
                return render(request, 'app/home.html', context)
            # else
            new_url = DataModel(url=url, slug=slug)
            new_url.clicked = (new_url.clicked  + 1)
            new_url.save()
            context = {
                'form': form,
                'new_url': f'http://127.0.0.1:8000/u/{new_url.slug}',
                'clicked': new_url.clicked
            }
            return render(request, 'app/home.html', context)
    form = DataForm(request.POST or None)
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'app/home.html', context)

def Redirect(request, slugs):
    try:
        data = DataModel.objects.get(slug=slugs)
        if request.user.is_authenticated:
            data.clicked = (data.clicked + 1)
            data.save()
            return redirect(data.url)
        return redirect(data.url)
    except DataModel.DoesNotExist:
        return JsonResponse('data is not in database', safe=False)

    
    # def urlRedirect(request, slugs):
    # data = UrlData.objects.get(slug=slugs)
    


        
@login_required(login_url='login')
def Info(request):
    try:
        data = DataModel.objects.filter(user=request.user).order_by('-date')
        context = {
            'data': data
        }
        return render(request, 'app/url.html', context)
    except DataModel.DoesNotExist:
        return JsonResponse('you are yet to shorten a url link', safe=False)



def updateItem(request):
    data = json.loads(request.body)
    infoId = data['infoId']
    action = data['action']
    print(action)
    print(infoId)

    product = DataModel.objects.get(id=infoId)
    print(product)

    if action == 'add':
        product.clicked = (product.clicked + 1)
   
    product.save()
    return JsonResponse('item was added' , safe=False)