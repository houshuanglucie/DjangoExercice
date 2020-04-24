# from django.contrib import admin
# from .models import Album, Artist, Track
#
#
# class AlbumAdmin(admin.ModelAdmin):
#     list_display = ("name", "pub_date", "active")
#     list_filter = ("pub_date",)
#     search_fields = ("name",)
#     form = AlbumForm
#     exclude = tuple(exclude_fields)
#
#     def __call__(self, request, url):
#         if url == "add_photos" and request.user.is_authenticated() and request.user.is_staff:
#             return self.add_photos(request)
#         return super(AlbumAdmin, self).__call__(request, url)
#
#
#
#
#
