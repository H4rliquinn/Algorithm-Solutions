"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""
def areFollowingPatterns(strings, patterns):
    # Create Hash to save pattern
    pattern_lookup={}
    # Return True unless pattern fails
    same=True

    # Loop through strings
    for x in range(len(strings)):
        # Look for pattern
        if pattern_lookup.get(patterns[x],None):
            match=strings[x]
            # Add pattern if not found

        # Match to pattern
    
    # Return result
    return same
