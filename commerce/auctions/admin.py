from django.contrib import admin
from .models import User, Listing, Bids, Comments, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Category)
