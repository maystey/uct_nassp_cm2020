---
redirect_from:
  - "/loops/list-comp"
interact_link: content/loops/list_comp.ipynb
kernel_name: python3
has_widgets: false
title: 'List Comprehension'
prev_page:
  url: /loops/for
  title: 'For Loops'
next_page:
  url: /loops/while
  title: 'While Loops'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# List Comprehension

There will be many times you will want to automate the creation of a list. You can use loops for this but can become impractical. A nice way to generate lists is using **list comprehension**:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#Generating a list of integers in ascending order
numbers = [i for i in range(6)]
print(numbers)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 1, 2, 3, 4, 5]
```
</div>
</div>
</div>



You can treat the `for` inside the list just like a `for` loop, including looping through collections:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
string = 'abcdefg'

#Generating a list of characters from a string
char_list = [char for char in string]
print(char_list)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
</div>
</div>
</div>



Only use list comprehension if you are interested in the list itself. Do not use it in place of a `for` loop.



You can also embed list comprehension: 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print([[i + j for j in range(3)] for i in range(4) ])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
```
</div>
</div>
</div>

