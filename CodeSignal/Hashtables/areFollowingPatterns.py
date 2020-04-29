"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""
def areFollowingPatterns(strings, patterns):
    # Create Hash to save pattern
    pattern_lookup={}
    string_lookup={}
    # Loop through strings
    for x in range(len(strings)):
        # Look for pattern
        if pattern_lookup.get(patterns[x],None):
            match=pattern_lookup[patterns[x]]
        else:
            # Add pattern if not found
            pattern_lookup[patterns[x]]=strings[x]
            match=strings[x]
        # Match to pattern
        print(strings[x],match)
        if strings[x]!=match:
            #Break if incorrect
            return False
    #Return True if no disparity found
    return True
