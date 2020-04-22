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
        curr_type=None
        #Iterate through string
        x=0
        while x<len(news):
        # for x in range(len(news)):
            # print(news,curr_type,last_type,x)
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
                # print(news,curr_type,last_type,x)
            else:
                x=x+1
                last_type=curr_type
        # Return joined String if successfull
        
        # print(news)
        if news[-1].isdigit()==news[-2].isdigit():
            return ""
        if news[-1].isalpha()==news[-2].isalpha():
            return ""
            
        return "".join(news)