# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests

class ShowSchedule(Action):

    def name(self) -> Text:
        return "action_show_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #is_arena = tracker.get_latest_entity_values("arena")

            # if entity == "arena":
            #     dispatcher.utter_message(text="The Puissance is currently on in Arena 1")

        user_type = tracker.slots['user_type']

        if user_type == "competitor":
            text="If you have your competitor number I can give you your schedule"
        elif user_type == "spectator":
            text="Would you like to see what's on?"
        else:
            text="Enjoy the show!"


        dispatcher.utter_message(text=text)

        return []





class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        loc = tracker.get_slot('location')
        if not loc:
            loc="Dunmanway"

        params = {
            'access_key': 'b4d0b394ea7e3826776a7ca0c898d49e',
            'query': loc,
            'forecast_days': 1,
        }

        api_result = requests.get('http://api.weatherstack.com/current', params)

        response = api_result.json()

        forecast = response['current']


        response = f"Forecast for today is {(', ').join(forecast['weather_descriptions'])}"


        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]