from django.apps import AppConfig
import traceback


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    def ready(self):
        try:
            from app import add_all_data
            # add_all_data.addStates()
        except:
            traceback.print_exc()
