## question_right
* greet
  - utter_greet
  - utter_question_1
* answer_1{"quantities_right":"três"}
  - utter_feedback
  - utter_next
  - utter_question_2
* answer_2{"materials_right":"pedra"}
  - utter_feedback
  - utter_next
  - utter_question_3
* answer_3
  - complex_form
  - form{"name":"complex_form"}
  - form{"name":"null"}
 
## question_wrong
* greet
  - utter_greet
  - utter_question_1
* answer_1{"quantities_wrong":"quatro"}
  - utter_hint_1
* answer_1{"quantities_right":"três"}
  - utter_feedback
  - utter_next
  - utter_question_2 
* answer_2{"materials_wrong":"madeira"}
  - utter_hint_2
* answer_2{"materials_right":"pedra"}
  - utter_feedback
  - utter_next
  - utter_question_3
* answer_3
  - complex_form
  - form{"name":"complex_form"}
  - form{"name":"null"}
    
## out_of_scope
* greet
 - utter_greet
 - utter_question_1
* answer_2{"materials_right":"pedra"}
 - utter_out_of_scope
 - utter_question_1
* answer_1{"quantities_right":"três"}
  - utter_feedback
  - utter_next
  - utter_question_2
* answer_1{"quantities_right":"três"}
  - utter_out_of_scope
  - utter_question_2

  


## out_of_scope_2
* greet
 - utter_greet
 - utter_question_1
* answer_2{"materials_wrong":"madeira"}
 - utter_out_of_scope
 - utter_question_1
* answer_1{"quantities_right":"três"}
  - utter_feedback
  - utter_next
  - utter_question_2
* answer_1{"quantities_wrong":"quatro"}
  - utter_out_of_scope
  - utter_question_2






## interactive_story_1
* greet
    - utter_greet
    - utter_question_1
* answer_1{"quantities_right": "três"}
    - slot{"quantities_right": "três"}
    - utter_feedback
    - utter_next
    - utter_question_2
* answer_2{"materials_wrong": "madeira"}
    - slot{"materials_wrong": "madeira"}
    - utter_hint_2
* answer_2{"materials_right": "pedra"}
    - slot{"materials_right": "pedra"}
    - utter_feedback
