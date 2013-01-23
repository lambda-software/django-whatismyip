from django.http import HttpResponse

def main(request):
    html = request.META.get('REMOTE_ADDR', '').lower()
    return HttpResponse(html)