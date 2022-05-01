from test_framework import generic_test
import collections

<<<<<<< HEAD
def can_form_palindrome(s):
    return sum([v % 2 for v in collections.Counter(s).values()]) <= 1
=======
def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    return True
>>>>>>> b736406dfb6e8e6be2612e8a57e710baf90a2d3e


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
