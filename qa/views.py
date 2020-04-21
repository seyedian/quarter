from django.shortcuts import render
from django.views.generic import View
# Create your views here.


import time
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from django.http import JsonResponse


import multiprocessing
globalVar = True
globalRequest = []


class LiveReport(View):
    def post(self, request):

        try:
            if request.is_ajax():
                command = request.POST.get('command')
                if command == 'start':
                    url = request.POST.get('url')
                    scopes = request.POST.getlist('scopes[]')
                    options = {
                        'cleanup_onexit': False,
                        'connection_timeout': None  # Never timeout

                    }

                    # Download and install Chrome web driver
                    global driver
                    driver = webdriver.Chrome(
                        ChromeDriverManager().install(), seleniumwire_options=options)

                    # Specifying driver scopes
                    driver.scopes = scopes

                    # Opening up the URL address
                    driver.get(url)

                    #p1 = multiprocessing.Process(target=mytest)
                    # p1.start()
                    return JsonResponse({'status': 'success'}, status=200)
                else:
                    return JsonResponse({'status': 'success'}, status=200)
        except:
            return JsonResponse({'response': 'error'}, status=200)

    def get(self, request):
        return render(request, 'live_report.html')


"""
def liveReport(request):
    if request.is_ajax() and request.GET.get('command') == 'start':
        url = request.GET.get('url')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        documentState = driver.execute_script('return document.readyState')
        while documentState != 'complete':
            time.sleep(1)
            documentState = driver.execute_script('return document.readyState')
            print(documentState)
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return render(request, 'live_report.html')




def mytest():
    # Download and install Chrome web driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Specifying driver scopes
    # Opening up the URL address
    driver.get('https://www.google.com')
    while globalVar:
        globalRequest = driver.requests

    driver.close()
"""
