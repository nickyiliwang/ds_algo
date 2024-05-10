# https://www.youtube.com/watch?v=-Cjgt5I0YvM
# https://stackoverflow.com/questions/58715870/explanation-about-dummy-nodes-and-pointers-in-linked-lists


# The crucial thing here is that when you set a Python variable to an object, it's a reference to that object, not a copy of that object. So in this code here:

# dummy = cur = ListNode(0)
# # cur = 0
# # dummy = 0
# dummy and cur both point to the same object (i.e. the same single-element list). When you append your other list to cur, you're simultaneously appending it to dummy because it's the same list.

# Box-and-pointer diagram:

# dummy
#   |
#   v
# /---\
# | 0 |
# \---/
#   ^
#   |
#  cur
# When you do this:

# cur = cur.next
# # cur = 1->4->5
# # dummy = 0->1->4->5
# you're not creating a new list, you're just iterating your cur pointer down the existing list. Both pointers are part of the same list, but dummy points to the first element and cur points to the second element.

# Box-and-pointer diagram:

# dummy
#   |
#   v
# /---\    /---\    /---\    /---\
# | 0 |--->| 1 |--->| 4 |--->| 5 |
# \---/    \---/    \---/    \---/
#            ^
#            |
#           cur
# Each time you call ListNode() you're creating a new node, so if you want to create two nodes with the same value, you need to call the initializer twice:

# dummy = ListNode(0)
# cur = ListNode(0)
# # cur and dummy both have values of 0, but they're different list objects!
# dummy
#   |
#   v
# /---\
# | 0 |
# \---/


# /---\
# | 0 |
# \---/
#   ^
#   |
#  cur
# Also: I'm not sure if this is what you were getting at when you mentioned "dummy nodes", but note that there is no particular need for a special "dummy node" in your list to signify the end of the list; None serves that purpose just fine (i.e. the end of the list is the one whose next is None).