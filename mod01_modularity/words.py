"""Retrieve and print words from a URL
Usage:
    python3 words.py <URL>
"""

from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from an URL
        Args:
            url: The URL of a UTF-8 text document
        Returns:
            A list of string containing the words from the document
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    """Prints each element in an array per line
        Args:
            story_words: An iterable series of printable items
    """
    for word in story_words:
        print(word)

def main_words(url):
    print(url)
    words = fetch_words(url)
    print_words(words)

print('words.py __name__ : ')
print(__name__)
