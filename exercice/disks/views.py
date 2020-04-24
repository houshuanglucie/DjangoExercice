from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Track
# from .forms import RechercheForm


def album_list(request):
    albums = Album.objects.all()
    # # form = RechercheForm(request.POST or None)
    # if form.is_valid():
    #     name = form.cleaned_data['Name']
    #     composer = form.cleaned_data['Composer']
    #     milliseconds = form.cleaned_data['Milliseconds']
    #     unit_price = form.cleaned_data['UnitPrice']
    #     return render(request, 'disk.recherche.html', )
    return render(request, 'disks/albumList.html', locals())


def album_info(request, q_id):
    q = get_object_or_404(Album, id=q_id)
    track_list = Track.objects.filter(Album=q)
    # for track in track_list:
    #     duree = track.Milliseconds

    return render(request, 'disks/albumInfo.html', locals())


# def search(request):
#     if request.method == 'POST':
#         q = RechercheForm(request.POST)
#
#     # q = request.GET.get('q')
#         error_msg = ''
#
#         if not q:
#             error_msg = 'Please enter a key word'
#             return render(request, 'disks/errors.html', {'error_msg': error_msg})
#
#         albums = Album.objects.filter(Title__icontains=q)
#         artists = Artist.objects.filter(Name__contains=q)
#         tracks = Track.onjects.filter(Name__contains=q)
#
#     return render(request, 'disks/result.html', locals())

