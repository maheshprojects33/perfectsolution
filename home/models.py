from django.db import models


# Create your models here.
class Hero(models.Model):
    hero_title = models.CharField(max_length=50)
    hero_detail = models.TextField()
    hero_img = models.ImageField(upload_to="hero", blank=True, default="hero/hero-img.png")
    hero_logo = models.ImageField(upload_to="hero", blank=True)


class About(models.Model):
    about_title = models.TextField()
    about_detail = models.TextField()
    about_img = models.ImageField(upload_to="about", blank=True)


class ServiceTitle(models.Model):
    serviceTitle = models.CharField(max_length=100)


class Service(models.Model):
    service_icon = models.ImageField(upload_to="service", blank=True)
    service_title = models.CharField(max_length=50)
    service_detail = models.TextField()


class Contact(models.Model):
    contact_address = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_mobile = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField()
    contact_open_hour = models.TextField()


class OurClientTitle(models.Model):
    client_title = models.CharField(max_length=50)


class OurClientLogo(models.Model):
    client_logo = models.ImageField(upload_to="client_logo")


class OurValue(models.Model):
    value_img = models.ImageField(upload_to="our_values")
    value_title = models.CharField(max_length=30)
    value_detail = models.TextField()


class OurValueTitle(models.Model):
    value_title_main = models.CharField(max_length=50)


class FeatureTitle(models.Model):
    feature_title = models.CharField(max_length=50)


class Feature(models.Model):
    feature = models.CharField(max_length=50)

class Faq(models.Model):
    faq_question = models.CharField(max_length=200)
    faq_answer = models.TextField()
