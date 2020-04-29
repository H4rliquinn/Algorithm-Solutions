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
            pattern_match=pattern_lookup[patterns[x]]
        else:
            # Add pattern if not found
            pattern_lookup[patterns[x]]=strings[x]
            pattern_match=strings[x]

        # Look for String
        if string_lookup.get(strings[x],None):
            string_match=string_lookup[strings[x]]
        else:
            # Add string if not found
            string_lookup[strings[x]]=patterns[x]
            string_match=patterns[x]  
        # Match Strings and Patterns
        if string_match!=patterns[x] or pattern_match!=strings[x]:
            #Break if incorrect
            return False
    #Return True if no disparity found
    return True
