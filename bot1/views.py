import json, telebot
from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .bot import bot
from .bot2 import bot as bot2


@require_http_methods(["POST"])
@csrf_exempt
def webhook(request, *args, **kwargs):
    data = request.body
    update = telebot.types.Update.de_json(json.loads(data))
    bot.process_new_updates([update])
    return JsonResponse("Ok", safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def webhook2(request, *args, **kwargs):
    data = request.body
    update = telebot.types.Update.de_json(json.loads(data))
    bot2.process_new_updates([update])
    return JsonResponse("Ok", safe=False)


def test(request):
    return JsonResponse("Bot Deployed Succesfully on /webhook/", safe=False)
