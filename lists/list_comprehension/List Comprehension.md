# List Comprehension

## List Comprehension:
**Is an elegant way to define and create lists based on existing list.**

## List Comprehension:
**is generally more compact and faster than normal functions and loops for creating list.**

### Remember: **Every list comprehension can be Rewritten in for loop, but  every for loop can't be Rewritten in the form of List Comprehension**

> Suppose, we want to separate the letters of the word 'Human' and add the letters as items of a list. The first thing that comes in mind would be using for loop.

*Syntax:*
`[Expression for item in list]` = 
`[letter for letter in 'human']`

> If you Noticed `human` is a string, not a list.
> This is the power of `List Comprehension.`

> It can identify when it receive a string or a tuple and work on it like a list.
