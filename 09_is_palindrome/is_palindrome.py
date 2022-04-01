def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        Truei

        >>> is_palindrome('Noon')
        True
    """
    lst = list(phrase)
    lst.reverse()
    if ''.join(lst) == phrase:
        return True
    else:
        return False
