'''
At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set.
For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize.
Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
'''

def minRecipes(preferences: dict[int, list[int]]) -> int:
    def rMinRecipes(drink_list: dict[int, set[int]], num_patrons: int, drinks_used: set[int]=set(), patrons_served: set[int]=set()) -> int:
        # All patrons served.
        if len(patrons_served) == num_patrons:
            return len(drinks_used)
        
        min_drinks = len(drink_list.keys())
        for drink, patrons in drink_list.items():
            if drink not in drinks_used:
                min_drinks = min(min_drinks, rMinRecipes(drink_list, num_patrons, drinks_used.union({drink}), patrons_served.union(patrons)))

        return min_drinks
            
    # Reorder by drinks as the keys and sets of patrons as the values.
    drink_list = dict()
    for patron, drinks in preferences.items():
        for d in drinks:
            if d not in drink_list:
                drink_list[d] = set()
            drink_list[d].add(patron)

    return rMinRecipes(drink_list, len(preferences.keys()))

if __name__ == "__main__":
    preferences = {
        0: [0, 1, 3, 6],
        1: [1, 4, 7],
        2: [2, 4, 7, 5],
        3: [3, 2, 5],
        4: [5, 8]
    }
    
    print(minRecipes(preferences))