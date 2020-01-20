---
redirect_from:
  - "/data-structures/dictionaries"
interact_link: content/data_structures/dictionaries.ipynb
kernel_name: python3
has_widgets: false
title: 'Dictionaries'
prev_page:
  url: /data_structures/lists
  title: 'Lists'
next_page:
  url: /loops/intro
  title: 'Loops'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Dictionaries

So far we have only looked at sequence data structures, where elements are referred to by their position in the sequence. In dictionaries, however, the objects stored are referred to by a key. Keys must be an immutable type, for example a string, number or tuple containing only immutable types.

You can create a dictionary using the `dict` function; and assign values using the subscript notation: <!--- Look this up. Introduce earlier. Make a glossary! -->
```
dictionary[key] = value
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d = dict()

d[1] = 'a'
d['lst'] = [1, 2, 3]

print(d)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{1: 'a', 'lst': [1, 2, 3]}
```
</div>
</div>
</div>



You can also access dictionary values using the subscript notation:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(d[1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
a
```
</div>
</div>
</div>



An alternative way to initialize a dictionary with key-value pairs is:
```
{key1 : value1, key2 : value2}
```
much like it appears in the print output:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
d = {1 : 'a',  'lst' : [1, 2, 3]}

print(d)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{1: 'a', 'lst': [1, 2, 3]}
```
</div>
</div>
</div>



Note that using a key that doesn't exist in the dictionary will give you a `KeyError`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(d[2])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-5-c8f93a31d4a2> in <module>
    ----> 1 print(d[2])
    

    KeyError: 2


```
</div>
</div>
</div>



## Listing the Keys Which Exist

Often you will want a list of the keys which a dictionary has. For this you can use the `dict.keys()` method:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(d.keys())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
dict_keys([1, 'lst'])
```
</div>
</div>
</div>



One use for this is to check if a dictionary has the key you're looking for if you want to avoid an error:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
if 2 in d.keys():
    print(d[2])
else:
    print(2, 'not a key in d')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2 not a key in d
```
</div>
</div>
</div>

