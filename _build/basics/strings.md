---
interact_link: content/basics/strings.ipynb
kernel_name: python3
has_widgets: false
title: 'Strings'
prev_page:
  url: /basics/functions
  title: 'Introduction to Functions'
next_page:
  url: /intro
  title: 'If Statements'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Strings

In this section we shall take a closer look at the string type and some of the operations associated with them. The following section makes heavy reference to Dr. Harrington's online notes....



## Concatenation `+`
For strings the `+` symbol is used to concatenate two strings together. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('One string' + ' and another')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
One string and another
```
</div>
</div>
</div>



## Duplication `*`
The duplication `*` operator takes a string and an integer and repeats the string as many times as the integer value:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('hello '*4)
print(2*'bye ')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hello hello hello hello 
bye bye 
```
</div>
</div>
</div>



## Indexing `[]`
Strings can be seen as a collection of characters. Each of these character has an integer index associated with it, based on it's position in the string. For example, take the string `'computer'`:



|---------|-|-|-|-|-|-|-|-|
character |c|o|m|p|u|t|e|r|
index     |0|1|2|3|4|5|6|7|



You can access individual characters in the string by index using:
```
string[index]
```
for example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
computer_string = 'computer'

print('Index 3:', computer_string[3])

print('Index 7:', computer_string[7])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Index 3: p
Index 7: r
```
</div>
</div>
</div>



If you use an index that is too large for the given string, Python will return an error:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('Index 11', computer_string[11])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-8-abeba3add71f> in <module>()
    ----> 1 print('Index 11', computer_string[11])
    

    IndexError: string index out of range


```
</div>
</div>
</div>



You can find the number of characters in a string using the `len()` function:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('There are', len(computer_string), 'characters in the string')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
There are 8 characters in the string
```
</div>
</div>
</div>



Notice how the length of `computer_string` is one greater than its largest index. This is because Python indexes from `0`.

Thus, if we don't know how long a string is before hand (if a variable holding a string is subject to change for instance) and we want to index the last value of the string, we could use `len() - 1` as the index:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('The last character:', computer_string[len(computer_string) - 1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
The last character: r
```
</div>
</div>
</div>



This method works, but Python gives us a far cleaner way of doing this: using an index of `-1`. This won't work for most other programming languages. 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('The last character:', computer_string[-1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
The last character: r
```
</div>
</div>
</div>



In general, negative indices in Python index the strings (and other objects) backwards:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('Second last character', computer_string[-2])

print('Third last character', computer_string[-3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Second last character e
Third last character t
```
</div>
</div>
</div>



Note that the index `-8` corresponds to the `0` index (`len(computer_string) - 8` is `0`) so anything less than this would be out of bounds.



## Slicing
Slicing allows us to extract segments of the string, as apposed to individual characters. The syntax for string slicing is:
```
string[start_index:stop_index]
```
where the `stop_index` is not included in the slice, rather the slice stops before this index. For example, consider the slice:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[2:5])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
mpu
```
</div>
</div>
</div>



where the last character is `'r'`, but the character with index `5` is `'t'`.

If we want to take a slice from the beginning of a string we could use `0` as the `start_index`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[0:3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
com
```
</div>
</div>
</div>



Alternatively if we left the `start_index` blank Python will interprate this as starting from the beginning of the string:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[:3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
com
```
</div>
</div>
</div>



Similarly if we wanted to take a slice up to and including the last character in the string, we can use: 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[3:len(computer_string)])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
puter
```
</div>
</div>
</div>



or simply leave the `stop_index` blank:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[3:])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
puter
```
</div>
</div>
</div>



Notice the slice above is not the same as if we used `-1` as the `stop_index`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[3:-1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
pute
```
</div>
</div>
</div>



even though the same rules apply as with indexing, the slice always stops **before** the `stop_index`.



We can use a third index when slicing as a step size:
```
string[start_index: stop_index: step_size]
```
For example, we can get every second character from a string using a step size of `2`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('Starting from 0:', computer_string[0:8:2])
print('Starting from 1:', computer_string[1:8:2])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Starting from 0: cmue
Starting from 1: optr
```
</div>
</div>
</div>



The step size can be any integer. Note that by default it is set to 1. As another example lets print out every second character from `computer_string` starting from the first:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[::3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
cpe
```
</div>
</div>
</div>



The step size need not be positive. If a negative step size is used the string will be sliced backwards. For example if we want to print out the whole of `computer_string` backwards:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(computer_string[::-1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
retupmoc
```
</div>
</div>
</div>



Note, when slicing with a negative step size you must ensure that `start_index` is greater than `stop_index`, otherwise your slice will be empty.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('Empty slice:', computer_string[0:6:-1])
print('Not empty slice:', computer_string[6:0:-1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Empty slice: 
Not empty slice: etupmo
```
</div>
</div>
</div>



Also notice how, in the second slice above, the `0` index character is not present. Even when slicing with a negative step size the `stop_index` is **not** included in the slice.



## String Formatting

