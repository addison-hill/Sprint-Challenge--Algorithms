'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# What is base case???

# What is a way we can compare two letters at a time to check if they are 'th'?

# Inner recursive function???

# Test inputs : "", "abcthxyz", "abcthefthghith", "thhtthht", "THtHThth"

# So we can check to see if the last two are 'th', then move all the way to the front comparing two each time, until we hit base case.


def count_th(word):
    count = 0

    def recurr(word):
        if len(word) < 2:
            return

        if word[-2:] == "th":  # if last two letters in range are 'th'
            nonlocal count
            count += 1
            # call function without last two items you just compared
            recurr(word[:-2])
        else:
            # if last two aren't 'th' dont need them. but -2 could be h, so just dont use last letter.
            recurr(word[:-1])

    recurr(word)  # calling inner recursive function
    return count
