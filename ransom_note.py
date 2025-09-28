def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Build frequency dictionary for magazine characters
    letter_counts = {}
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # Check each character in ransomNote
    for char in ransomNote:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1  # use one occurrence

    return True
