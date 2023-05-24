from django.core.management.base import BaseCommand, CommandError
from app.models import *
import traceback
import json

class Command(BaseCommand):
    help = 'Create data'
    def handle(self, *args, **kwargs):
        try:
            json_path = f"./assets/static/json/states.json"
            json_file = open(json_path, "r")
            json_data = json.load(json_file)
            for state in json_data:
                if not States.objects.filter(Name=state["state"]).exists():
                    States.objects.create(Name=state["state"], Is_Union_Territory=state['union_territory'])
                state_obj = States.objects.get(Name=state["state"])
                for district in state['districts']:
                    if not Districts.objects.filter(Name=district, state=state_obj).exists():
                        Districts.objects.create(Name=district, state=state_obj)
        except:
            traceback.print_exc()