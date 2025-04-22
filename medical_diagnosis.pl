% --- Dynamic Predicate Declarations ---
:- dynamic symptom/1.

% --- Start the Diagnosis ---
diagnose :-
    write('Welcome to the Medical Diagnosis Expert System!'), nl,
    write('Please answer the following questions with yes or no.'), nl, nl,
    retractall(symptom(_)),
    ask_symptoms,
    diagnosis(Disease),
    nl,
    write('Diagnosis Result: You may have '), write(Disease), write('.'), nl, !.

diagnose :-
    nl, write('Sorry, your symptoms do not match any known disease in our system.'), nl.

% --- Asking Symptoms ---
ask_symptoms :-
    ask('Do you have sneezing? (yes/no): ', sneezing),
    ask('Do you have runny nose? (yes/no): ', runny_nose),
    ask('Do you have sore throat? (yes/no): ', sore_throat),
    ask('Do you have mild fever? (yes/no): ', mild_fever),
    ask('Do you have high fever? (yes/no): ', high_fever),
    ask('Do you have headache? (yes/no): ', headache),
    ask('Do you have body ache? (yes/no): ', body_ache),
    ask('Do you feel fatigue? (yes/no): ', fatigue),
    ask('Do you have cough? (yes/no): ', cough),
    ask('Do you have loss of taste or smell? (yes/no): ', loss_of_taste_smell),
    ask('Do you have difficulty breathing? (yes/no): ', difficulty_breathing),
    ask('Do you have chills? (yes/no): ', chills),
    ask('Do you have sweating? (yes/no): ', sweating),
    ask('Do you feel nausea? (yes/no): ', nausea).

ask(Question, Symptom) :-
    write(Question),
    read(Response),
    (Response == yes -> asserta(symptom(Symptom)) ; true).

% --- Diagnosis Rules ---
diagnosis(common_cold) :-
    symptom(sneezing),
    symptom(runny_nose),
    symptom(sore_throat),
    symptom(mild_fever).

diagnosis(flu) :-
    symptom(high_fever),
    symptom(headache),
    symptom(body_ache),
    symptom(fatigue),
    symptom(cough).

diagnosis(covid_19) :-
    symptom(fever),
    symptom(cough),
    symptom(loss_of_taste_smell),
    symptom(difficulty_breathing),
    symptom(fatigue).

diagnosis(malaria) :-
    symptom(high_fever),
    symptom(chills),
    symptom(sweating),
    symptom(headache),
    symptom(nausea).

% --- Optional: Add More Conditions Below ---
% diagnosis(disease_name) :- symptom(...), symptom(...), ...
