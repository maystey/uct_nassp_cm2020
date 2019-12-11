---
redirect_from:
  - "/if-statements/comparison-operators"
interact_link: content/if_statements/comparison_operators.ipynb
kernel_name: python3
has_widgets: false
title: 'Comparison Operators'
prev_page:
  url: /if_statements/bools
  title: 'Booleans'
next_page:
  url: /if_statements/logical_operators
  title: 'Logical Operators'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Comparison Operators
Comparison operators operate on two variables and return a boolean result.



## Less-than `<` and  Greater-than `>`
These operators act in the same way as the mathematical objects you are familiar with. If `a` is less than `b`, then `a < b` will return `True` and `a > b` will return `False`. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('3 > 2 is', 3 > 2)
print('2.54 < 1 is', 2.54 < 1)
print('1 < 1 is', 1 < 1)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
3 > 2 is True
2.54 < 1 is False
1 < 1 is False
```
</div>
</div>
</div>



Note that these operators act on both integers and floats interchangeably.



## Less-than-equal-to `<=` and Greater-than-equal-to `>=`

As there names suggest, the `<=` operator is related to the $\leq$ assertion in mathematics. Similarly `>=` is related to $\geq$.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('3.3 < 3.4 is', 3.3 <= 3.4)
print('2 <= 2 is', 2 <= 2)
print('2 >= 3.4 is', 2 >= 3.4)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
3.3 < 3.4 is True
2 <= 2 is True
2 >= 3.4 is False
```
</div>
</div>
</div>



## Equals-to `==`
The `==` operator is used to check equality. When used on numbers, this is similar to the mathematical $=$.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('3 == 2 is', 3==2)
print('5.3 == 5.3 is', 5.3 == 5.3)
print('6 == 6.0 is', 6 == 6.0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
3 == 2 is False
5.3 == 5.3 is True
6 == 6.0 is True
```
</div>
</div>
</div>



The `==` operator is used more generally to compare non-numerical values. For example, it can be used to compare two strings:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print("'apple' == 'apple' is", 'apple' == 'apple')
print("'banana' == 'apple' is", 'banana' == 'apple')
print('''"banana" == 'banana' is''', "banana" == 'banana')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
'apple' == 'apple' is True
'banana' == 'apple' is False
"banana" == 'banana' is True
```
</div>
</div>
</div>



## Not-equal-to `!=`
This operator returns `True` if the two objects being compared aren't equivalent (if `==` would return `False`). For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('3 != 2 is', 3 != 2)
print('7.3 != 7.3 is', 7.3 != 7.3)
print("'apple' != 'banana' is", 'apple' != 'banana')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
3 != 2 is True
7.3 != 7.3 is False
'apple' != 'banana' is True
```
</div>
</div>
</div>



## in

