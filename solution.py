"""
First Non-Repeating Character
Given a string s, find the first non-repeating character and return its index.
If it does not exist, return -1.
"""
from collections import Counter

def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    for idx, ch in enumerate(s):
        if counts[ch] == 1:
            return idx
    return -1

if __name__ == "__main__":
    sample = "leetcode"
    print(f"Index of first unique char in '{sample}': {first_uniq_char(sample)}")
