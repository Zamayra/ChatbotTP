import random

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

animals_db = {
    'puppy': 'https://i.imgur.com/aeWQBPb.jpeg',
    'butterflies': 'https://i.imgur.com/wuaYap6.jpeg',
    'koala': 'https://i.imgur.com/1p5nKyZ.jpeg',
    'kangaroo': 'https://i.imgur.com/7jKQ33i.jpeg',
    'elephant': 'https://i.imgur.com/3fLmUEu.jpeg',
    'turtle': 'https://i.imgur.com/a6Xjw5L.jpeg',
    'giraffe': 'https://i.imgur.com/htl4k1N.jpeg',
    'panda': 'https://i.imgur.com/JXiw5qb.jpeg',
    'dog': 'https://i.imgur.com/fSgnUKW.jpeg',
    'cat': 'https://i.imgur.com/0HErNcZ.jpeg',
    'horse': 'https://i.imgur.com/zXrsJRE.jpeg'
}

class ActionShowImage(Action):

     def name(self) -> Text:
         return "action_show_image"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = next(tracker.get_latest_entity_values("animal"),None)
        
        if not animal_type: 
             msg = f"I'm sorry, I don't have photos of that animal. Try another one! for exemple butterflies, kangaroo, puppy or panda!"
             dispatcher.utter_message(text=msg)
             return []
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = "Let me see... I found this... Does it help?",
        			             image=animal_image)

class ActionRandomImage(Action):

     def name(self) -> Text:
         return "action_random_image"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = random.choice(list(animals_db.keys()))
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = f"I found this cute {animal_type} ! Does it help?",
        			             image=animal_image)

class ActionFavoriteAnimal(Action):

     def name(self) -> Text:
         return "action_favorite_animal"
        
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        animal_type = next(tracker.get_latest_entity_values("animal"),None)
        
        if not animal_type: 
             msg = f"They are really cute !"
             dispatcher.utter_message(text=msg)
             return []
        
        animal_image = animals_db.get(animal_type,None) 
        
        dispatcher.utter_message(text = "Me too ! I found this picture !",
        			             image=animal_image)