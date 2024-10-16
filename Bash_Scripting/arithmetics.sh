#!/bin/bash

# Syntax: $((n1 + n2))

sum=$((7+8))
echo "The sum of 7 and 8 is: $sum"

# Also, you can use:
a=10
echo "a is $a"
b=2
echo "b is $b"

addition=$((a+b))
echo "Sum of a and b: $addition"

# Subtraction
difference=$((a-b))
echo "Difference of a and b: $difference"

# Division
division=$((a/b))
echo "a divided by b: $division"

# Multiplication
multiple=$((a*b))
echo "a multiplied by b: $multiple"

# Modulos
c=10
echo "c is $c"
d=3
echo "d is $d"

modulos=$((c%d))
echo "c modulos d: $modulos"

# For multiplication use: "*"
# For division use: "/"
# For modulos use: "%"
# For exponentiation or power use: "**"