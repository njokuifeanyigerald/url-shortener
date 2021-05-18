from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
from .models import DataModel
import random, string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

def home(request):
    try:
        if request.method == 'POST':
            form = DataForm(request.POST )
            if form.is_valid():
                slug = ''.join(random.choice(string.ascii_letters) for x in range(8))
                url  = form.cleaned_data['url']
                new_url = DataModel(user=request.user, url=url, slug=slug)
                new_url.clicked = (new_url.clicked  + 1)
                new_url.save()
                # f'/u/{new_url.slug}
                context = {
                    'form': form,
                    'new_url': f'http://127.0.0.1:8000/u/{new_url.slug}'
                }
                # request.user.urlshort.add(new_url)
                return render(request, 'app/home.html', context)
        form = DataForm(request.POST or None)
        context = {
            'form': form,
            'user': request.user
        }
        return render(request, 'app/home.html', context)
    except request.user == 'AnonymousUser':
        # form = DataForm(request.POST or None)
        # context = {
        #     'form': form,
        #     'user': request.user
        # }
        # return render(request, 'app/home.html', context)
        return JsonResponse('data is not in database', safe=False)


def Redirect(request, slugs):
    try:
        data = DataModel.objects.get(slug=slugs)
    except DataModel.DoesNotExist:
        return JsonResponse('data is not in database', safe=False)


        

    return redirect(data.url)
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
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)

    product = DataModel.objects.get(id=productId)
    print(product)

    if action == 'add':
        product.clicked = (product.clicked + 1)
   
    product.save()
    return JsonResponse('item was added' , safe=False)