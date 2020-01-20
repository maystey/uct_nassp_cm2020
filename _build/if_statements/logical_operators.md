---
redirect_from:
  - "/if-statements/logical-operators"
interact_link: content/if_statements/logical_operators.ipynb
kernel_name: python3
has_widgets: false
title: 'Logical Operators'
prev_page:
  url: /if_statements/comparison_operators
  title: 'Comparison Operators'
next_page:
  url: /data_structures/intro
  title: 'Data Structures'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Logical Operators

Logical operators act on booleans and return booleans. The logical operators are `and`, `or` and `not`. 

<!--- Maybe mention bitwise operations? Python doesn't expose these in the Standard Library afaik, but just so that they are aware of the difference -->



## Logical `and`



This acts on 2 booleans. It returns `True` if both booleans are `True` and `False` otherwise. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('True and True is', True and True)
print('True and False is', True and False)
print('False and True is', False and True)
print('False and False is', False and False)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
True and True is True
True and False is False
False and True is False
False and False is False
```
</div>
</div>
</div>



<!-- Add examples with comparison operators? Or do it all later? -->



## Logical `or`

This operator acts on 2 booleans. It returns `True` if at least one of the booleans is `True` and `False` if both booleans are `False`. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('True or True is', True or True)
print('True or False is', True or False)
print('False or True is', False or True)
print('False or False is', False or False)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
True or True is True
True or False is True
False or True is True
False or False is False
```
</div>
</div>
</div>



## Logical `not`
This operator acts on a single boolean. It returns the opposite of the boolean:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('not True is', not True)
print('not False is', not False)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
not True is False
not False is True
```
</div>
</div>
</div>



## Combining Logical Operations
Although logical operations only act on up to 2 booleans at a time, just like arithmetic operators they can be combined in a single statement. For example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print('True and False or True is ', True and False or True)
print('True or True and False is', True or True and False)
print(not True or True and False)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
True and False or True is  True
True or True and False is True
False
```
</div>
</div>
</div>



<!---The order in which the logical operators are executed if no brackets are used is: `not`, `and`, `or`.

If you want to control the order in which the operators execute you can use brackets: --->



Although it isn't important for the cases above, if you need to ensure a specific order for the operations you can use brackets to group them.

