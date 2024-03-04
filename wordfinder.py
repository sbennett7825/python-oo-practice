import random

"""Word Finder: finds random words from a dictionary and counts how many total words have been read.

>>> wf = WordFinder(start=0)

>>> wf.random()
furnishing
1 words read

>>> wf.random()
diffusor
2 words read

>>> wf.reset()

>>> wf.random()
granule
1 words read
"""
class WordFinder:
    # def __init__(self, start=0):
    #     """Make a new word counter starting at start"""
    #     self.start = self.next = start

    # def random(self):
    #     """Opens words.txt file, reads random word on line from range of lines from words.txt file, adds +1 to word counter"""
    #     file = open("words.txt", "r")
    #     self.next +=1
    #     print (f"{file.readlines()[random.randrange(0,235887)]}" f"{self.next} words read")
    
    # def reset(self):
    #     """Reset word counter to original start."""
    #     self.next = self.start

    def __init__(self, path):
        """Reads dictionary and reports number of items read."""
        dict = open(path)
        self.words = self.parse(dict)
        print(f"{len(self.words)} words read")

    def parse(self, dict):
        """Parses dict into list of words."""
        return [word.strip() for word in dict]

    def random(self):
        """Returns random word."""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    def parse(self, dict):
        """Parses dict and turns into list of words, skipping blanks/comments."""
        return [word.strip() for word in dict
                if word.strip() and not word.startswith("#")]
