% --- Medical Diagnosis Expert System using Backward Chaining ---

start :-
    write('Welcome to the Medical Diagnosis Expert System!'), nl,
    write('Please answer the following questions with yes. or no.'), nl,
    disease(Disease),
    write('Based on your symptoms, you may have: '), write(Disease), nl,
    undo.

% --- Diseases and related symptoms
disease(cold) :- cold, !.
disease(flu) :- flu, !.
disease(malaria) :- malaria, !.
disease(covid19) :- covid19, !.
disease(unknown) :- write('Sorry, we could not determine your illness.'), nl.

% --- Disease Rules
cold :-
    verify(sneezing),
    verify(runny_nose),
    verify(sore_throat),
    verify(mild_fever).

flu :-
    verify(high_fever),
    verify(headache),
    verify(body_ache),
    verify(cough).

malaria :-
    verify(high_fever),
    verify(sweating),
    verify(shivering),
    verify(vomiting).

covid19 :-
    verify(high_fever),
    verify(dry_cough),
    verify(loss_of_taste),
    verify(difficulty_breathing).

% --- Ask user and remember answer
verify(Symptom) :-
    known(Symptom, true), !.

verify(Symptom) :-
    known(Symptom, false), !, fail.

verify(Symptom) :-
    ask(Symptom),
    read(Response),
    nl,
    ( (Response == yes ; Response == y)
    -> assertz(known(Symptom, true))
    ;  assertz(known(Symptom, false)), fail).

% --- Question wording
ask(Question) :-
    write('Do you have '), write(Question), write('? (yes/no): ').

% --- Reset knowledge base
undo :- retract(known(_, _)), fail.
undo.

:- dynamic known/2.
