# You are given a string with repeated characters, your task is to rearrange the

# characters in the string so that no two adjacent characters are the same.

# Sample Input & Output

# bcaaa -> abaca

def rearrange(str):
    pass


# Amazon has a catalog of training courses. Each course has a unique String name and can have a dependency on
# previous courses that have to be taken before you can start a course.
#
# An example of a valid catalog might look like this:
# {
#     "Databases": ["Security", "Logging"]
#     "Security": ["Logging"]
#     "Logging": []
# }
# Your task is to write a validation function that will be invoked when someone updates the catalog. It must indicate
# whether the new catalog structure is valid or it contains errors.

def course_validation(courses):
    cycle, visited = set(), set() // {}, {}

    def dfs(crs):
        if crs in cycle:  # cycle = {}
            return False

        if crs in visited:  # visited = {}
            return True

        if not courses[crs]:  # [Sec..., Logging]
            return True

        cycle.add(crs)  # {Data}
        for pre in courses[crs]:
            if not dfs(crs):
                return False
        cycle.remove(crs)

        visited.add(crs)
        return True

    for crs in courses.keys():  # Databases
        if dfs(crs):  # dfs(Databases)
            return True

# course_validation(
# {
# "Databases": ["Security", "Logging"]
#  "Security": ["Logging"]
#     "Logging": []
#  })

#  course_validation(
# {
# "Databases": ["Security", "Logging"]
#  "Security": ["Logging"]
#     "Logging": ["Databases"]
#   }
#  )

#   course_validation(
# {
# "Databases": []
#  )

#    course_validation(
# {
# "Databases": [""]
# }
#  )

# Given a sum of money, compute the minimized combination of

# denominations required to equal that sum. Assume you only

# have the following denominations:

# 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01


def combination(denoms, targetSum):
    res = []  # 35.10 # res = [20], rem = 15.10 # res = [20, 10], rem = 5.10 # res = [20, 10, 5], rem = 0.10 # res = [20, 10, 5, 0.1], rem = 0
    index = 0
    rem = targetSum
    while index < len(denoms):
        if denoms[index] < rem:
            res.append(denoms[index])
            rem -= denoms[index]
        else:
            index += 1

        return res if rem == 0 else -1
    # [20, 10]
