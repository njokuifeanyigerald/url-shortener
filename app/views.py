from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
from .models import DataModel
import random, string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
import urllib


# import urllib2
# original_url = 'http://someshorturl/5b2su2'
# response = urllib2.urlopen(original_url)
# # final_url != original_url if redirected
# final_url = response.geturl() 
# # response_code will be 302 for redirects
# response_code = response.getcode()

# if response_code == 302:
#     # redirected so this may a short url
# else:
#     # this is not a short url

# original_url = ''
# response = urllib.urlopen()


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
                    'new_url': f'http://127.0.0.1:8000/u/{new_url.slug}',
                    'clicked': new_url.clicked
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
        # product = DataModel.objects.get(slug=slugs)
        data = DataModel.objects.get(slug=slugs)
        # match = tracking_url.guess_carrier(data)
        # if match:
        #     product.clicked = (product.clicked + 1)   
    except DataModel.DoesNotExist:
        return JsonResponse('data is not in database', safe=False)


        
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