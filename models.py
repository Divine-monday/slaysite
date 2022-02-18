from django.db import models
from PIL import Image

# Create your models here.
# ****************** Models for the home page ****************** #
class SearchBox(models.Model):
    searchbox_title = models.CharField(max_length=1000, blank=True)
    searchbox_url = models.URLField()
    def __str__(self):
        return self.searchbox_url


class HomeIcons(models.Model):
    homeicon_title =  models.CharField(max_length=50)
    homeicon_url = models.URLField()
    homeicon_file = models.ImageField(default='default.png', upload_to="home_icons")

    def __str__(self):
        return self.homeicon_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.homeicon_file.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.homeicon_file.path)
            #Rememberance: the image may likely be resized down to 200 or 220. TAKE_NOTE


# ****************** Models for the main page  ****************** #
class SlaysiteIcons(models.Model):
    slaysiteicon_file = models.ImageField(upload_to="slaysite_icons")
    slaysiteicon_title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.slaysiteicon_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.slaysiteicon_file.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.slaysiteicon_file.path)


class News_article(models.Model):
    news_article_head = models.CharField(max_length=50, blank=True)
    news_article_title = models.CharField(max_length=100)
    news_article_url = models.URLField()
    news_article_file = models.ImageField(default='newsdefault.png', blank=True, upload_to = "News_article")

    def __str__(self):
        return f'Title Head: {self.news_article_head}, Title: {self.news_article_title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.news_article_file.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.news_article_file.path)

# Web models
class Web(models.Model):
    web_title =  models.CharField(max_length=100)
    web_url = models.URLField()
    web_file = models.ImageField(default='default.png', blank=True, upload_to="web_icons")

    def __str__(self):
        return self.web_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.web_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.web_file.path)



# # Koinoniavid Video_models
class KoinoniaVideo(models.Model):
    koinoniavid_title =  models.CharField(max_length=100)
    koinoniavid_video = models.FileField(upload_to="Koinoniavid/%y", default="")
    koinoniavid_file = models.ImageField(default='default.png', blank=True, upload_to="Koinoniavid")

    def __str__(self):
        return self.koinoniavid_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.koinoniavid_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.koinoniavid_file.path)



# Koinonia models would be here
class Koinonia(models.Model):
    koinonia_title =  models.CharField(max_length=100)
    koinonia_url = models.URLField()
    koinonia_file = models.ImageField(default='default.png', blank=True, upload_to="koinonia_icons")

    def __str__(self):
        return self.koinonia_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.koinonia_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.koinonia_file.path)


# Koinnonia Apostle Michael O
class KoinoniaVidAMO(models.Model):
    koinoniavidamo_title =  models.CharField(max_length=100)
    koinoniavidamo_video = models.FileField(upload_to="Koinoniavidamo/%y", default="")
    koinoniavidamo_file = models.ImageField(default='default.png', blank=True, upload_to="Koinoniavidamo")

    def __str__(self):
        return self.koinoniavid_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.koinoniavidamo_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.koinoniavidamo_file.path)



# KoinoniaAMO models would be here
class KoinoniaAMO(models.Model):
    koinoniaamo_title =  models.CharField(max_length=100)
    koinoniaamo_url = models.URLField()
    koinoniaamo_file = models.ImageField(default='default.png', blank=True, upload_to="koinoniaamo_icons")

    def __str__(self):
        return self.koinoniaamo_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.koinoniaamo_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.koinoniaamo_file.path)



# # Koinonia_models
class Koinonia_Others(models.Model):
    koothers_title =  models.CharField(max_length=100)
    koothers_url = models.URLField()
    koothers_file = models.ImageField(default='default.png', blank=True, upload_to="koothers_icons")

    def __str__(self):
        return self.koothers_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.koothers_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.koothers_file.path)


# Hillsong models would be here
class Hillsong(models.Model):
    hillsong_title =  models.CharField(max_length=100)
    hillsong_url = models.URLField()
    hillsong_file = models.ImageField(default='default.png', blank=True, upload_to="hillsong_icons")

    def __str__(self):
        return self.hillsong_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.hillsong_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.hillsong_file.path)


# Gospel model
class Gospel(models.Model):
    gospel_title =  models.CharField(max_length=100)
    gospel_video = models.FileField(upload_to="Gospel/%y", default="")
    gospel_file = models.ImageField(default='default.png', blank=True, upload_to="Gospel")

    def __str__(self):
        return self.gospel_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.gospel_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.gospel_file.path)



# Amazon models
class Amazon(models.Model):
    amazon_title =  models.CharField(max_length=100)
    amazon_url = models.URLField()
    amazon_file = models.ImageField(default='default.png', blank=True, upload_to="amazon_icons")

    def __str__(self):
        return self.amazon_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.amazon_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.amazon_file.path)


# Apps models
class Apps(models.Model):
    aps_title =  models.CharField(max_length=100)
    aps_url = models.URLField()
    aps_file = models.ImageField(default='default.png', blank=True, upload_to="apps_icons")

    def __str__(self):
        return self.aps_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.aps_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.aps_file.path)

# Arts models
class Arts(models.Model):
    art_title =  models.CharField(max_length=100)
    art_url = models.URLField()
    art_file = models.ImageField(default='default.png', blank=True, upload_to="arts_icons")

    def __str__(self):
        return self.art_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.art_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.art_file.path)

# Audio_book models
class AudioBook(models.Model):
    audiobook_title =  models.CharField(max_length=100)
    audiobook_url = models.URLField()
    audiobook_file = models.ImageField(default='default.png', blank=True, upload_to="audiobook_icons")

    def __str__(self):
        return self.audiobook_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.audiobook_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.audiobook_file.path)

# Automobiles models
class AutoMobiles(models.Model):
    automobiles_title =  models.CharField(max_length=100)
    automobiles_url = models.URLField()
    automobiles_file = models.ImageField(default='default.png', blank=True, upload_to="automobiles_icons")

    def __str__(self):
        return self.automobiles_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.automobiles_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.automobiles_file.path)


# Banking models
class Banking(models.Model):
    banking_title =  models.CharField(max_length=100)
    banking_url = models.URLField()
    banking_file = models.ImageField(default='default.png', blank=True, upload_to="banking_icons")

    def __str__(self):
        return self.banking_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.banking_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.banking_file.path)

# Bcosmetics models
class Bcosmetics(models.Model):
    bcosmetics_title =  models.CharField(max_length=100)
    bcosmetics_url = models.URLField()
    bcosmetics_file = models.ImageField(default='default.png', blank=True, upload_to="bcosmetics_icons")

    def __str__(self):
        return self.bcosmetics_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.bcosmetics_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.bcosmetics_file.path)

# Birthday models
class Birthday(models.Model):
    birthday_title =  models.CharField(max_length=100)
    birthday_url = models.URLField()
    birthday_file = models.ImageField(default='default.png', blank=True, upload_to="birthday_icons")

    def __str__(self):
        return self.birthday_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.birthday_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.birthday_file.path)

# Books models
class Books(models.Model):
    books_title =  models.CharField(max_length=100)
    books_url = models.URLField()
    books_file = models.ImageField(default='default.png', blank=True, upload_to="books_icons")

    def __str__(self):
        return self.books_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.books_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.books_file.path)

# Browsers models
class Browsers(models.Model):
    browsers_title =  models.CharField(max_length=100)
    browsers_url = models.URLField()
    browsers_file = models.ImageField(default='default.png', blank=True, upload_to="browsers_icons")

    def __str__(self):
        return self.browsers_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.browsers_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.browsers_file.path)


# # Cartoons models
class Cartoons(models.Model):
    cartoons_title =  models.CharField(max_length=100)
    cartoons_url = models.URLField()
    cartoons_file = models.ImageField(default='default.png', blank=True, upload_to="cartoons_icons")

    def __str__(self):
        return self.cartoons_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cartoons_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.cartoons_file.path)

# # Cfood models
class Cfood(models.Model):
    cfood_title =  models.CharField(max_length=100)
    cfood_url = models.URLField()
    cfood_file = models.ImageField(default='default.png', blank=True, upload_to="cfood_icons")

    def __str__(self):
        return self.cfood_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cfood_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.cfood_file.path)


# # Crypto models
class Crypto(models.Model):
    crypto_title =  models.CharField(max_length=100)
    crypto_url = models.URLField()
    crypto_file = models.ImageField(default='default.png', blank=True, upload_to="crypto_icons")

    def __str__(self):
        return self.crypto_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.crypto_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.crypto_file.path)


# # Disney models
class Disney(models.Model):
    disney_title =  models.CharField(max_length=100)
    disney_url = models.URLField()
    disney_file = models.ImageField(default='default.png', blank=True, upload_to="disney_icons")

    def __str__(self):
        return self.disney_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.disney_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.disney_file.path)


# # Education models
class Education(models.Model):
    education_title =  models.CharField(max_length=100)
    education_url = models.URLField()
    education_file = models.ImageField(default='default.png', blank=True, upload_to="education_icons")

    def __str__(self):
        return self.education_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.education_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.education_file.path)

# # Entertainment models
class Entertainment(models.Model):
    entertainment_title =  models.CharField(max_length=100)
    entertainment_url = models.URLField()
    entertainment_file = models.ImageField(default='default.png', blank=True, upload_to="entertainment_icons")

    def __str__(self):
        return self.entertainment_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.entertainment_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.entertainment_file.path)

# # Fashion models
class Fashion(models.Model):
    fashion_title =  models.CharField(max_length=100)
    fashion_url = models.URLField()
    fashion_file = models.ImageField(default='default.png', blank=True, upload_to="fashion_icons")

    def __str__(self):
        return self.fashion_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.fashion_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.fashion_file.path)

# # Gaming models
class Gaming(models.Model):
    gaming_title =  models.CharField(max_length=100)
    gaming_url = models.URLField()
    gaming_file = models.ImageField(default='default.png', blank=True, upload_to="gaming_icons")

    def __str__(self):
        return self.gaming_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.gaming_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.gaming_file.path)


# # Gdp models
class Gdp(models.Model):
    gdp_title =  models.CharField(max_length=100)
    gdp_url = models.URLField()
    gdp_file = models.ImageField(default='default.png', blank=True, upload_to="gdp_icons")

    def __str__(self):
        return self.gdp_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.gdp_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.gdp_file.path)


# # Google models
class Google(models.Model):
    google_title =  models.CharField(max_length=100)
    google_url = models.URLField()
    google_file = models.ImageField(default='default.png', blank=True, upload_to="google_icons")

    def __str__(self):
        return self.google_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.google_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.google_file.path)


# # Graphics Design models
class Gdesign(models.Model):
    gdesign_title =  models.CharField(max_length=100)
    gdesign_url = models.URLField()
    gdesign_file = models.ImageField(default='default.png', blank=True, upload_to="gdesign_icons")

    def __str__(self):
        return self.gdesign_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.gdesign_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.gdesign_file.path)


# # Health Care models
class HealthCare(models.Model):
    healthcare_title =  models.CharField(max_length=100)
    healthcare_url = models.URLField()
    healthcare_file = models.ImageField(default='default.png', blank=True, upload_to="healthcare_icons")

    def __str__(self):
        return self.healthcare_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.healthcare_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.healthcare_file.path)


# # ICT models
class ICT(models.Model):
    ict_title =  models.CharField(max_length=100)
    ict_url = models.URLField()
    ict_file = models.ImageField(default='default.png', blank=True, upload_to="ict_icons")

    def __str__(self):
        return self.ict_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.ict_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.ict_file.path)


# # Images models
class Images(models.Model):
    images_title =  models.CharField(max_length=100)
    images_url = models.URLField()
    images_file = models.ImageField(default='default.png', blank=True, upload_to="images_icons")

    def __str__(self):
        return self.images_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.images_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.images_file.path)



# # Jobs models
class Jobs(models.Model):
    jobs_title =  models.CharField(max_length=100)
    jobs_url = models.URLField()
    jobs_file = models.ImageField(default='default.png', blank=True, upload_to="jobs_icons")

    def __str__(self):
        return self.jobs_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.jobs_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.jobs_file.path)


# # Microsoft models
class Microsoft(models.Model):
    microsoft_title =  models.CharField(max_length=100)
    microsoft_url = models.URLField()
    microsoft_file = models.ImageField(default='default.png', blank=True, upload_to="microsoft_icons")

    def __str__(self):
        return self.microsoft_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.microsoft_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.microsoft_file.path)


# # Movies models
class Movies(models.Model):
    movies_title =  models.CharField(max_length=100)
    movies_url = models.URLField()
    movies_file = models.ImageField(default='default.png', blank=True, upload_to="movies_icons")

    def __str__(self):
        return self.movies_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.movies_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.movies_file.path)


# # Music models
class Music(models.Model):
    music_title =  models.CharField(max_length=100)
    music_url = models.URLField()
    music_file = models.ImageField(default='default.png', blank=True, upload_to="music_icons")

    def __str__(self):
        return self.music_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.music_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.music_file.path)


# # News models
class News(models.Model):
    news_title =  models.CharField(max_length=100)
    news_url = models.URLField()
    news_file = models.ImageField(default='default.png', blank=True, upload_to="news_icons")

    def __str__(self):
        return self.news_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.news_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.news_file.path)


# # Online Dating models
class OnlineDating(models.Model):
    online_dating_title =  models.CharField(max_length=100)
    online_dating_url = models.URLField()
    online_dating_file = models.ImageField(default='default.png', blank=True, upload_to="online_dating_icons")

    def __str__(self):
        return self.online_dating_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.online_dating_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.online_dating_file.path)


# # Online Payment models
class OnlinePayment(models.Model):
    online_payment_title =  models.CharField(max_length=100)
    online_payment_url = models.URLField()
    online_payment_file = models.ImageField(default='default.png', blank=True, upload_to="online_payment_icons")

    def __str__(self):
        return self.online_payment_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.online_payment_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.online_payment_file.path)


# # Opera models
class Opera(models.Model):
    opera_title =  models.CharField(max_length=100)
    opera_url = models.URLField()
    opera_file = models.ImageField(default='default.png', blank=True, upload_to="opera_icons")

    def __str__(self):
        return self.opera_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.opera_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.opera_file.path)


# # Pdfs models
class Pdfs(models.Model):
    pdfs_title =  models.CharField(max_length=100)
    pdfs_url = models.URLField()
    pdfs_file = models.ImageField(default='default.png', blank=True, upload_to="pdfs_icons")

    def __str__(self):
        return self.pdfs_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.pdfs_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.pdfs_file.path)


# # Programming models
class Programming(models.Model):
    program_title =  models.CharField(max_length=100)
    program_url = models.URLField()
    program_file = models.ImageField(default='default.png', blank=True, upload_to="programming_icons")

    def __str__(self):
        return self.program_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.program_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.program_file.path)


# # Shopping models
class Shopping(models.Model):
    shopping_title =  models.CharField(max_length=100)
    shopping_url = models.URLField()
    shopping_file = models.ImageField(default='default.png', blank=True, upload_to="shopping_icons")

    def __str__(self):
        return self.shopping_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.shopping_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.shopping_file.path)


# # Social models
class Social(models.Model):
    social_title =  models.CharField(max_length=100)
    social_url = models.URLField()
    social_file = models.ImageField(default='default.png', blank=True, upload_to="social_icons")

    def __str__(self):
        return self.social_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.social_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.social_file.path)


# # Sports models
class Sports(models.Model):
    sports_title =  models.CharField(max_length=100)
    sports_url = models.URLField()
    sports_file = models.ImageField(default='default.png', blank=True, upload_to="sports_icons")

    def __str__(self):
        return self.sports_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.sports_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.sports_file.path)


# # Travel models
class Travel(models.Model):
    travel_title =  models.CharField(max_length=100)
    travel_url = models.URLField()
    travel_file = models.ImageField(default='default.png', blank=True, upload_to="travel_icons")

    def __str__(self):
        return self.travel_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.travel_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.travel_file.path)


# # Tv shows models
class Tv_Shows(models.Model):
    tvshows_title =  models.CharField(max_length=100)
    tvshows_url = models.URLField()
    tvshows_file = models.ImageField(default='default.png', blank=True, upload_to="tvshows_icons")

    def __str__(self):
        return self.tvshows_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.tvshows_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.tvshows_file.path)


# # Videos models
class Videos(models.Model):
    videos_title =  models.CharField(max_length=100)
    videos_url = models.URLField()
    videos_file = models.ImageField(default='default.png', blank=True, upload_to="videos_icons")

    def __str__(self):
        return self.videos_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.videos_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.videos_file.path)


# # Wallet models
class Wallet(models.Model):
    wallet_title =  models.CharField(max_length=100)
    wallet_url = models.URLField()
    wallet_file = models.ImageField(default='default.png', blank=True, upload_to="wallet_icons")

    def __str__(self):
        return self.wallet_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.wallet_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.wallet_file.path)


# # Weather models
class Weather(models.Model):
    weather_title =  models.CharField(max_length=100)
    weather_url = models.URLField()
    weather_file = models.ImageField(default='default.png', blank=True, upload_to="weather_icons")

    def __str__(self):
        return self.weather_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.weather_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.weather_file.path)


# # Web hosting models
class WebHosting(models.Model):
    webhost_title =  models.CharField(max_length=100)
    webhost_url = models.URLField()
    webhost_file = models.ImageField(default='default.png', blank=True, upload_to="webhost_icons")

    def __str__(self):
        return self.webhost_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.webhost_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.webhost_file.path)



# # Wikipedia models
class Wikipedia(models.Model):
    wikipedia_title =  models.CharField(max_length=100)
    wikipedia_url = models.URLField()
    wikipedia_file = models.ImageField(default='default.png', blank=True, upload_to="wikipedia_icons")

    def __str__(self):
        return self.wikipedia_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.wikipedia_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.wikipedia_file.path)        


# # WWE models
class WWE(models.Model):
    wwe_title =  models.CharField(max_length=100)
    wwe_url = models.URLField()
    wwe_file = models.ImageField(default='default.png', blank=True, upload_to="wwe_icons")

    def __str__(self):
        return self.wwe_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.wwe_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.wwe_file.path)          


# # Covid_19 models
class Covid_19(models.Model):
    covid19_title =  models.CharField(max_length=100)
    covid19_url = models.URLField()
    covid19_file = models.ImageField(default='default.png', blank=True, upload_to="covid19_icons")

    def __str__(self):
        return self.covid19_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.covid19_file.path)
        if img.height > 50 or img.width > 50:
            output_size = (50, 50)
            img.thumbnail(output_size)
            img.save(self.covid19_file.path)         


# This is for the about page model for the background image there. i want to resize the image because its to large.
# ****************** Models for the about page  ****************** #
class AboutIcons(models.Model):
    abouticon_file = models.ImageField(upload_to="aboutpage_icons")
    abouticon_title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.abouticon_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.abouticon_file.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.abouticon_file.path)





# This is for the tour page model for the background image there. i want to resize the image because its to large.
# ****************** Models for the tour page  ****************** #

# TourAll models
class TourAll(models.Model):
    tourall_title =  models.CharField(max_length=100)
    tourall_video = models.FileField(upload_to="Tourall/%y", default="")
    tourall_file = models.ImageField(default='default.png', blank=True, upload_to="Tourall")

    def __str__(self):
        return self.tourall_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.tourall_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.tourall_file.path)


# # TourMovies models
class TourMovies(models.Model):
    tourmovies_title =  models.CharField(max_length=100)
    tourmovies_video = models.FileField(upload_to="Tourmovies/%y", default="")
    tourmovies_file = models.ImageField(default='default.png', blank=True, upload_to="Tourmovies")

    def __str__(self):
        return self.tourmovies_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.tourmovies_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.tourmovies_file.path)


# # TourMusics  models
class TourMusics(models.Model):
    tourmusics_title =  models.CharField(max_length=100)
    tourmusics_video = models.FileField(upload_to="Tourmusics/%y", default="")
    tourmusics_file = models.ImageField(default='default.png', blank=True, upload_to="Tourmusics")

    def __str__(self):
        return self.tourmusics_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.tourmusics_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.tourmusics_file.path)



# # TourSports models
class TourSports(models.Model):
    toursports_title =  models.CharField(max_length=100)
    toursports_video = models.FileField(upload_to="Toursports/%y", default="")
    toursports_file = models.ImageField(default='default.png', blank=True, upload_to="Toursports")

    def __str__(self):
        return self.toursports_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.toursports_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.toursports_file.path)




# # TourNews models
class TourNews(models.Model):
    tournews_title =  models.CharField(max_length=100)
    tournews_video = models.FileField(upload_to="Tournews/%y", default="")
    tournews_file = models.ImageField(default='default.png', blank=True, upload_to="Tournews")

    def __str__(self):
        return self.tournews_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.tournews_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.tournews_file.path)


        
# # TourGames models
class TourGames(models.Model):
    tourgames_title =  models.CharField(max_length=100)
    tourgames_video = models.FileField(upload_to="Tourgames/%y", default="")
    tourgames_file = models.ImageField(default='default.png', blank=True, upload_to="Tourgames")

    def __str__(self):
        return self.tourgames_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.tourgames_file.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.tourgames_file.path)