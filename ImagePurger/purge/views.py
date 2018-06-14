from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import PurgeLog, ServerList
from .forms import URLForm
from urllib import parse
import socket
import requests as req
import os


def purgeUrlCreate(reqURL, servers):
    parseurl = parse.urlparse(reqURL)
    urllist = {}
    if parseurl.scheme:
        for i in servers:
            url = "{}://{}{}".format(parseurl.scheme, i, parseurl.path)
            urllist[str(i)] = url
    else:
        for i in servers:
            url = "http://{}{}".format(i, parseurl.path)
            urllist[str(i)] = url
    return urllist


def purgeCall(urls):
    result = {}
    for url in urls.values():
        server = parse.urlparse(url)
        try:
            res = req.request('PURGE', url)
            bs = BeautifulSoup(res.text, 'html.parser')
            statusCode = res.status_code
            statusText = bs.center.h1.text
        except Exception as e:
            statusCode = '000'
            statusText = e

        if server.netloc not in result:
            result[server.netloc] = [statusText, statusCode]

    return result


@login_required(login_url='/purge/account/login')
def purge(requests):
    if requests.method == 'POST' and requests.POST['url']:
        form = URLForm(requests.POST)
        if form.is_valid():
            url = str(form.cleaned_data['url'])
            servers = ServerList.objects.all().filter(status=True).order_by('rank')

            purgeUrl = purgeUrlCreate(url, servers)
            purgeResult = purgeCall(purgeUrl)

            form = URLForm()
            for ip in purgeResult.keys():
                PurgeLog.objects.create(user=requests.user,
                                        originurl=url,
                                        requrl=purgeUrl[ip],
                                        result_text=purgeResult[ip][0],
                                        result_code=purgeResult[ip][1],)

            return render(requests, 'main.html', context={
                'requrl': url,
                'servers': servers,
                'result': purgeResult,
                'form': form,
             })

    else:
        servers = ServerList.objects.all().filter(status=True)
        form = URLForm()
        return render(requests, 'main.html', context={
            'servers': servers,
            'form': form,
         })
