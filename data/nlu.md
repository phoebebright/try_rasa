
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
- are you real?

## intent:get_weather
- what's the weather
- what's the weather here
- what is the weather
- whats the weather
- weather?

## intent:how_to_enter
- where do I enter?
- where can I enter?
- who is doing the entries?
- how do I enter?


## intent:whats_on
- what's on now?
- show me the schedule
- whats on
- schedule
- what's on in [arena 1](arena)
- which competition is happening in [arena 1](arena)

## intent:competitor
- competitor
- I am a competitor

## intent:need_service_provider
- I need a [vet](service_type)
- I need a [doctor](service_type)
- I need [first aid](service_type)
- I need a [farrier](service_type)
- I need a [blacksmith]{"entity": "service_type", "value": "farrier"}
- my horse has lost a shoe {"entity": "service_type", "value": "farrier"}


## intent:query_knowledge_base
- what [restaurants](object_type:restaurant) can you recommend?
- list some [restaurants](object_type:restaurant)
- can you name some [restaurants](object_type:restaurant) please?
- can you show me some [restaurant](object_type:restaurant) options
- list [German](cuisine) [restaurants](object_type:restaurant)
- do you have any [mexican](cuisine) [restaurants](object_type:restaurant)?
- do you know the [price range](attribute:price-range) of [that one](mention)?
- what [cuisine](attribute) is [it](mention)?
- do you know what [cuisine](attribute) the [last one](mention:LAST) has?
- does [Donath](restaurant) have [outside seating](attribute:outside-seating)?
- what is the [price range](attribute:price-range) of [Berlin Burrito Company](restaurant)?
- what is with [I due forni](restaurant)?
- Do you also have any [Vietnamese](cuisine) [restaurants](object_type:restaurant)?
- What about any [Mexican](cuisine) [restaurants](object_type:restaurant)?
- Do you also know some [Italian](cuisine) [restaurants](object_type:restaurant)?
- can you tell me the [price range](attribute) of [that restaurant](mention)?
- what [cuisine](attribute) do [they](mention) have?
- what [hotels](object_type:hotel) can you recommend?
- please list some [hotels](object_type:hotel) in [Frankfurt am Main](city) for me
- what [hotels](object_type:hotel) do you know in [Berlin](city)?
- name some [hotels](object_type:hotel) in [Berlin](city)
- show me some [hotels](object_type:hotel)
- what are [hotels](object_type:hotel) in [Berlin](city)
- does the [last](mention:LAST) one offer [breakfast](attribute:breakfast-included)?
- does the [second one](mention:2) [include breakfast](breakfast-included)?
- what is the [price range](attribute:price-range) of the [second](mention:2) hotel?
- does the [first](mention:1) one has [wifi](attribute:free-wifi)?
- does the [third](mention:3) one has a [swimming pool](attribute:swimming-pool)?
- what is the [star rating](attribute:star-rating) of [Berlin Wall Hostel](hotel)?
- Does the [Hilton](hotel) has a [swimming pool](attribute:swimming-pool)?

## lookup:service_provider
- vet
- farrier
- doctor

## lookup:restaurant
- Donath
- Berlin Burrito Company
- I due forni
- Lụa Restaurant
- Pfefferberg
- Marubi Ramen
- Gong Gan

## lookup:hotel
- Hilton
- B&B
- Berlin Wall Hostel
- City Hotel
- Jugendherberge
- Berlin Hotel

 
