from urllib.request import urlopen

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)

def main_words(url):
    print(url)
    words = fetch_words(url)
    print_words(words)

print('words.py __name__ : ')
print(__name__)
