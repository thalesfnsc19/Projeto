#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## question_01  
* greet: oi 
  - utter_greet
  - utter_question_1
* answer_1:[três](quantities)
  - utter_feedback
  - utter_next
  - utter_question_2
* answer_2:[pedra](materials)
  - utter_feedback

## question_01 wrong
* greet:oi
  - utter_greet
  - utter_question_1
* answer_1:[quatro](quantities)
  - utter_hint_1
* answer_1:[três](quantities)
  - utter_feedback
  - utter_next
  - utter_question_2 
* answer_2:[madeira](materials)
  - utter_hint_2
* answer_2:[pedra](materials)
  - utter_feedback


