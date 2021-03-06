rasa train
rasa run -m models --enable-api --cors "*" --debug

run action server using pycharm configuration

http://localhost:63342/rasa_try/index.html?_ijt=mvgviqcssg7i08n86p14t189jb


TODO
-----

! have a greeting when you open the chat
! whats on
! my entries
! how do I enter?
! map - show map with location and guide user there when they are ready
! checkin
-! rules for tack
! I need a vet
! where do I park (car, trailer, truck)
! I need a [something that is not in the database] - currently calls whatever is in the slot - how to clear the slot?

Knowledgebase
-------------
https://rasa.com/docs/rasa/core/knowledge-bases/#create-a-knowledge-base
https://blog.rasa.com/integrating-rasa-with-knowledge-bases/
https://github.com/RasaHQ/tutorial-knowledge-base/blob/master/actions.py
https://github.com/scholrly/neo4django

These are the default names::

    SLOT_MENTION = "mention"
    SLOT_OBJECT_TYPE = "object_type"
    SLOT_ATTRIBUTE = "attribute"
    SLOT_LISTED_OBJECTS = "knowledge_base_listed_objects"
    SLOT_LAST_OBJECT = "knowledge_base_last_object"
    SLOT_LAST_OBJECT_TYPE = "knowledge_base_last_object_type"



https://forum.rasa.com/t/faq-bot-knowledge-base/742/15
https://stackoverflow.com/questions/60734906/convert-faq-json-file-into-rasa-nlu-and-stories-files

? Build fresh for each event
? Combine different areas of expertise - eg. module for dressage tests may or may not be included


Examples
------------
https://github.com/RasaHQ/rasa/tree/master/examples/concertbot/

javascript widget:
https://github.com/JiteshGaikwad/Chatbot-Widget

weather
https://github.com/RasaHQ/NLU-training-data/blob/master/weather/nlu.md


Arriving at Event

Checkin

- identify event (from time/location)

- identify user or type of user
    competitior, judge, support
- I can help you with

- what is the weather forecast



Integrate with front end:
- web
- mobile
- rocket chat



Getting actions working
------------------------
Create action in actions.py::

    from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ShowSchedule(Action):

    def name(self) -> Text:
        return "action_show_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []



in domain.yaml add::

    actions:
    - action_show_schedule
  
In stores::

    ## Some question about schedule
    * greet
      - utter_greet
    * whats_on
        - action_show_schedule


Being able to debug actions.  
What didn't work:
https://www.jetbrains.com/help/pycharm/attaching-to-local-process.html

Create this python script then create a run configuration that runs it using Python Server.  Breakpoints work!

"""This script allows use of an IDE (Wing, Pycharm, ...) to debug custom actions:

(-) Place this script in same location as your actions.py
(-) Open & run it from within your IDE
(-) Now you can put breakpoints in your actions.py, but also explore the internals of the
    rasa_sdk action server itself.
"""

import os
import sys

# insert path of this script in syspath so actions.py will be found
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

#
# This is exactly like issuing the command:
#  $ rasa run actions
#
sys.argv.append('run')
sys.argv.append('actions')
from rasa.__main__ import main
main()

check action server::

    curl http://localhost:5055/health

    curl http://localhost:5055/actions

Ask for info to put in slot and display back
---------------------------------------------

hi
Hey! How are you?
which color
what color would you like?
blue
blue looks great.

responses::

      utter_fav_color:
    - text: "{favorite_color}  looks great."

  select_color:
    - text: "{favorite_color}"
    
slots::

    slots:
  favorite_color:
    type: text
    initial_value: "white"
    
story::

            
    ## whats_my_color
    * greet
        - utter_greet
    * whats_my_color
        - utter_ask_color
    * select_color
        - utter_fav_color
        
intents::

    ## intent:whats_on
    - what's on now?
    - show me the schedule
    - whats on
    - schedule
    - what's on in [arena 1](arena)
    
    ## intent:whats_my_color
    - what's the best color
    - which color?
    
    


Old version

intents:
  - greet
  - goodbye
  - thank
  - affirm
  - deny
  - mood_great
  - mood_unhappy
  - bot_challenge
  - whats_on
  - whats_on_next
  - competitors
  - whois_judging
  - results
  - competition
  - schedule_request
  - inform

entities:
  - competition
  - session_type
  - rider
  - horse
  - judge

slots:
  competition:
    type: text
  date_or_interest:
    type: 
responses:
  utter_greet:
  - text: "Hey! How are you?"

  utter_cheer_up:
  - text: "Here is something to cheer you up:"
    image: "https://i.imgur.com/nGF1K8f.jpg"

  utter_did_that_help:
  - text: "Did that help you?"

  utter_happy:
  - text: "Great, carry on!"

  utter_goodbye:
  - text: "Bye"

  utter_iamabot:
  - text: "I am a bot, powered by Rasa."

  utter_schedule
  - In [Ring 1](arena) the [Puissance](competition) is currently running. If you want to see the full
    schedule for the day go to [Full Schedule](https://skorie.ie/V1234).



  utter_judges
  - We cannot give you the list of judges yet



actions:
  - respond_schedule

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true


## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks

## intent:goodbye
- goodbye
- goodnight
- good bye
- good night
- see ya
- toodle-oo
- bye now
- so long
- byeeee
- bye bye
- gotta go
- farewell

## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:whats_on
- what's on now?
- what [competitions](session_type) can I watch
- show me [competitions](session_type) on now
- show me [clinics](session_type) on now
- show me what's on in [arena 1](arena)

## intent:whats_on_next
- what's on next?
- what's on later?
- show me schedule
- show me next [competitions](session_type) in [arena 2](arena)

## intent: competitors
- who is competing in [competition 1](session)
- who is participating in [clinics](session_type)

## intent: judges
- who is judging [competition 1](session)

## intent: results
- who won [competition 1](session)?
- what are the results for [competition 1](session)
- show me the winner of [competition 1](session)
- show me the full results of [competition 1](session)

## lookup:competition
data/lookups/competitions.txt

## intent:schedule_request
- is there a [Puissance](competition)?
- show me clases for [8 Year Old Horses](competition)
- show me competitions for [Young Riders](competition)


## intent:inform
- [Younge Riders](competition) is on now
- [8 Year Old Horses](competition) is on next
- Yes the [Puissance](competition) is on next
- The winner of the [Speed Stages](competition) is [Cormac Hanley](rider) riding [Copain Z](horse)


Generating Data for a show
----------------------------

https://rodrigopivi.github.io/Chatito/

https://yuukanoo.github.io/tracy/#/agents

## intent:need_service_provider
#- I need a [vet](service_provider)
#- I need a [doctor](service_provider)
#- I need [first aid](service_provider)
#- I need a [farrier](service_provider)
#- I need a [blacksmith]{"entity": "service_provider", "value": "farrier"}
#- my horse has lost a shoe {"entity": "service_provider", "value": "farrier"}


## intent:need_facility
- I need a [toilet](facility)
- I need [water](facility)



## synonym: session
# redefine using format {"entity": "city", "value": "New York City"}
#- competition
#- clinic
#- class
#- competitions
#- clinics
#- classes