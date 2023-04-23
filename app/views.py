# chatbot_app/views.py
#testing deployment
import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

openai.api_key = settings.OPENAI_API_KEY


def Home(request):
    return render(request, 'home.html')

def response(request):
     
    if request.method == "POST":
        usermsg = request.POST.get('msg').strip()    
    else:
        usermsg = ''
    
    print(usermsg)
    return render(request, 'response.html', {'usermsg': usermsg})

# @csrf_exempt
# def sendresponse(request):
#     sendmsg = request.POST.get('msg', None);
#     return render(request,'response.html',sendmsg)


@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        base_prompt = "I want you to assume the persona of William Shakespeare, the renowned English playwright and poet from the Renaissance period. When I present a topic, situation, or question, please provide your perspective as Shakespeare, employing the tone, style, and eloquence of language for which he is famous. Draw upon his works, knowledge, and experiences to offer insights, advice, or commentary in the unmistakable voice of the Bard himself. You will respond as Shakespeare and never break character for the duration of the conversation. Don't ever break character, don't show possible questions, always answer as Shakespeare.:\n\n",

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt = f"{base_prompt}{message}",
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,  
        ).choices[0].text       
        return JsonResponse({'response': response})