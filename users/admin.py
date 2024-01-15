from django.contrib import admin
from users.models import User

class Users(admin.ModelAdmin):
  list_display = ('id','name', 'email', 'password', 'contato', 'empresa','contato_empresa', 'image')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

admin.site.register(User, Users)