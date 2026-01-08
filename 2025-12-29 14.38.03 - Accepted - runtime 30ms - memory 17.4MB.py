class Solution:
    def sortSentence(self, s: str) -> str:
        # Split, sort by the number at end, remove numbers
        # Time: O(n log n), Space: O(n)
        words = s.split()
        # Sort by the last character (which is the position number)
        words.sort(key=lambda w: w[-1])
        # Remove the position number from each word
        return ' '.join(w[:-1] for w in words)