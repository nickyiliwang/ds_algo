How to implement a backtracking algorithm
Draw the tree, draw the tree, draw the tree!!!
Draw a state-space tree to visualize the problem. A small test case that's big enough to reach at least one solution (leaf node). We can't stress how important this is. Once you draw the tree, the rest of the work becomes so much easier - simply traverse the tree depth-first.

When drawing the tree, bear in mind:

how do we know if we have reached a solution?
how do we branch (generate possible children)?
Then, apply the following backtracking template:

```py
function dfs(start_index, path):
  if is_leaf(start_index):
    report(path)
    return
  for edge in get_edges(start_index):
    path.add(edge)
    dfs(start_index + 1, path)
    path.pop()
```

`start_index` is used to keep track of the current level of the state-space tree we are in.

`edge` is the choice we make; the string a, b in the above state-space trees.

The main logic we have to fill out are

`is_leaf`
`get_edges`
which correspond to the two questions above.

Notice how very similar this is to the Ternary Tree Path code we've seen in DFS with States module. That problem has an explicit tree. For combinatorial search problems, we have to find our own tree.

Note that the is_leaf and get_edges helper functions can be just one line of code, in which case it wouldn't be necessary to separate into another function.

Time and space complexity
We visit each node of the state-space tree exactly once so the time complexity of a backtracking algorithm is proportional to the number of nodes in the state-space tree. The number of nodes in a tree can be calculated by multiplying number of children of each node ^ height of the tree.

The space complexity of a backtracking algorithm is typically the height of the tree because that's where the DFS recursive call stack is of maximum height and uses the most memory.

```
Combinatorial Example Problem
Given a non-negative integer n, find all n-letter words composed by 'a' and 'b', return them in a list of strings in lexicographical order.

Input: 2
Output: ["aa", "ab", "ba", "bb"]

Input: 4
Output: ["aaaa", "aaab", "aaba", "aabb", "abaa", "abab", "abba", "abbb", "baaa", "baab", "baba", "babb", "bbaa", "bbab", "bbba", "bbbb"]
```
