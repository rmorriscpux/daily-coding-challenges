'''
You are given a list of (website, user) pairs that represent users visiting websites.
Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].
'''

from typing import List, Tuple

def similarWebsites(visit_pairs: List[Tuple[str, int]], k: int) -> List[Tuple[str, str]]:
    # Create dictionary of sets of users that went to each website.
    users_per_site = dict()
    for site, user in visit_pairs:
        if site not in users_per_site:
            users_per_site[site] = set()
        users_per_site[site].add(user)

    sites_list = list(users_per_site.keys())
    similar_sites = []
    # Assign each pair of websites a similarity score and append the score and pair to the list.
    # Similarity score is defined by the total users who visited both websites (set intersection) divided by the total users who visited either website (set union).
    for i in range(0, len(sites_list)-1):
        for j in range(i+1, len(sites_list)):
            users_on_both = len(users_per_site[sites_list[i]].intersection(users_per_site[sites_list[j]]))
            users_on_either = len(users_per_site[sites_list[i]].union(users_per_site[sites_list[j]]))
            similarity_score = users_on_both / users_on_either
            similar_sites.append((similarity_score, (sites_list[i], sites_list[j])))
    # Sort site pairs by similarity score in descending order.
    similar_sites.sort(key=lambda s: -s[0])
    # Return the top k similar site pairs.
    return list(map(lambda s: s[1], similar_sites[:k]))
    
if __name__ == "__main__":
    visit_pairs = [('a', 1), ('a', 3), ('a', 5),
                    ('b', 2), ('b', 6),
                    ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
                    ('d', 4), ('d', 5), ('d', 6), ('d', 7),
                    ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
    
    print(similarWebsites(visit_pairs, 1))
    print(similarWebsites(visit_pairs, 2))