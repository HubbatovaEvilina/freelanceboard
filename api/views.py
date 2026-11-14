from django.http import JsonResponse


def ping(request):
    return JsonResponse({'status': 'ok', 'message': 'pong'})


def health(request):
    return JsonResponse({'status': 'ok', 'service': 'web'})
