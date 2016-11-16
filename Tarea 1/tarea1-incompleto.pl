% if there is one initial situation, we assume all of them are

initial_states([[s1,[at_robby(r1),at(b1,r1),at(b2,r3),free(g1),free(g2)]],
                [s2,[at_robby(r1),at(b1,r2),at(b2,r3),free(g1),free(g2)]]]).


ball(B) :- member(B,[b1,b2]).
room(R) :- member(R,[r1,r2,r3]).
gripper(G) :- member(G,[g1,g2]).

poss(move(X,Y),SitSet) :- %complete

poss(pick(B,Room,Gripper),SitSet) :- %complete aca

poss(drop(B,Room,Gripper),SitSet) :- %complete aca

% complete reglas para conditional_positive_effect y conditional_negative_effect

holds(true,S).

holds(F,S) :-
    initial_states(Inits),
    %complete 


holds(F,do(A,S)) :-
    holds(F,S),
    %complete

holds(F,do(A,S)) :-
    %complete

believes(F,Set) :- %complete

knows(F,Set) :- %complete 

legal(Set) :- initial_states(I),findall(S,member([S,L],I),Set).
legal(Set) :- %complete 

