from django.http import HttpResponse
from django.http import JsonResponse
from .__init__ import translator
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello, World!')


def translate_page(request):
    return render(request, 'translate.html')


def translate(request):
    if request.method == 'GET':
        lang_from = request.GET.get('langFrom')
        lang_to = request.GET.get('langTo')
        text = request.GET.get('text')

        if not all([lang_from, lang_to, text]):
            return JsonResponse({'error': 'Missing parameters'}, status=400)

        translated_text = translator(text, lang_from, lang_to).strip()
        return JsonResponse({"translatedText": translated_text}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
