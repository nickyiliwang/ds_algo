def cakes(recipe, available):
    res = []
    if len(recipe) > len(available):
        return 0
    
    for inge in recipe:
        if inge in available and recipe[inge] <= available[inge]:
            res.append(available[inge] // recipe[inge])
        else:
            return 0
    return min(res)


print(
    cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
)
