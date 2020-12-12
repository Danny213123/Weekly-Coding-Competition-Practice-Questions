# Spam or not?

Somehow, your phone number got leaked on the internet and a bunch of spam companies have picked it up. You are tired of constantly getting spam calls, and want to make a bot to hang up automatically when a spam number calls. You noticed that spam numbers contain at least one of the following:

Number starts with 800
Number starts with 909
Last 4 numbers are a palindrome (ie. 4004, 5225)
the 4th to 6th numbers are all the same (ie. 6813332808, 2017773459)
The input will always be 10 integers long, like a standard phone number (no dashes or brackets, just plain numbers)
The output will be either a "yes" or a "no"

Test Cases:

    INPUT: 2003432089
    OUTPUT: no

    INPUT: 8003002000
    OUTPUT: yes

    INPUT: 6473840990
    OUTPUT: yes

    INPUT: 4167772008
    OUTPUT: yes

    INPUT: 4167892323
    OUTPUT: no

    INPUT: 9096782340
    OUTPUT: yes

    INPUT: 6369091111
    OUTPUT: yes

    INPUT: 4168085218
    OUTPUT: no

    INPUT: 2009999818
    OUTPUT: yes

    INPUT: 9003012020
    OUTPUT: no

This question is very similar to one that was on the Junior level CCC a few years back, so this will be some good practice! I suggest trying it in various languages to see what is the fastest way to solve it.
