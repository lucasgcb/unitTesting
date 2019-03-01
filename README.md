Circle CI: [![CircleCI](https://circleci.com/gh/lucasgcb/unitTesting.svg?style=svg)](https://circleci.com/gh/lucasgcb/unitTesting)
Travis CI: [![Build Status](https://travis-ci.org/lucasgcb/unitTesting.svg?branch=master)](https://travis-ci.org/lucasgcb/unitTesting)

Coveralls: [![Coverage Status](https://coveralls.io/repos/github/lucasgcb/unitTesting/badge.svg?branch=master)](https://coveralls.io/github/lucasgcb/unitTesting?branch=master)
Code Conv: [![codecov](https://codecov.io/gh/lucasgcb/unitTesting/branch/master/graph/badge.svg)](https://codecov.io/gh/lucasgcb/unitTesting)
## About

A simple unit test suite for some basic functions.

[mydivpack](https://github.com/lucasgcb/unitTesting/tree/master/mydivpack) and [mysumpack](https://github.com/lucasgcb/unitTesting/tree/master/mysumpack) contain some generic code for adding and dividing lists of numbers. These can be used for anything.

[tests](https://github.com/lucasgcb/unitTesting/tree/master/tests) have a few _unit test_ cases for the generic code in this repository. It is clear that in computing, a certain input will always have a certain output, so the `pytest`suite will run the generic code against defined cases for these inputs awaiting a certain output or convergence of such an output. If the results deviate from what is expected, then the code is acting in an unexpected way and is thereby failing the build test.

The tests may be run locally using `python -m pytest`.

To automate this, Continuous Integration platforms such as [Circle CI](https://circleci.com/) and [Travis CI](https://travis-ci.org/) offers cloud environments for observing this repository and running the tests.

[Coveralls](https://coveralls.io/) and [CodeConv](https://codecov.io/) are services that lets us know how much of our code is Covered for tests. 





## About Testing

"Testing", in general programming terms, is the practice of writing code (separate from your actual application code) that invokes the code it tests to help determine if there are any blaring errors. 
- It does not prove that code is correct
- It merely reports if the conditions the tester thought of are handled correctly.
- Always referring to "automated testing", where the tests are run by the machine. 
- "Manual testing", where a human runs the program and interacts with it to find bugs, is a separate subject. 

"Unit  Testing" is a level of software testing where individual components of a software are tested. 
-  A unit is the smallest testable part of any software. 
-  One or a few inputs and usually a single output. 
-  Tests validate that each unit performs as designed.
-  A unit may be an individual program, function, procedure, etc. 
-  In object-oriented programming, the smallest unit is a method


![unittesting](http://softwaretestingfundamentals.com/wp-content/uploads/2010/12/unittesting.jpg)

----

## Structure

This repository has the following structure:
```
.
├── mydivpack
│   ├── divs.py
│   └── __init__.py
├── mysumpack
│   ├── __init__.py
│   └── sums.py
├── README.md
├── testingExamples
│   ├── test2_sum.py
│   ├── test_sum.py
│   └── test_sum_unitTest.py
├── tests
│   ├── context.py
│   ├── test_div_pytest.py
│   └── test_sum_unittest.py
└── travis.yml
```
testingExamples are examples with the `unittest` framework.
tests are working examples with both `pytest` and `unittest`
