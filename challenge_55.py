'''
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''

from hashlib import sha256 # Can use any hash, but this will do.

class URLShortener:
    def __init__(self):
        self._char_map = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # Length: 10+26+26 = 62
        self.url_map = dict()
        
    def shorten(self, url: str):
        # Start by getting an integer from a sha256 hash of the URL.
        n = int(sha256(url.encode()).hexdigest(), 16)
        # Converting the hashed value to a 62-bit alphanumeric value.
        full_short_url = ""
        while n > 0:
            map_key = n % 62
            full_short_url += self._char_map[map_key]
            n //= 62
        # Now shorten the URL. Start with 6 characters. Add one character if there is a clash.
        total_chars = 6
        while full_short_url[:total_chars] in self.url_map and total_chars < len(full_short_url): # Edge case: Total hash clash. Odds of occurrence are 1 in 2^256.
            # Case - URL was already shortened. No need to add it again.
            if self.url_map[full_short_url[:total_chars]] == url:
                break
            total_chars += 1

        self.url_map[full_short_url[:total_chars]] = url
        return full_short_url[:total_chars]

    def restore(self, short: str):
        if short in self.url_map:
            return self.url_map[short]
        return None

if __name__ == "__main__":
    s = URLShortener()
    short1 = s.shorten("https://www.google.com/")
    restored1 = s.restore(short1)
    print(short1, restored1)
    short2 = s.shorten("https://www.superduperlong.com/kg2vghv2vgf2kvv2gfg2hkvg22fvg2kv2kfv2k3jf2v2vgc")
    restored2 = s.restore(short2)
    print(short2, restored2)