---
interact_link: content/loops/while.ipynb
kernel_name: python3
has_widgets: false
title: 'While Loops'
prev_page:
  url: /loops/list_comp
  title: 'List Comprehension'
next_page:
  url: /loops/break
  title: 'Breaking Out of Loops'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# While Loops

For loops are useful if you know what you want to iterate over, but what if you wanted to keep looping until a certain condition is met? `while` loops are the tool for this job.

<!--- Give an example problem that isn't exactly solvable using a for loop -->



The syntax for a `while` loop is:
```
while condition:
    block of code to be repeated
```

where `condition` is/evaluates to a boolean value. The loop will keep repeating, executing the block of code indented after the `:` as long as `condition` evaluates to `True`. When `condition` evaluates to `False` the loop will no longer be repeated and control will progress to the code after the loop. <!--- is control the correct term here? --> Note that if `condition` starts as `False`, the code inside the loop will never be executed.

<!-- example -->



Something to be careful of when using `while` loops is a loop that doesn't stop looping. If `condition` never evaluates to `False`, or if you never break out of the loop in another way, control will never leave the loop. Sometimes it is useful to use a maximum number of loop iterations to avoid this:
```
counter = 0

while condition and counter < max_count:
    block of code
```

where `max_count` is the chosen maximum number of recursions (normally chosen as a very large number). <!--- rather give a concrete example -->



`while` loops can be used to replace for `loops` (though this is more cumbersome, especially in the case of looping through a collection):

<!--- For loop followed by identical while loop -->

