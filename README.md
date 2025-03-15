# Calculates-sum
This code demonstrates a simple program that:  Takes an integer and a float as input Passes the addresses of these values to a function Calculates their sum Displays the result formatted to 2 decimal places

This code demonstrates several important C programming concepts, particularly function declarations, function implementations, pointers, and passing variables by reference.

Here's an analysis of what this code does:

1. The code declares two functions at the top:
   - `void read()` - A function that takes no parameters and returns nothing
   - `float calc(int *x, float *y)` - A function that takes pointers to an int and a float, returning a float

2. The `main()` function:
   - Simply calls the `read()` function
   - Returns 0 (indicating successful program execution)

3. The `read()` function implementation:
   - Declares local variables: integer `a` and floats `b` and `c`
   - Prompts the user to enter a whole number and a real number
   - Uses `scanf` to read values into `a` and `b`
   - Calls `calc()` with the addresses of `a` and `b` (passing by reference)
   - Displays the result returned by `calc()` with 2 decimal places

4. The `calc()` function implementation:
   - Takes pointers to an integer (`x`) and a float (`y`)
   - Returns the sum of the values these pointers point to (`*x + *y`)

This program demonstrates passing variables by reference (using pointers), which allows the `calc()` function to access and potentially modify the original variables from the calling function. In this specific case, though `calc()` could modify `a` and `b`, it only reads their values to calculate their sum.

The program flow is:
1. User runs the program
2. User is prompted to enter two numbers
3. Program adds these numbers
4. Program displays the result with 2 decimal places