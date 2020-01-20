---
redirect_from:
  - "/data-structures/tuple"
interact_link: content/data_structures/tuple.ipynb
kernel_name: python3
has_widgets: false
title: 'Tuple'
prev_page:
  url: /data_structures/intro
  title: 'Data Structures'
next_page:
  url: /data_structures/lists
  title: 'Lists'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Tuple

Just as strings are a sequence of characters, tuples are a sequence of objects. This makes their use far more general.

You can set a tuple by separating the objects using commas. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
t = 1, 2, 3, 'a', 'b', 'c'

print(t)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
(1, 2, 3, 'a', 'b', 'c')
```
</div>
</div>
</div>



This is called tuple packing.

You can also put brackets around the objects, which is useful if you need to instance a list and use it in the same line (for example as a function argument):



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(('a', 1, 'b', 2, 'c', 3))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('a', 1, 'b', 2, 'c', 3)
```
</div>
</div>
</div>



Like strings, tuples can be indexed and sliced:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('Index 3:', t[3])
print('Slice from index 3:', t[3:])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Index 3: a
Slice from index 3: ('a', 'b', 'c')
```
</div>
</div>
</div>



Tuples are also immutable (like strings):



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
t[2] = 5

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-5255d5d095a8> in <module>
    ----> 1 t[2] = 5
    

    TypeError: 'tuple' object does not support item assignment


```
</div>
</div>
</div>



You can unpack a tuple into multiple variables, just like you can pack multiple values into a tuple:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
t = (1, 2, 3)
print('t is ', t)

x, y, z = t
print('x is', x) 
print('y is', y)
print('z is', z)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
t is  (1, 2, 3)
x is 1
y is 2
z is 3
```
</div>
</div>
</div>

