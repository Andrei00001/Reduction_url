import datetime

from django.contrib import admin

from admin_panel.models import URL
from django.utils.translation import gettext_lazy as _

# Register your models here.

register_admin = admin.site.register


class FilterURL(admin.SimpleListFilter):
    title = "Expired at"
    parameter_name = "is expired"

    def lookups(self, request, model_admin):
        return ('is_expired', _('Is expired')),

    def queryset(self, request, queryset):
        if self.value() != 'is_expired':
            return None
        return queryset.filter(expired_at__lt=datetime.date.today())


class URLAdmin(admin.ModelAdmin):
    model = URL
    ordering = ['id']
    list_display = ['url', 'reduction_url', 'expired_at']
    fields = ['url', 'reduction_url', 'expired_at']
    list_filter = [FilterURL, ]
    actions = ['delete_all_expired']

    @admin.action(description='Delete all expired')
    def delete_all_expired(self, request, queryset):
        queryset.filter(expired_at__lt=datetime.date.today()).delete()


register_admin(URL, URLAdmin)
