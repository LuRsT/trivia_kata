# Trivia Kata for Python 3

This is a copy of https://github.com/jbrains/trivia/ except that it's
just the Python one, and I changed it to be used with Python 3.

## Pre-requisites:

- Install `uv` if you don't have it.

## How to run:

- `make` to run unit tests
- `make gold` to run golden test

Alternatively, read the Makefile and run the commands inside.

## How to kata this kata:

This is a Refactoring Kata, you get some code that could be improved and what
you do is write some code and refactor until can't do it anymore.

I will leave a golden test, but it's a good exercise to write them yourself,
there's also a failing unit test that you can fix and start hacking on.

Text taken from: http://legacycoderetreat.typepad.com/

### More guided practice

I run Legacy Code Retreat with more guidance than a typical Code Retreat. I have so far used these exercises in this sequence:

- Do anything you like, but try to add tests changing the code as little as you can.
- Use the Golden Master technique to generate characterisation tests (I make this a 20-minute iteration and explain the exercise below).
- Practise using the Subclass to Test refactoring.
- Practise using Subclass to Test, followed immediately by Replace Inheritance with Delegation.
- Practise extracting Pure Functions, that is, functions with no side effects. (Be careful! You think there's no side effects, but if can't mark the function as abstract/class-level, then there might still be side effects!)

As always, write whatever tests will help you do these things safely and correctly. Whatever you do, do what you don't normally do!

After each iteration, throw away your changes except for the Golden Master
exercise. I recommend that people keep their Golden Master to help them with
the other exercises.

For the last two iterations of the day, keep the changes after iteration 1, but
switch partners.
