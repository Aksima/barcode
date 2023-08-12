from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = 'Админка ГТО'
    site_title = 'ГТО'
