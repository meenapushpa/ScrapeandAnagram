# Anagram

## What is Anagram?
An anagram is a word formed by rearranging the letters of a different word, for example state and taste are
anagrams of each other, as are damned, demand and madden.

## What is the requirement ?

Construct a function written in Python that, given a list of words, returns a dictionary whose keys are the letters
of a word sorted into alphabetical order and whose values are lists of all the words with that key.
    
    Example:
          
          A key-value pair might be:
          ‘aestt’: [‘state’, ‘taste’]

Write a Python script that uses words.txt to find and print the anagram with the largest number of variants.
Also find and print the longest pair of words that are anagrams of each other.


## How do I configure workstation to run this program?

* Install Python 3.6 in your workstation, please refer this [link](https://www.python.org/downloads/) for more info

* Create virtual envuironment (Windows) 
     
     `python -m venv venv`                   

* Activate the virtualenv (Windows)       

     `Source venv/Scripts/activate`
* The default modules are used in this program,they are datetime,csv,collections,os,unittest

## How to run this program ?

This program is using default collections module, Hence no module is require to install. Please Note, that line number 6 needs change according to your words.txt location.

`python anagram.py`

*Sample output*

![Test Image 1](/output.png)
