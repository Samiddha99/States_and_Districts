from django.shortcuts import *
from django.http import *
from django.views.decorators.http import *
import traceback
from .models import *
from django_ratelimit.decorators import ratelimit
from django.conf import settings


# Create your views here.
@require_safe
@ratelimit(group='Main', key='ip', rate=settings.DEFAULT_VIEW_RATE_LIMIT, method=ratelimit.ALL, block=True)
def home(request):
    context = {
        'states': States.objects.all(),
        'districts': Districts.objects.all(),
    }
    return render(request, "index.html", context=context)

@require_safe
@ratelimit(group='Main', key='ip', rate=settings.DEFAULT_VIEW_RATE_LIMIT, method=ratelimit.ALL, block=True)
def apiSearch(request):
    try:
        state = request.GET.get("state_name", '')
        district = request.GET.get('district_name', '')
        State = States.objects.filter(Name=state)
        District = Districts.objects.filter(Name=district)
        response_data = {}
        status = None
        if state != '' and district != '':
            if State.exists() and District.exists():
                State = State.first()
                District = District.first()
                districts = Districts.objects.filter(state=State)
                response_data = {
                    'Success': True,
                    'Is_Matched': District.state.Name == State.Name,
                    'State': State.Name,
                    'Districts': list(districts.values_list("Name", flat=True)),
                    'Is_UT': State.Is_Union_Territory,
                }
                status = 200
            elif not District.exists():
                State = State.first()
                districts = Districts.objects.filter(state=State)
                response_data = {
                    'Success': True,
                    'State': State.Name,
                    'Districts': list(districts.values_list("Name", flat=True)),
                    'Is_UT': State.Is_Union_Territory,
                    'Message': "No district found with the given district_name.",
                    'Error': '404.b'
                }
                status = 404
            elif not State.exists():
                response_data = {
                    'Success': False,
                    'Message': "No state found with the given state_name.",
                    'Error': '404.a'
                }
                status = 404
        elif state != '':
            if State.exists():
                State = State.first()
                districts = Districts.objects.filter(state=State)
                response_data = {
                    'Success': True,
                    'State': State.Name,
                    'Districts': list(districts.values_list("Name", flat=True)),
                    'Is_UT': State.Is_Union_Territory,
                }
                status = 200
            else:
                response_data = {
                    'Success': False,
                    'Message': "No state found with the given state_name.",
                    'Error': '404.a'
                }
                status = 404
        elif district != '':
            if District.exists():
                District = District.first()
                districts = Districts.objects.filter(state=District.state)
                response_data = {
                    'Success': True,
                    'State': District.state.Name,
                    'Districts': list(districts.values_list("Name", flat=True)),
                    'Is_UT': District.state.Is_Union_Territory,
                }
                status = 200
            else:
                response_data = {
                    'Success': False,
                    'Message': "No district found with the given district_name.",
                    'Error': '404.b'
                }
                status = 404
        else:
            states = States.objects.all()
            states_data = []
            for state in states:
                districts = list(Districts.objects.filter(state=state).values_list("Name", flat=True))
                state_dict = {
                    'State': state.Name,
                    'Districts': districts,
                    'Is_UT': state.Is_Union_Territory,
                }
                states_data.append(state_dict)
            response_data = {
                'Success': True,
                'Data': states_data,
            }
            status = 200
        return JsonResponse(response_data, status=status)
    except:
        traceback.print_exc()
        response_data = {}
        response_data["Error"] = "500"
        response_data["Success"] = False
        response_data["Message"] = "Server Error"
        status = 500 # Internal Server Error
        return JsonResponse(response_data, status=status)