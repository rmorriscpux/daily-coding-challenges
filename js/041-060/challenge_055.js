/*
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
*/

const { createHash } = require('crypto');

class URLShortener {
    #charMap = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"; // 62 characters total.
    #urlMap = {};
    // Change the string here if you wish to use a different hash algorithm.
    #hashAlgo = "sha256";

    constructor() {
    }

    shorten(urlString) {
        // Generate Hash, and convert to an integer.
        let urlHashInt = parseInt(createHash(this.#hashAlgo).update(urlString).digest('hex'), 16);
        // Now map to characters.
        let fullShortURL = "";
        while (urlHashInt > 0) {
            fullShortURL = fullShortURL.concat(this.#charMap.charAt(urlHashInt % 62));
            urlHashInt = Math.floor(urlHashInt / 62);
        }
        // Now shorten the URL. Start with 6 characters. Add one character if there is a clash.
        let totalChars = 6;
        while (Object.keys(this.#urlMap).includes(fullShortURL.slice(0, totalChars)) && totalChars < fullShortURL.length) {
            // Case - URL was already shortened. No need to add it again.
            if (this.#urlMap[fullShortURL.slice(0, totalChars)] == urlString) {
                break;
            }
            totalChars++;
        }

        // Add to urlMap and return the short string.
        this.#urlMap[fullShortURL.slice(0, totalChars)] = urlString;
        return fullShortURL.slice(0, totalChars);
    }

    restore(shortString) {
        if (Object.keys(this.#urlMap).includes(shortString)) {
            return this.#urlMap[shortString];
        }
        return null;
    }
}

const urlShortener = new URLShortener();
const short1 = urlShortener.shorten("https://www.google.com");
const restored1 = urlShortener.restore(short1);
console.log(short1, restored1);
const short2 = urlShortener.shorten("https://www.superduperlong.com/kg2vghv2vgf2kvv2gfg2hkvg22fvg2kv2kfv2k3jf2v2vgc");
const restored2 = urlShortener.restore(short2);
console.log(short2, restored2);