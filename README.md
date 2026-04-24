# eml
EML (EML Machine Language) is a simple programming language built around the eml(x,y) function.

This project was inspired by this [paper on arXiv](https://arxiv.org/abs/2603.21852), describing a single mathematical function capable of implementing a wide variety of arithmetical operations.

## Language reference
### Invoking eml(x, y)
The syntax for invoking eml(x, y) is `x y`, where x is the first argument and y is the second one. If either argument is specified as the string "ans", it will be substituted with the value from the previous operation (0 if no other operations have been run).

### Multiplying the ans variable by -1
To multiply the ans variable by -1, use the `inv` command with no arguments.

### Showing help
To show the built-in help, type `h`.

### Ending program
To end the program, use the `q` command or send the end-of-file character (Ctrl+D on most Linux machines).

### Subroutines
EML has no built-in support for functions, jumping, or logic, but it is possible to produce a basic form of subroutine by copy-pasting pre-written code and using `ans` to pass data around.

On Unix-like systems, the `cat` command can prove helpful in automating this task.

## Standard library
A basic standard library is available for `eml`:
* `zero.emlprg`: set `ans` to 0
* `epow.emlprg`: compute e^ans
* `ln.emlprg`: compute ln(ans)

For information on using these in your program, see the Subroutines section.
