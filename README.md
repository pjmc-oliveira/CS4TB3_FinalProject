Group 5 Final Project
=========================================
**Team Name:**  Group 5<br/>
**Team Members:** Pedro Oliveira, Zak Ahmed, Piranaven Selva


## What is it? 
The project for the course COMP SCI 4TB3 - Syntax Based Tools and Compilers will be to apply the knowledge gained from the course. Group 5, comprised of Pedro, Piranaven \& Zak will work together to enhance Python.
Python is one of the most beloved programming languages. It contains a plethora of syntax that enables its users to achieve their goals.  
However, it does not contain a handful of syntax that we believe would enrich the programming language and provide developers with more flexibility. 
These language constructs are Increment, Decrement, Until, Unless, Do-While Loops, & Switch-Case Statements. These enhancements, although not necessarily pythonic, would undoubtedly strengthen a developers toolkit



-------------------------------------------------
### How to Use?
-------------------------------------------------

##Setup Requirements 
(Would recommend running on VM or AWS instance)
- Ensure you have gcc installed
- Ensure you are able to call the commands make, configure, git
- Clone the repo


- Navigate to the directory src/cpython
- run `bash./configure` (This will create your Makefile)
- run `make`( An executable will be created)
- run `./python <LOCATION OF TEST i.e : /group-05-final-project/src/test/testSet.py>`
 VOLILA!

-------------------------------------------------
### Summary of File's Modified 
-------------------------------------------------

Additions:
- src/test/testSet.py

From src/cPython:

- Grammar/Grammar
- Python/ast.c
- Python/symtable.c 
- Python/compile.c
- Ptyhon/ceval.c
- Parser/Python.asdl
- Parser/tokenizer.c
- Include/token.h
- Lib/lib2to3/tests/data/py3_test_grammar.py

Auto-Generated Files we had to verify:

- Include/graminit.h
- Include/Python-ast.h
 - Python/Python-ast.c
 - Python/graminit.c

-------------------------------------------------
### Summary of Folder Structure and File Contents 
-------------------------------------------------

**Doc** <br/>
Documentation for the project
- Development Plan
- Poster

**Resources** 
  - Research Material used as foundations for the project

**src**
- cpython
- test
  

LICENSE
  - License information
  
README.md
  - This file
