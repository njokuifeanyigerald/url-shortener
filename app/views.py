from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
from .models import DataModel
import random, string
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        form = DataForm(request.POST )
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url  = form.cleaned_data['url']
            new_url = DataModel(url=url, slug=slug)
            new_url.save()
            # request.user.urlshort.add(new_url)
            return redirect(f'/u/{new_url.slug}')
    else:
        form = DataForm(request.POST or None)
    data = DataModel.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'app/home.html', context)

def Redirect(request, slugs):
    try:
        data = DataModel.objects.get(slug=slugs)
    except DataModel.DoesNotExist:
        return JsonResponse('data is not in database', safe=False)


        

    return redirect(data.url)

def Info(request):
    data = DataModel.objects.all()
    context = {
        'data': data
    }
    return render(request, 'app/url.html', context)

