"""
Share
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
"""
class Solution:
    def reformat(self, s: str) -> str:
        # Edge Case
        if len(s)==0:
            return ""
        # Prep string 
        news=list(s)
        
        # Set first char type
        if news[0].isdigit():
            front_type="d"
        else:
            front_type="l"
        last_type=None
        
        #Iterate through string
        for x in range(len(news)):
            if news[x].isdigit():
                curr_type="d"
            else:
                curr_type="l"
            
            # Check if repeat type
            if curr_type==last_type:
            # Move the type if repeat 
            # If safe to push to front do that
                if curr_type!=front_type:
                    news.insert(0,news.pop(x))
                    front_type=curr_type
                # Else push to end
                else:
                    news.append(news.pop(x))
        # Return joined String
        return "".join(news)