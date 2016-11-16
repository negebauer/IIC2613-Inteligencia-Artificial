% if there is one initial situation, we assume all of them are

initial_states([[s1,[at_robby(r1),at(b1,r1),at(b2,r3),free(g1),free(g2)]],
                [s2,[at_robby(r1),at(b1,r2),at(b2,r3),free(g1),free(g2)]]]).

ball(B) :- member(B,[b1,b2]).
room(R) :- member(R,[r1,r2,r3]).
gripper(G) :- member(G,[g1,g2]).

poss(move(X,Y),SitSet) :-
  room(X),room(Y),\+X=Y,
  knows(at_robby(X), SitSet).

poss(pick(B,Room,Gripper),SitSet) :-
  ball(B),room(Room),gripper(Gripper),
  knows(at_robby(Room),SitSet),
  believes(at(B,Room),SitSet),
  knows(free(Gripper),SitSet).

poss(drop(B,Room,Gripper),SitSet) :-
  ball(B),room(Room),gripper(Gripper),
  knows(carry(B,Gripper),SitSet),
  knows(at_robby(Room),SitSet).

% complete reglas para conditional_positive_effect y conditional_negative_effect
conditional_positive_effect(move(X,Y),at_robby(X),at_robby(Y)).
conditional_positive_effect(pick(B,Room,Gripper),at(B,Room),carry(B,Gripper)).
conditional_positive_effect(drop(B,_,Gripper),carry(B,Gripper),free(Gripper)).
conditional_positive_effect(drop(B,Room,Gripper),carry(B,Gripper),at(B,Room)).

conditional_negative_effect(move(X,_),at_robby(X),at_robby(X)).
conditional_negative_effect(pick(B,Room,Gripper),at(B,Room),free(Gripper)).
conditional_negative_effect(pick(B,Room,_),at(B,Room),at(B,Room)).
conditional_negative_effect(drop(B,_,Gripper),carry(B,Gripper),carry(B,Gripper)).

holds(true,_).

holds(F,S) :-
  initial_states(Inits),
  member([S,X],Inits),
  member(F,X).

holds(F,do(A,S)) :-
  holds(F,S),
  \+ conditional_negative_effect(A,F0,F),
  holds(F0,S).


holds(F,do(A,S)) :-
  holds(F0,S),
  conditional_positive_effect(A,F0,F).

believes(F,Set) :-
  Set = [Head|_],
  holds(F, Head).

believes(F,Set) :-
  Set = [_|Tail],
  believes(F, Tail).

knows(F, [S]) :-
  holds(F, S).

knows(F,Set) :-
  Set = [Head|Tail],
  holds(F, Head),
  knows(F, Tail).

subDoSet([],[],_).
subDoSet([do(A,S)|Tail],[S|Tail2],A) :-
  subDoSet(Tail,Tail2,A).

legal(Set) :-
  initial_states(I),
  findall(S,member([S,_],I),Set).

legal(Set) :-
  legal(Set2),
  subDoSet(Set,Set2,A),
  poss(A,Set2).
