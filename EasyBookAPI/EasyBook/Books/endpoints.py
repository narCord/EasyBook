from django.http import JsonResponse
from requests import Response


def test(request, testId):
        return JsonResponse({f'{testId}': 'testing'}, status=200)

def test2(request):
    return JsonResponse({'test': 'testing'}, status=200)
