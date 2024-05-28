# Initialization
# Start with an empty result list: res = [].
# Define the dfs function that performs depth-first search to build subsets.
# Initial Call
# Call dfs(0, []).
# First Call to dfs(0, [])
# Add the empty subset to res: res = [[]].
# Iterate over elements starting from index 0:
# For j = 0 (element 1), call dfs(1, [1]).
# Second Call to dfs(1, [1])
# Add subset [1] to res: res = [[], [1]].
# Iterate over elements starting from index 1:
# For j = 1 (element 2), call dfs(2, [1, 2]).
# Third Call to dfs(2, [1, 2])
# Add subset [1, 2] to res: res = [[], [1], [1, 2]].
# Iterate over elements starting from index 2:
# For j = 2 (element 3), call dfs(3, [1, 2, 3]).
# Fourth Call to dfs(3, [1, 2, 3])
# Add subset [1, 2, 3] to res: res = [[], [1], [1, 2], [1, 2, 3]].
# i = 3, which is beyond the length of nums, so return to the previous call dfs(2, [1, 2]).
# Back to Third Call dfs(2, [1, 2])
# Continue iterating over elements starting from index 2:
# No more elements to include, so return to the previous call dfs(1, [1]).
# Back to Second Call dfs(1, [1])
# Continue iterating over elements starting from index 1:
# For j = 2 (element 3), call dfs(3, [1, 3]).
# Fifth Call to dfs(3, [1, 3])
# Add subset [1, 3] to res: res = [[], [1], [1, 2], [1, 2, 3], [1, 3]].
# i = 3, which is beyond the length of nums, so return to the previous call dfs(1, [1]).
# Back to Second Call dfs(1, [1])
# Continue iterating over elements starting from index 1:
# No more elements to include, so return to the initial call dfs(0, []).
# Back to First Call dfs(0, [])
# Continue iterating over elements starting from index 0:
# For j = 1 (element 2), call dfs(2, [2]).
# Sixth Call to dfs(2, [2])
# Add subset [2] to res: res = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]].
# Iterate over elements starting from index 2:
# For j = 2 (element 3), call dfs(3, [2, 3]).
# Seventh Call to dfs(3, [2, 3])
# Add subset [2, 3] to res: res = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]].
# i = 3, which is beyond the length of nums, so return to the previous call dfs(2, [2]).
# Back to Sixth Call dfs(2, [2])
# Continue iterating over elements starting from index 2:
# No more elements to include, so return to the initial call dfs(0, []).
# Back to First Call dfs(0, [])
# Continue iterating over elements starting from index 0:
# For j = 2 (element 3), call dfs(3, [3]).
# Eighth Call to dfs(3, [3])
# Add subset [3] to res: res = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]].
# i = 3, which is beyond the length of nums, so return.
# Completion
# All elements have been processed. The final res contains all subsets:

# []
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 3]
# [2]
# [2, 3]
# [3]
# Generation of [1, 3]
# The subset [1, 3] is generated as follows:

# In the second call to dfs(1, [1]), after completing the exploration starting with [1, 2], the loop continues with j = 2.
# The element 3 is added to the subset [1], resulting in [1, 3].
# The dfs function is called with dfs(3, [1, 3]), adding [1, 3] to the result list.
# This backtracking approach ensures that all combinations are explored, including [1, 3].