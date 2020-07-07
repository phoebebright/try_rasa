# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ShowSchedule(Action):

    def name(self) -> Text:
        return "action_show_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        is_arena = tracker.get_latest_entity_values("arena")

            # if entity == "arena":
            #     dispatcher.utter_message(text="The Puissance is currently on in Arena 1")


        dispatcher.utter_message(text="Hello World!")

        return []


#
#
#
# class ActionWeather(Action):
#     def name(self):
#         return 'action_weather'
#
#     def run(self, dispatcher, tracker, domain):
#         from apixu.client import ApixuClient
#         api_key = '937920fXXXXXX5f81747180611'
#         client = ApixuClient(api_key)
#
#         loc = tracker.get_slot('location')
#         current = client.getCurrentWeather(q=loc)
#
#         country = current['location']['country']
#         city = current['location']['name']
#         condition = current['current']['condition']['text']
#         temperature_c = current['current']['temp_c']
#         humidity = current['current']['humidity']
#         wind_mph = current['current']['wind_mph']
#
#         response = """ It is currently {} in {} at the moment. The Temperature is {} degrees, the humidity is {}%s and the wind speed is {} mph.""".format(
#             condition, city, temperature_c, humidity, wind_mph)
#
#         dispatcher.utter_message(response)
#         return [SlotSet('location', loc)]