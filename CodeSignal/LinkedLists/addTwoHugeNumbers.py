# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def addTwoHugeNumbers(a, b):

    def returnInt(ll):
        str_a=''
        while ll is not None:
            val=str(ll.value)
            str_a+=f'{"0"*(4-len(val))}{val}'
            ll=ll.next
        return str_a

    res=str(int(returnInt(a))+int(returnInt(b)))
    
    resll=None    
    while len(res)>4:
        if resll is None:
            resll=ListNode(int(res[-4:]))
            res=res[:-4]
        else:
            new_node=ListNode(int(res[-4:]))
            new_node.next=resll
            resll=new_node
            res=res[:-4]
    new_node=ListNode(int(res))
    new_node.next=resll
    resll=new_node
    return resll