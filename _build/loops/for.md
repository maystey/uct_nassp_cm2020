---
interact_link: content/loops/for.ipynb
kernel_name: python3
has_widgets: false
title: 'For Loops'
prev_page:
  url: /loops/intro
  title: 'Loops'
next_page:
  url: /loops/for_examples
  title: 'For Loop Examples'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# For Loops

For loops can be used to repeat a block of code by iterating through specified values.

The structure of a for loop is as follows:

```
for i in iterator:
    code block to be repeated
```

where `i` is the iteration variable and the iterator represents a collection of values that `i` will be set to each time the loop is repeated. Here `i` can be treated like a variable and can take on any allowed variable name.

The code block to be repeated must be indented after the `:`. The loop repeats until `i` has run through all of the values in the iterator, or until the loop is broken.

Be careful not to alter the iterator inside the code block being repeated.



## Worked Example
As a simple example, let's say we wanted to print out the first $n$ integer squares starting with 0.

This can be achieved manually for small $n$, for example $n = 5$:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('0 squared is', 0**2)
print('1 squared is', 1**2)
print('2 squared is', 2**2)
print('3 squared is', 3**2)
print('4 squared is', 4**2)
print('5 squared is', 5**2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0 squared is 0
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
```
</div>
</div>
</div>



This quickly becomes tedious and produces messy code. To achieve the same goal using a `for` loop we can do the following:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for i in range(6):
    print(i, 'squared is', i**2)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0 squared is 0
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
```
</div>
</div>
</div>



Here we have made use of the `range` function to create our iterator.



## The `range()` Function





## Looping Through Collections
<!--- I need to introduce lists somewhere else! Maybe in basics along with dictionaries? -->

Collections such as lists and strings can also be used as iterators. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for char in 'This string':
    print(char)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
T
h
i
s
 
s
t
r
i
n
g
```
</div>
</div>
</div>



and



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
for item in [1, 2, 3, 'a', 'b', 'c']:
    print(item)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1
2
3
a
b
c
```
</div>
</div>
</div>

