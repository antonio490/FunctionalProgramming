
# Functional Programming with Python

- Lambda expresions
- Higher order functions (Functions as arguments and return values)
- Common functional design patterns
- Errors and exceptions in lambda expresions

### Procedural programming

- Line by line (Script implementation)
- Heavy use of statements and expressions
- Long functions

### Functional programming

- Little se of statements
- Heavy use of expressions
- Single line functions


#### Stateless and side-effects

The state of program defines how a function works. Stateless functions always return the same result given the same arguments. Functions without side effects are related to stateless functions but not the same thing.

#### Referential transparency

Functions without side effects and stateless allow parallel execution and can be testet separately.

- Use of global variables make functions stateful.

Stateless functions are trivial, they reduce functions to its minimal and make them isolate.

#### Unit Testing

Normally functions are tested with different kinds of input to see if the behave well but there is not guarentee our function will behave well under certain circumstances.

Referential transparency allows formal provability, meaning we can reach some semi formal sense that a function is really correct on every possible way. 

#### Cons of Functional Programming

Recursion: Functions that call themselves. It is elegant but difficult to follow. In Python recursion is limited with a maximun recursion depth.

####  Statements 
Functional programming in its pure way does not use statements (Asignments, loops, conditional branching...) instead it uses expresions in order to improve performance.

