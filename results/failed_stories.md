## happy path 1 (/var/folders/dd/4x89x9g16q3_ntxvgm5y1jw40000gn/T/tmpo1963g4v/6aa13e3cd5254116b586a19041dd5def_conversation_tests.md)
* greet: hello there!   <!-- predicted: get_weather{"location": "New York"}: hello there! -->
    - utter_greet   <!-- predicted: action_listen -->
* mood_great: amazing
    - utter_happy   <!-- predicted: action_weather -->


## happy path 2 (/var/folders/dd/4x89x9g16q3_ntxvgm5y1jw40000gn/T/tmpo1963g4v/6aa13e3cd5254116b586a19041dd5def_conversation_tests.md)
* greet: hello there!   <!-- predicted: get_weather{"location": "New York"}: hello there! -->
    - utter_greet   <!-- predicted: action_listen -->
* mood_great: amazing
    - utter_happy   <!-- predicted: action_weather -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (/var/folders/dd/4x89x9g16q3_ntxvgm5y1jw40000gn/T/tmpo1963g4v/6aa13e3cd5254116b586a19041dd5def_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_greet -->


## sad path 2 (/var/folders/dd/4x89x9g16q3_ntxvgm5y1jw40000gn/T/tmpo1963g4v/6aa13e3cd5254116b586a19041dd5def_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_greet -->


## sad path 3 (/var/folders/dd/4x89x9g16q3_ntxvgm5y1jw40000gn/T/tmpo1963g4v/6aa13e3cd5254116b586a19041dd5def_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_greet -->


