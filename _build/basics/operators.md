---
interact_link: content/basics/operators.ipynb
kernel_name: python3
has_widgets: false
title: 'Operators'
prev_page:
  url: /basics/types
  title: 'Type Conversion'
next_page:
  url: /basics/functions
  title: 'Introduction to Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Operators



Coding, in the simplest sense, is merely the action of assigning values to variables, and then 'doing things' with those variables.

In this section we will look at some of the basic operators used for integers and floats. Other variable types have different operators, which we shall see later.

An obvious starting point is basic arithmetic; addition, subtraction, multiplication and division:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a = 2.0
b = 3.0
c = 10.0

print('a added to b is', a + b)
print('a multiplied by c is', a*c)
print('c divided by b is', c/b)
print('a subtracted from c', c - a)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
a added to b is 5.0
a multiplied by c is 20.0
c divided by b is 3.3333333333333335
a subtracted from c 8.0
```
</div>
</div>
</div>



These operators can also be used for integers:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('2 multiplied by 3 is', 2*3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2 multiplied by 3 is 6
```
</div>
</div>
</div>



and between integers and floats:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('1.5 multiplied by 2 is', 1.5*2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1.5 multiplied by 2 is 3.0
```
</div>
</div>
</div>



If you are using Python version 2.xxx or below, beware of dividing by integers...



## The Exponential Operator `**`
Another useful operator is the exponential operator `**`. This returns the left number to the power of the right:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(2**3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
8
```
</div>
</div>
</div>



which can be read as $2^3$.

Note that this operator also works on floats and float-integer combinations:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(4**0.5) #square root of 4

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2.0
```
</div>
</div>
</div>



## The Modulo Operator `%`
The modulo operator returns the remainder of the left number divided by the right:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(16%3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1
```
</div>
</div>
</div>



In mathematics this would be expressed as 

$16$ mod $3$.

This operator can also act on floats and integer-float combinations:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(16.3%3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1.3000000000000007
```
</div>
</div>
</div>



## The Floor Division Operator `//`
This returns the result of the left number divided by the right, but without the remainder:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(16//3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
5
```
</div>
</div>
</div>



Like the others this works for both integers and floats.



## Special Functions and Advanced Mathematics
For more complex mathematics involving logs, trigonometry, etc. we'll rely on the scientific packages SciPy and NumPy. We'll discuss these at a later stage.



## Multiple Operations in a Single Expression
Though we have only seen one operation or function used per line, you can combine as many as you'd like:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print( 2**3 + 4)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
12
```
</div>
</div>
</div>



If you want to group or control the order in which operations are executed use brackets. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print( (2 + 17//2)**5 )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
100000
```
</div>
</div>
</div>



where the `//` is applied first, then the `+` and lastly the `**`. We shall discuss the order in which operations and function calls are executed in Section.... Make a url

