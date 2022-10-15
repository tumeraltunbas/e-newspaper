from django.shortcuts import render
from News.models import News,Topic
from currency_converter import CurrencyConverter
import cryptocompare

def index(request):
    card_news = News.objects.order_by("-date")[:9]
    list_news = News.objects.order_by("date")[:4]
    bar_news = News.objects.order_by("?")[:10]
    return render(request, "index.html", {"card_news":card_news, "list_news":list_news, "bar_news":bar_news})

def navbar(request):
    topics = Topic.objects.all()
    context = {"topics":topics}
    return context

def currency_bar(request):
    c=CurrencyConverter()
    usd_btc = cryptocompare.get_avg("BTC", currency="USD")
    usd_eth = cryptocompare.get_avg("ETH",currency="USD")
    usd_eur = c.convert(1,'USD','EUR')
    usd_pound = c.convert(1,'USD','GBP')
    usd_cad = c.convert(1, 'USD','CAD')
    usd_sgd = c.convert(1, 'USD', 'SGD')
    usd_sek = c.convert(1, 'USD', 'SEK')
    usd_bgn = c.convert(1, 'USD', 'BGN')
    usd_try = c.convert(1, 'USD', 'TRY')
    usd_pln = c.convert(1, "USD", "PLN")
    context = {"usd_eur":usd_eur, "usd_pound":usd_pound, "usd_cad":usd_cad, "usd_sgd":usd_sgd, "usd_sek":usd_sek, "usd_bgn":usd_bgn, "usd_try":usd_try, "usd_pln":usd_pln, "usd_btc":usd_btc["PRICE"], "usd_eth":usd_eth["PRICE"]}
    return context
    