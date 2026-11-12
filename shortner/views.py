import uuid
from django.shortcuts import get_object_or_404, redirect, render
from shortner.models import ShortURL

def home(request):
    short_url_obj = None
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            short_code = str(uuid.uuid4())[:6]
            while ShortURL.objects.filter(short_code=short_code).exists():
                short_code = str(uuid.uuid4())[:6]
            short_url_obj = ShortURL.objects.create(
                long_url=long_url, short_code=short_code
            )
    context = {'short_url_obj': short_url_obj}
    return render(request, 'shortner/home.html', context)

def redirect_url(request, short_code):
    url_obj = get_object_or_404(ShortURL, short_code=short_code)
    url_obj.clicks += 1
    url_obj.save()
    return redirect(url_obj.long_url)

def update_url(request, pk):
    url_obj = get_object_or_404(ShortURL, id=pk)
    if request.method == 'POST':
        new_long_url = request.POST.get('long_url')
        if new_long_url:
            url_obj.long_url = new_long_url
            url_obj.save()
            return redirect('home')
    context = {'url_obj': url_obj}
    return render(request, 'shortner/update.html', context)