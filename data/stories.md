## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Some question about schedule
* greet
  - utter_greet
* whats_on
    - action_show_schedule
    
## whats_my_color
* greet
    - utter_greet
* whats_my_color
    - utter_ask_color
* select_color
    - utter_fav_color
    