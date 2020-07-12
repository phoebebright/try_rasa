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

    
## get the weather
* get_weather
    - action_weather
    
## where to enter
* greet
  - utter_greet
* how_to_enter
    - utter_how_to_enter
      
## choose competitor
* choose {"user_type": "competitor"}
    - utter_welcome_competitor
## choose support
* choose {"user_type": "support"}
    - utter_welcome_support
## choose judge
* choose {"user_type": "judge"}
    - utter_welcome_judge
## choose spectator
* choose {"user_type": "spectator"}
    - utter_welcome_spectator
    - utter_whats_on_now
## choose team
* choose {"user_type": "team"}
    - utter_welcome_team
                                 
## schedule in location
* whats_on {"arena": "arena 1"}
    - utter_arena_1_schedule