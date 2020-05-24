# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
# class SetResponse(Action):
#        def name(self):
#            return "set_response"
#
#        def run(self, dispatcher, tracker, domain):
#            return []

class ComplexForm(FormAction):

    def name(self):
        return "complex_form" 
    
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["wolf_action1","subject_1","wolf_action2","subject_2"]
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_template('utter_feedback',Tracker)
        return []

