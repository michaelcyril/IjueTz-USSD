from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from mtaa import tanzania
import datetime
import requests


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""
        if text == "":
            response = "CON Ijue Tanzania by @michaelCyril \n"
            response += "1. Jua mikoa yote ya tanzania na kata zake \n"
            response += "2. Jua wilaya za mkoa wako \n"
            # response += "3. Jua kata za wilaya yako \n"

        elif text == "1":
            response = "CON Ndugu mwananchi hii ndio mikoa ya tanzania, andika jina la mkoa kujua wilaya zake by @michaelCyril \n"
            mikoa = tanzania
            m = 1
            for i in mikoa:
                response += str(m) + ". " + i + " \n"
                m = m + 1

        elif len(text.split("*")) == 2 and text.split("*")[0] == "1":
            mkoa = text.split("*")[1]
            wilaya = tanzania.get(mkoa.capitalize()).districts
            response = "CON Ndugu mwananchi hii ndio wilaya za " + mkoa + ", andika jina la wilaya kujua kata zake by @michaelCyril \n"
            a = 1
            for e in wilaya:
                response += str(a) + ". " + e + " \n"
                a = a + 1

        elif len(text.split("*")) == 3 and text.split("*")[0] == "1":
            mkoa = text.split("*")[1]
            wilaya = text.split("*")[2].capitalize()
            y = wilaya.replace(" ","\n")
            print(y)
            kata = tanzania.get(mkoa.capitalize()).districts.get(y).wards
            response = "END Ndugu mwananchi hizi ndio kata za " + wilaya + " by @michaelCyril \n"
            a = 1
            for e in kata:
                if e == "ward_post_code":
                    continue
                response += str(a) + ". " + e + " \n"
                a = a + 1

        elif text == "2":
            response = "CON Ingiza jina la mkoa wako @michaelCyril \n"

        elif len(text.split("*")) == 2 and text.split("*")[0] == "2":
            c = text.split("*")[1]
            print("hey i reach here")
            response = "END Ndugu mwananchi hizi ndio wilaya zinazo patikana mkoa wa " + c + " @michaelCyril \n"
            h = tanzania.get(c.capitalize()).districts
            print(h)
            a = 1
            for e in h:
                response += str(a) + ". " + e + " \n"
                a = a + 1

        # elif text == "3":
        #     response = "CON Ingiza jina la wilaya yako @michaelCyril \n"

        # elif len(text.split("*")) == 2 and text.split("*")[0] == "3":
        #     c = text.split("*")[1]
        #     response = "END Ndugu mwananchi hizi ndio kata zinazo patikana wilaya ya " + c + " @michaelCyril \n"
        #     h = tanzania.get(c.capitalize()).wards
        #     a = 1
        #     for e in h:
        #         response += str(a) + ". " + e + " \n"
        #         a = a + 1
        return HttpResponse(response)
    return HttpResponse("END error bro")
