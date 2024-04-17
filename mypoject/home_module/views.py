from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, '')


def contact_page(request):
    return render(request, '')


def site_header_component(request):
    context = {

    }
    return render(request, '', context)


def site_footer_component(request):
    return render(request, '', {})
