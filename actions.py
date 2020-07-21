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
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from rasa_sdk.knowledge_base.utils import (
    SLOT_OBJECT_TYPE,
    SLOT_LAST_OBJECT_TYPE,
    SLOT_ATTRIBUTE,
    reset_attribute_slots,
    SLOT_MENTION,
    SLOT_LAST_OBJECT,
    SLOT_LISTED_OBJECTS,
    get_object_name,
    get_attribute_slots,
)

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

class ShowServices(ActionQueryKnowledgeBase):

    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("event_data.json")


        # # overwrite the representation function of the hotel object
        # # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "service_provider", lambda obj: obj["name"] + " (" + obj["mobile"] + ")"
        )

        super().__init__(knowledge_base)


    def name(self) -> Text:
        return "action_service_providers"


    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """
        Executes this action. If the user ask a question about an attribute,
        the knowledge base is queried for that attribute. Otherwise, if no
        attribute was detected in the request or the user is talking about a new
        object type, multiple objects of the requested type are returned from the
        knowledge base.

        Args:
            dispatcher: the dispatcher
            tracker: the tracker
            domain: the domain

        Returns: list of slots

        """

        # need to check that service_type matches something in the list
        # if so the the slot will have been filled but if not the slot will have the value from the last time it was set
        # this is a hack to unset it
        if len(tracker.latest_message['entities']) == 0:
            SlotSet('service_type', None)
            dispatcher.utter_message("I can't help you with that.  Try asking for something else :-)")
            return []

        entity_types = [item['entity'] for item in tracker.latest_message['entities']]

        if 'service_type' in entity_types:
            service_type = tracker.slots["service_type"]
            object_type = "service_provider"
            attribute = "service_type"
        elif 'service' in entity_types:
            service_type = tracker.slots["service"]
            object_type = "service"
            attribute = "service_type"
        else:
            dispatcher.utter_message("I can't help you with that.  Try asking for something else :-)")
            return []


        objects = self.knowledge_base.data[object_type]

        # filter objects by attributes
        if service_type:
            objects = list(
                filter(
                    lambda obj:
                                obj[attribute] == service_type
                                , objects,
                )
            )

        response = f"The following {service_type}s are available :\n" + '\n '.join([f"{obj['name']} call {obj['mobile']}" for obj in objects])

        dispatcher.utter_message(response)

        return []

    # def run(self, dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #
    #     #is_arena = tracker.get_latest_entity_values("arena")
    #
    #         # if entity == "arena":
    #         #     dispatcher.utter_message(text="The Puissance is currently on in Arena 1")
    #
    #     service_type = tracker.slots["service_type"]
    #
    #     services = self.get_objects("service_provider", [{'service_type': service_type},])
    #
    #     text=f"We have the following {service_type}s on call:"
    #
    #
    #     dispatcher.utter_message(text=text)
    #
    #     return []


class TestSheetKB(ActionQueryKnowledgeBase):

    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("kb_data/testsheets.json")


        # # overwrite the representation function of the hotel object
        # # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "testsheets", lambda obj: obj["name"] + " (" + obj["code"] + ")"
        )

        super().__init__(knowledge_base)


    def name(self) -> Text:
        return "action_show_testsheet"


    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """
        Executes this action. If the user ask a question about an attribute,
        the knowledge base is queried for that attribute. Otherwise, if no
        attribute was detected in the request or the user is talking about a new
        object type, multiple objects of the requested type are returned from the
        knowledge base.

        Args:
            dispatcher: the dispatcher
            tracker: the tracker
            domain: the domain

        Returns: list of slots

        """

        # slot testsheets holds all the testsheets related to this person.
        # if they are a spectator, all the ones they have made enquiries about
        # if the are a competitor, it should be preloaded with the tests they are riding today


        entity_types = [item['entity'] for item in tracker.latest_message['entities']]

        testsheet = tracker.slots["testsheet"]
        object_type = "testsheet"
        attribute = "code"



        objects = self.knowledge_base.data[object_type]

        # filter objects by attributes
        if service_type:
            objects = list(
                filter(
                    lambda obj:
                                obj[attribute] == service_type
                                , objects,
                )
            )

        response = f"The following {service_type}s are available :\n" + '\n '.join([f"{obj['name']} call {obj['mobile']}" for obj in objects])

        dispatcher.utter_message(response)

        return []

class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # # overwrite the representation function of the hotel object
        # # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "service_provider", lambda obj: obj["name"] + " (" + obj["mobile"] + ")"
        )

        super().__init__(knowledge_base)

    def name(self) -> Text:
        return "action_query_knowledge_base"


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