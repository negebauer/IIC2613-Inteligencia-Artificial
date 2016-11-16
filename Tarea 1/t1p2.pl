% knows(F, Set)
%   F es conocido en el conjunto Set
% believes(F, Set)
%   F es creído en el conjunto Set
% conditional_positive_effect(A, predicates...)
%   La acción A tiene como resultado que [predicates] sea cierto
% conditional_negative_effect(A, predicates...)
%   La acción A tiene como resultado que [predicates] sea cierto
% poss(A, Set)
%   Acción A se puede ejecutar sobre conjunto Set
% holds(F, S)
%   F se cumple en la situación S
% legal(Set)
%   Acciones legales en el Set

% if there is one initial situation, we assume all of them are

initial_states([[s1,[at_robby(r1),at(b1,r1),at(b2,r3),free(g1),free(g2)]],
                [s2,[at_robby(r1),at(b1,r2),at(b2,r3),free(g1),free(g2)]]]).


ball(B) :- member(B,[b1,b2]).
room(R) :- member(R,[r1,r2,r3]).
gripper(G) :- member(G,[g1,g2]).

poss(move(X, Y), SitSet) :-
  room(X),
  room(Y),
  \+X=Y,
  knows(at_robby(X), SitSet).

poss(pick(B, Room, Gripper), SitSet) :-
  ball(B),
  room(Room),
  gripper(Gripper),
  knows(at_robby(Room), SitSet),
  believes(at(B, Room), SitSet),
  knows(free(Gripper), SitSet).

poss(drop(B, Room, Gripper), SitSet) :-
  ball(B),
  room(Room),
  gripper(Gripper),
  knows(carry(B, Gripper), SitSet),
  knows(at_robby(Room), SitSet).

% complete reglas para conditional_positive_effect y conditional_negative_effect

% positive_effect(move(_,Y),at_robby(Y)).
conditional_positive_effect(move(X, Y), at_robby(X), at_robby(Y)).

% positive_effect(pick(B,_,Gripper),carry(B,Gripper)).
conditional_positive_effect(pick(B, Room, Gripper), at(B, Room), carry(B, Gripper)).

% positive_effect(drop(_,_,Gripper),free(Gripper)).
conditional_positive_effect(drop(B, _, Gripper), carry(B, Gripper), free(Gripper)).

% positive_effect(drop(B,Room,_),at(B,Room)).
conditional_positive_effect(drop(B, Room, Gripper), carry(B, Gripper), at(B, Room)).

% negative_effect(move(X,_),at_robby(X)).
conditional_negative_effect(move(X, _), at_robby(X), at_robby(X)).

% negative_effect(pick(_,_,Gripper),free(Gripper)).
conditional_negative_effect(pick(B, Room, Gripper), at(B, Room), free(Gripper)).

% negative_effect(pick(B,Room,_),at(B,Room)).
conditional_negative_effect(pick(B, Room, _), at(B, Room), at(B, Room)).

% negative_effect(drop(B,_,Gripper),carry(B,Gripper)).
conditional_negative_effect(drop(B, _, Gripper), carry(B, Gripper), carry(B, Gripper)).

holds(true,_).

holds(Predicate, State) :-
  initial_states(Initial),
  member([State, Predicates], Initial),
  member(Predicate, Predicates).

holds(Predicate, do(Action, State)) :-
  holds(Predicate, State),
  \+ conditional_negative_effect(Action, RequiredPredicate, Predicate),
  holds(RequiredPredicate, State).


holds(Predicate, do(Action, State)) :-
  holds(RequiredPredicate, State),
  conditional_positive_effect(Action, RequiredPredicate, Predicate).

believes(Predicate, States) :-
  States = [State | _],
  holds(Predicate, State).

believes(Predicate, States) :-
  States = [_ | States],
  believes(Predicate, States).

knows(Predicate, [State]) :-
  holds(Predicate, State).

knows(Predicate, States) :-
  States = [State | States2],
  holds(Predicate, State),
  knows(Predicate, States2).

statesWithAction([], [], _).
statesWithAction([do(Action, State) | States], [State | States2], Action) :-
  statesWithAction(States, States2, Action).

legal(States) :-
  initial_states(Initial),
  findall(State, member([State, _], Initial), States).

legal(States) :-
  legal(NewStates),
  statesWithAction(States, NewStates, Action),
  poss(Action, NewStates).
