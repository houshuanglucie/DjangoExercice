from django.shortcuts import render, get_object_or_404
from .models import Album, Track
from .forms import RechercheForm


def album_list(request):
    albums = Album.objects.all()
    form = RechercheForm(request.POST or None)
    if form.is_valid():
        key_word = form.cleaned_data['key_word']
        result = Album.objects.filter(Title__contains=key_word)
        send = True
        return render(request, 'disks/recherche.html', locals())
    return render(request, 'disks/albumList.html', locals())


def album_info(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    track_list = Track.objects.filter(Album=album)
    return render(request, 'disks/albumInfo.html', locals())


# def recherche(request):
#     form = RechercheForm(request.POST or None)
#     if form.is_valid():
#         key_word = form.cleaned_data['key_word']
#         albums = Album.objects.filter(Title__contains=key_word)
#         envoi = True
#
#         return render(request, 'disks/recherche.html', locals())
#     return render(request, 'disks/albumList.html', locals())
