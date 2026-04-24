# eml
EML (EML Machine Language) is a simple programming language built around the eml(x,y) function.

This project was inspired by this [paper on arXiv](https://arxiv.org/abs/2603.21852), describing a single mathematical function capable of implementing a wide variety of arithmetical operations.

## Language reference
### Invoking eml(x, y)
The syntax for invoking eml(x, y) is `x y`, where x is the first argument and y is the second one. 

### Multiplying the ans variable by -1
To multiply the ans variable by -1, use the `inv` command with no arguments.

### Showing help
To show the built-in help, type `h`.

### Ending program
To end the program, use the `q` command or send the end-of-file character (Ctrl+D on most Linux machines).

### Subroutines
EML has no built-in support for functions, jumping, or logic, but it is possible to produce a basic form of subroutine by copy-pasting pre-written code and using variables to pass data around.

Convention is to use lowercase w, x, y, z, and so on for subroutine inputs, and the `ans` variable for the finished output as well as any intermediate steps.

### Setting a variable
To set a variable, you use the `set` command, like this: `set x 5`.
`ans` can also be set like a variable.

### Using a variable
Putting a variable's name anywhere in a command invocation (except the first argument of the `set` command) will have it substituted to a value before the command is executed.

## Standard library
A basic standard library is available for `eml`:
* `epow.emlprg`: compute e^x
* `ln.emlprg`: compute ln(x)
* `subtract.emlprg`: compute x-y
* `add.emlprg`: compute x+y

For information on using these in your program, see the Subroutines section.
