from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.conf import settings


import os


# Create your views here.
class ReactAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.BASE_DIR, 'codesign_front/build', 'index.html')) as file:
                return HttpResponse(file.read())
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! ensure your React project has been built and index.html is available
                """,
                status=501,
            )
        

