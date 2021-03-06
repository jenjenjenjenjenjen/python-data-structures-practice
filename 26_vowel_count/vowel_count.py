def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    frequency = {}
    for vowel in 'aeiou':
        vowel_count = 0
        for letter in phrase.lower():
            if vowel == letter:
                vowel_count += 1
                frequency[vowel] = vowel_count
    return frequency
