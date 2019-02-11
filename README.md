![testing](https://travis-ci.com/lucasgcb/unitTesting.svg?branch=master)

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
