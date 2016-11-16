% Esta es la solución que subieron. Me dijeron que no iba a tener puntaje asi que no la hice. Pero aquí está igual.

:- discontiguous positive_effect/2, negative_effect/2.

ball(B) :- member(B,[b1,b2]).
room(R) :- member(R,[r1,r2,r3,r4]).
gripper(G) :- member(G,[g1,g2]).

poss(move(X,Y),S) :- room(X),room(Y),\+X=Y,holds(at_robby(X),S).

poss(pick(B,Room,Gripper),S) :-
    ball(B),room(Room),gripper(Gripper),
    holds(at_robby(Room),S),
    holds(at(B,Room),S),
    holds(free(Gripper),S).

poss(drop(B,Room,Gripper),S) :-
    ball(B),room(Room),gripper(Gripper),
    holds(carry(B,Gripper),S),
    holds(at_robby(Room),S).

positive_effect(move(_,Y),at_robby(Y)).
negative_effect(move(X,_),at_robby(X)).

positive_effect(pick(B,_,Gripper),carry(B,Gripper)).
negative_effect(pick(_,_,Gripper),free(Gripper)).
negative_effect(pick(B,Room,_),at(B,Room)).

negative_effect(drop(B,_,Gripper),carry(B,Gripper)).
positive_effect(drop(_,_,Gripper),free(Gripper)).
positive_effect(drop(B,Room,_),at(B,Room)).


%

holds(F,s0) :- member(F,[at_robby(r1),at(b1,r2),at(b2,r3),free(g1),free(g2)]).

holds(F,do(A,S)) :-
    holds(F,S),
    \+ negative_effect(A,F).

holds(F,do(A,_)) :-
    positive_effect(A,F).

legal(s0).
legal(do(A,S)) :-
    legal(S),
    poss(A,S).
