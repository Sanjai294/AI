% Chatbot Query Resolution System in Prolog
% This system demonstrates how to implement a simple knowledge-based chatbot
% that can answer user queries based on facts and rules.

% ======= Knowledge Base =======
% Facts about various domains
% Tech products
product(iphone, apple, smartphone, 999).
product(macbook, apple, laptop, 1299).
product(surface, microsoft, laptop, 1199).
product(pixel, google, smartphone, 799).
product(galaxy, samsung, smartphone, 899).

% Countries information
country(usa, north_america, english, 331).
country(india, asia, hindi, 1380).
country(china, asia, mandarin, 1441).
country(germany, europe, german, 83).
country(brazil, south_america, portuguese, 212).
country(nigeria, africa, english, 206).

% Health information
healthy_food(apple, fruit, vitamin_c).
healthy_food(spinach, vegetable, iron).
healthy_food(salmon, fish, omega3).
healthy_food(chicken, meat, protein).
healthy_food(quinoa, grain, protein).

% Educational courses
course(mathematics, science, difficult, 'problem solving').
course(history, humanities, medium, 'critical thinking').
course(programming, computer_science, medium, 'logical thinking').
course(literature, humanities, easy, 'communication').
course(physics, science, difficult, 'analytical skills').

% ======= Rules =======
% Product recommendations
recommend_product(Type, Budget, Product) :-
    product(Product, _, Type, Price),
    Price =< Budget.

% Country information rules
continent_countries(Continent, Country) :-
    country(Country, Continent, _, _).

populous_country(Country) :-
    country(Country, _, _, Population),
    Population > 200.

% Health recommendations
recommend_food(Nutrient, Food) :-
    healthy_food(Food, _, Nutrient).

% Course recommendations
recommend_course(Field, Difficulty, Course) :-
    course(Course, Field, Difficulty, _).

% ======= Pattern Matching for User Input =======
% Define patterns to match user queries
pattern_match(Query, Response) :-
    product_query(Query, Response).
pattern_match(Query, Response) :-
    country_query(Query, Response).
pattern_match(Query, Response) :-
    food_query(Query, Response).
pattern_match(Query, Response) :-
    course_query(Query, Response).
pattern_match(Query, Response) :-
    generic_query(Query, Response).

% Product related queries
product_query(Query, Response) :-
    contains(Query, [recommend, product, budget]),
    extract_budget(Query, Budget),
    extract_type(Query, Type),
    findall(P, recommend_product(Type, Budget, P), Products),
    format_product_response(Products, Type, Budget, Response).

product_query(Query, Response) :-
    contains(Query, [how, much, cost]),
    extract_product(Query, Product),
    (product(Product, Brand, Type, Price) ->
        format(atom(Response), "The ~w ~w from ~w costs $~w.", [Type, Product, Brand, Price])
    ;   Response = "I don't have information about that product.").

% Country related queries
country_query(Query, Response) :-
    contains(Query, [countries, in]),
    extract_continent(Query, Continent),
    findall(C, continent_countries(Continent, C), Countries),
    format_list_response("Countries in ~w include: ", [Continent], Countries, Response).

country_query(Query, Response) :-
    contains(Query, [population, of]),
    extract_country(Query, Country),
    (country(Country, _, _, Population) ->
        format(atom(Response), "The population of ~w is approximately ~w million.", [Country, Population])
    ;   Response = "I don't have population information for that country.").

% Food related queries
food_query(Query, Response) :-
    contains(Query, [foods, with]),
    extract_nutrient(Query, Nutrient),
    findall(F, recommend_food(Nutrient, F), Foods),
    format_list_response("Foods rich in ~w include: ", [Nutrient], Foods, Response).

food_query(Query, Response) :-
    contains(Query, [healthy, food]),
    findall(F-T, healthy_food(F, T, _), Foods),
    format_food_types(Foods, Response).

% Course related queries
course_query(Query, Response) :-
    contains(Query, [courses, in]),
    extract_field(Query, Field),
    findall(C-D, course(C, Field, D, _), Courses),
    format_courses_response(Field, Courses, Response).

course_query(Query, Response) :-
    contains(Query, [skills, from]),
    extract_course(Query, Course),
    (course(Course, Field, _, Skill) ->
        format(atom(Response), "~w, which is a ~w course, helps develop ~w.", [Course, Field, Skill])
    ;   Response = "I don't have information about skills for that course.").

% Generic queries
generic_query(Query, Response) :-
    contains(Query, [hello, hi]), 
    Response = "Hello! How can I help you today?".

generic_query(Query, Response) :-
    contains(Query, [help]), 
    Response = "I can answer questions about products, countries, healthy foods, and educational courses. Try asking about product recommendations, countries in a continent, foods with specific nutrients, or courses in a field.".

generic_query(_, "I'm not sure how to answer that query. Try asking about products, countries, foods, or courses.").

% ======= Helper Predicates =======
% Check if a list contains any of the words
contains(Text, Words) :-
    atomic_list_concat(TextWords, ' ', Text),
    member(Word, Words),
    member(Word, TextWords).

% Extract information from queries
extract_budget(Query, Budget) :-
    atomic_list_concat(Words, ' ', Query),
    member(BudgetWord, Words),
    atom_chars(BudgetWord, Chars),
    Chars = ['$'|Rest],
    atom_chars(BudgetAtom, Rest),
    atom_number(BudgetAtom, Budget).
extract_budget(_, 1000).  % Default budget

extract_type(Query, Type) :-
    (contains(Query, [smartphone]) -> Type = smartphone;
    contains(Query, [laptop]) -> Type = laptop;
    Type = smartphone).  % Default type

extract_product(Query, Product) :-
    (contains(Query, [iphone]) -> Product = iphone;
    contains(Query, [macbook]) -> Product = macbook;
    contains(Query, [surface]) -> Product = surface;
    contains(Query, [pixel]) -> Product = pixel;
    contains(Query, [galaxy]) -> Product = galaxy;
    fail).

extract_continent(Query, Continent) :-
    (contains(Query, [north_america, 'north america']) -> Continent = north_america;
    contains(Query, [asia]) -> Continent = asia;
    contains(Query, [europe]) -> Continent = europe;
    contains(Query, [africa]) -> Continent = africa;
    contains(Query, [south_america, 'south america']) -> Continent = south_america;
    fail).

extract_country(Query, Country) :-
    (contains(Query, [usa]) -> Country = usa;
    contains(Query, [india]) -> Country = india;
    contains(Query, [china]) -> Country = china;
    contains(Query, [germany]) -> Country = germany;
    contains(Query, [brazil]) -> Country = brazil;
    contains(Query, [nigeria]) -> Country = nigeria;
    fail).

extract_nutrient(Query, Nutrient) :-
    (contains(Query, [vitamin_c, 'vitamin c']) -> Nutrient = vitamin_c;
    contains(Query, [iron]) -> Nutrient = iron;
    contains(Query, [omega3, 'omega 3']) -> Nutrient = omega3;
    contains(Query, [protein]) -> Nutrient = protein;
    fail).

extract_field(Query, Field) :-
    (contains(Query, [science]) -> Field = science;
    contains(Query, [humanities]) -> Field = humanities;
    contains(Query, [computer_science, 'computer science']) -> Field = computer_science;
    fail).

extract_course(Query, Course) :-
    (contains(Query, [mathematics, math]) -> Course = mathematics;
    contains(Query, [history]) -> Course = history;
    contains(Query, [programming]) -> Course = programming;
    contains(Query, [literature]) -> Course = literature;
    contains(Query, [physics]) -> Course = physics;
    fail).

% Format responses
format_product_response([], _, _, "I couldn't find any products matching your criteria.").
format_product_response(Products, Type, Budget, Response) :-
    format_list_response("I recommend these ~w options under $~w: ", [Type, Budget], Products, Response).

format_list_response(_, _, [], "I couldn't find any items matching your criteria.").
format_list_response(Template, Args, Items, Response) :-
    atomic_list_concat(Items, ', ', ItemsList),
    append(Args, [ItemsList], AllArgs),
    format(atom(Response), Template, AllArgs).

format_food_types(Foods, Response) :-
    findall(Type-Count, (
        findall(F, (member(F-Type, Foods)), TypeFoods),
        length(TypeFoods, Count)
    ), TypeCounts),
    format_food_summary(TypeCounts, Response).

format_food_summary(TypeCounts, Response) :-
    findall(TypeInfo, (
        member(Type-Count, TypeCounts),
        format(atom(TypeInfo), "~w (~w)", [Type, Count])
    ), TypeInfos),
    atomic_list_concat(TypeInfos, ', ', Summary),
    format(atom(Response), "I know about these healthy food types: ~w", [Summary]).

format_courses_response(Field, [], Response) :-
    format(atom(Response), "I don't have information about courses in ~w.", [Field]).
format_courses_response(Field, Courses, Response) :-
    findall(CourseInfo, (
        member(Course-Difficulty, Courses),
        format(atom(CourseInfo), "~w (~w)", [Course, Difficulty])
    ), CourseInfos),
    atomic_list_concat(CourseInfos, ', ', CoursesList),
    format(atom(Response), "Courses in ~w include: ~w", [Field, CoursesList]).

% ======= Main Chat Interface =======
% Start the chatbot
start_chatbot :-
    write('Prolog Chatbot: Hello! How can I help you today?'), nl,
    write('(Type "quit" to exit)'), nl,
    chat_loop.

% Main chat loop
chat_loop :-
    write('You: '),
    read_line_to_string(user_input, Input),
    (
        Input = "quit" -> 
            write('Prolog Chatbot: Goodbye!'), nl
        ;
            string_lower(Input, LowerInput),
            process_input(LowerInput, Response),
            format('Prolog Chatbot: ~w~n', [Response]),
            chat_loop
    ).

% Process user input
process_input(Input, Response) :-
    pattern_match(Input, Response), !.
process_input(_, "I don't understand that query. Can you try rephrasing it?").

% Example queries to test the chatbot:
% recommend smartphone under $900
% how much does iphone cost
% countries in asia
% what is the population of india
% foods with protein
% healthy food types
% courses in science
% what skills do I get from programming