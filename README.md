# Trivia Kata for Python 3

This is basically a copy of https://github.com/jbrains/trivia/ except that it's
just the Python one, and I changed it to be used with Python 3.

## How to setup:

Create a virtualenv with Python 3.* (tested in Python3.6) and install `pytest`.

## How to run:

Just use the `Makefile`:

- `make` to run unit tests
- `make gold` to run golden test

Alternatively, read the Makefile and execute the commands inside, it's just 4 lines.

## How to kata this kata:

This is a Refactoring Kata, you get some code that could be improved and what
you do is write some code and refactor until can't do it anymore.

I will leave a golden test, but it's a good exercise to write them yourself,
there's also a failing unit test that you can fix and start hacking on.
