from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import requests
import json
import pdb

from .models import (AboutIcons, Banking, Programming, SearchBox, HomeIcons, SlaysiteIcons, News_article, Sports, 
Web, KoinoniaVideo, Koinonia, KoinoniaVidAMO, KoinoniaAMO, Koinonia_Others, Hillsong, Gospel, Amazon, Apps, Arts, AudioBook, 
AutoMobiles, Banking, Bcosmetics, Birthday, Books, Browsers, Cartoons, Cfood, Crypto, Disney, Education, Entertainment, Fashion,
Gaming, Gdp, Google, Gdesign, HealthCare, ICT, Images, Jobs, Microsoft, Movies, Music, News, OnlineDating, OnlinePayment, Opera, 
Pdfs, Programming, Shopping, Social, Sports, Travel, Tv_Shows, Videos, Wallet, Weather, WebHosting, Wikipedia, WWE, Covid_19, TourAll, 
TourMovies, TourMusics, TourSports, TourNews, TourGames)

# Create your views here.
def home_view(request, *args, **kwargs):
    searchlink = SearchBox.objects.all()
    homeiconlink = HomeIcons.objects.all()
    
    
    context= {
        "searchbox_title": searchlink,
        "homeicon_file": homeiconlink,
        

    }
    return render(request, "blog/home.html", context)

def main_view(request, *args, **kwargs):
    # ip = requests.get('https://api.ipify.org?format=json')
    # ip_data = json.loads(ip.text)
    # res = requests.get('http://ip-api.com/json/' + ip_data ["ip"])
    # location_data_one = res.text
    # location_data = json.loads(location_data_one)

#################### Geo-location for country only at the top #####################
    slaysite = SlaysiteIcons.objects.all()
    newsarticlelink = News_article.objects.all()
    web_links = Web.objects.all()
    koinoniavid_links = KoinoniaVideo.objects.all()
    koinonia_links = Koinonia.objects.all()
    koinoniavidamo_links = KoinoniaVidAMO.objects.all()
    koinoniaamo_links = KoinoniaAMO.objects.all()
    koothers_links = Koinonia_Others.objects.all()
    hillsong_links = Hillsong.objects.all()
    gospel_links = Gospel.objects.all()
    amazon_links = Amazon.objects.all()
    apps_links = Apps.objects.all()
    art_links = Arts.objects.all()
    audiobook_links = AudioBook.objects.all()
    automobiles_links = AutoMobiles.objects.all()
    banking_links = Banking.objects.all()
    bcosmetics_links = Bcosmetics.objects.all()
    birthday_links = Birthday.objects.all()
    books_links = Books.objects.all()
    browsers_links = Browsers.objects.all()
    cartoons_links = Cartoons.objects.all()
    cfood_links = Cfood.objects.all()
    crypto_links = Crypto.objects.all()
    disney_links = Disney.objects.all()
    education_links = Education.objects.all()
    entertainment_links = Entertainment.objects.all()
    fashion_links = Fashion.objects.all()
    gaming_links = Gaming.objects.all()
    gdp_links = Gdp.objects.all()
    google_links = Google.objects.all()
    gdesign_links = Gdesign.objects.all()
    healthcare_links = HealthCare.objects.all()
    ict_links = ICT.objects.all()
    images_links = Images.objects.all()
    jobs_links = Jobs.objects.all()
    microsoft_links = Microsoft.objects.all()
    movies_links = Movies.objects.all()
    music_links = Music.objects.all()
    news_links = News.objects.all()
    online_dating_links = OnlineDating.objects.all()
    online_payment_links = OnlinePayment.objects.all()
    opera_links = Opera.objects.all()
    pdfs_links = Pdfs.objects.all()
    programming_links = Programming.objects.all()
    shopping_links = Shopping.objects.all()
    social_links = Social.objects.all()
    sports_links = Sports.objects.all()
    travel_links = Travel.objects.all()
    tvshows_links = Tv_Shows.objects.all()
    videos_links = Videos.objects.all()
    wallet_links = Wallet.objects.all()
    weather_links = Weather.objects.all()
    webhost_links = WebHosting.objects.all()
    wikipedia_links = Wikipedia.objects.all()
    wwe_links = WWE.objects.all()
    covid19_links = Covid_19.objects.all()

    context = {
        # "data": location_data,
        "slaysiteicon_file": slaysite,
        "news_article_file": newsarticlelink,
        "web_file": web_links,
        "koinoniavid_file": koinoniavid_links,
        "koinonia_file": koinonia_links,
        "koinoniavidamo_file": koinoniavidamo_links,
        "koinoniaamo_file": koinoniaamo_links,
        "koothers_file": koothers_links,
        "hillsong_file": hillsong_links,
        "gospel_file": gospel_links,
        "amazon_file": amazon_links,
        "aps_file": apps_links,
        "art_file": art_links,
        "audiobook_file": audiobook_links,
        "automobiles_file": automobiles_links,
        "banking_file": banking_links,
        "bcosmetics_file": bcosmetics_links,
        "birthday_file": birthday_links,
        "books_file": books_links,
        "browsers_file": browsers_links,
        "cartoons_file": cartoons_links,
        "cfood_file": cfood_links,
        "crypto_file": crypto_links,
        "disney_file": disney_links,
        "education_file": education_links,
        "entertainment_file": entertainment_links,
        "fashion_file": fashion_links,
        "gaming_file": gaming_links,
        "gdp_file": gdp_links,
        "google_file": google_links,
        "gdesign_file": gdesign_links,
        "healthcare_file": healthcare_links,
        "ict_file": ict_links,
        "images_file": images_links,
        "jobs_file": jobs_links,
        "microsoft_file": microsoft_links,
        "movies_file": movies_links,
        "music_file": music_links,
        "news_file": news_links,
        "online_dating_file": online_dating_links,
        "online_payment_file": online_payment_links,
        "opera_file": opera_links,
        "pdfs_file": pdfs_links,
        "program_file": programming_links,
        "shopping_file": shopping_links,
        "social_file": social_links,
        "sports_file": sports_links,
        "travel_file": travel_links,
        "tvshows_file": tvshows_links,
        "videos_file": videos_links,
        "wallet_file": wallet_links,
        "weather_file": weather_links,
        "webhost_file": webhost_links,
        "wikipedia_file": wikipedia_links,
        "wwe_file": wwe_links,
        "covid19_file": covid19_links,
        'title': 'Easy access to different websites',
    }

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        messages.success(request, f'!!! {message_name}')
        
        send_mail(
            "DONATE MESSAGE- "
            'name: ' + message_name,
            'subject: ' + message_subject,
            'email: ' + message_email,

            recipient_list=['slaysite@gmail.com'],
            fail_silently=False
            )
        return render(request, "blog/main.html", context)
    else:
        return render(request, "blog/main.html", context)




def about_view(request, *args, **kwargs):
    slaysite = SlaysiteIcons.objects.all()
    aboutpagebackimage = AboutIcons.objects.all()

    context = {
        "slaysiteicon_file": slaysite,
        "abouticon_file": aboutpagebackimage,
        'title': 'About Dzipup',

    }
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        messages.success(request, f'!!! {message_name}')
        
        send_mail(
            "ABOUT MESSAGE- "
            'name: ' + message_name,
            'subject: ' + message_subject,
            'email: ' + message_email,

            recipient_list=['slaysite@gmail.com'],
            fail_silently=False
            )
        return render(request, "blog/about.html", context)
    else:
        return render (request, "blog/about.html", context)


def tour_view(request, *args, **kwargs):
    tourall_links = TourAll.objects.all()
    tourmovies_links = TourMovies.objects.all()
    tourmusics_links = TourMusics.objects.all()
    toursports_links = TourSports.objects.all()
    tournews_links = TourNews.objects.all()
    tourgames_links = TourGames.objects.all()

    context = {
        "tourall_file": tourall_links,
        "tourmovies_file": tourmovies_links,
        "tourmusics_file": tourmusics_links,
        "toursports_file": toursports_links,
        "tournews_file": tournews_links,
        "tourgames_file": tourgames_links,
        'title': 'Finding Your Next Tour On Dzipup',
    }
    return render(request, "blog/tour.html", context)