ball(B) :- member(B,[b1,b2]).
room(R) :- member(R,[r1,r2,r3,r4]).
gripper(G) :- member(G,[g1,g2]).

poss(move(X,Y),S) :- room(X),room(Y),\+X=Y,holds(at_robby(X),S).

poss(pick(B,Room,Gripper),S) :-
    ball(B),room(Room),gripper(Gripper),
    %complete

poss(drop(B,Room,Gripper),S) :-
    ball(B),room(Room),gripper(Gripper),
    %complete

% Complete reglas para positive_effect y negative_effect

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
