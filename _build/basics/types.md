---
interact_link: content/basics/types.ipynb
kernel_name: python3
has_widgets: false
title: 'Type Conversion'
prev_page:
  url: /basics/comments
  title: 'Comments'
next_page:
  url: /basics/operators
  title: 'Operators'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Type Conversion

So far we have looked at three variable types: integers, floats and strings; and how to check what type a variable is.

Sometimes we want to convert between different variable types. To do this we can use the `int`, `float` and `str` functions:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
int_var = 1
print(int_var, type(int_var))

float_var = float(int_var)
print(float_var, type(float_var))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 <class 'int'>
1.0 <class 'float'>
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
float_var = 5.7
print(float_var, type(float_var))

int_var = int(float_var)
print(int_var, type(int_var))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
5.7 <class 'float'>
5 <class 'int'>
```
</div>
</div>
</div>



Note that when you convert a float to an integer Python does simply discards the decimal part (if you wish to round-off a float you can use the `round` function).<!--- link docs?-->



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
str_var = '1.43'
print(str_var, type(str_var))

float_var = float(str_var)
print(float_var, type(float_var))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1.43 <class 'str'>
1.43 <class 'float'>
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
str_var = '12'
print(str_var, type(str_var))

int_var = int(str_var)
print(int_var, type(int_var))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
12 <class 'str'>
12 <class 'int'>
```
</div>
</div>
</div>



Note that anything other than a number cannot be converted from a string to a float or int:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
str_var = 'not a number'
print(str_var, type(str_var))

float_var = float(str_var)
print(float_var, type(float_var))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
not a number <class 'str'>
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-9-4224f055b9d6> in <module>
          2 print(str_var, type(str_var))
          3 
    ----> 4 float_var = float(str_var)
          5 print(float_var, type(float_var))


    ValueError: could not convert string to float: 'not a number'


```
</div>
</div>
</div>



Even strings that contain a number with a decimal part cannot be converted to an integer:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
str_var = '4.563'
print(str_var, type(str_var))

int_var = int(str_var)
print(int_var, type(int_var))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
4.563 <class 'str'>
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-10-a3094efdeb44> in <module>
          2 print(str_var, type(str_var))
          3 
    ----> 4 int_var = int(str_var)
          5 print(int_var, type(int_var))


    ValueError: invalid literal for int() with base 10: '4.563'


```
</div>
</div>
</div>

