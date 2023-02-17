from django.contrib import admin
from .models import *


# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "hero_detail", "hero_logo", "hero_img")


admin.site.register(Hero, HeroAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ("about_title", "about_detail", "about_img")


admin.site.register(About, AboutAdmin)


class ServiceTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "serviceTitle")


admin.site.register(ServiceTitle, ServiceTitleAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_title", "service_detail", "service_icon")


admin.site.register(Service, ServiceAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("contact_phone", "contact_mobile", "contact_phone", "contact_email", "contact_open_hour")


admin.site.register(Contact, ContactAdmin)


class OurClientTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "client_title")


admin.site.register(OurClientTitle, OurClientTitleAdmin)


class OurClientLogoAdmin(admin.ModelAdmin):
    list_display = ("id", "client_logo")


admin.site.register(OurClientLogo, OurClientLogoAdmin)


class OurValueAdmin(admin.ModelAdmin):
    list_display = ("value_title", "value_detail", "value_img")


admin.site.register(OurValue, OurValueAdmin)


class OurValueTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "value_title_main")


admin.site.register(OurValueTitle, OurValueTitleAdmin)


class FeatureTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "feature_title")


admin.site.register(FeatureTitle, FeatureTitleAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ("id", "feature")


admin.site.register(Feature, FeatureAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ("faq_question", "faq_answer")


admin.site.register(Faq, FaqAdmin)
