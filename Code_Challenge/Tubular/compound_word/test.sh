#!/usr/bin/env sh

cat input.txt | python CompoundWordFinder.py | diff answer.txt -