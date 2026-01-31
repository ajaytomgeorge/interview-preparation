def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True


# ✅ 2. Find all anagrams of a word in a list

# (Using dictionary frequency comparison)

def find_anagrams(word, word_list):
    def freq_map(s):
        m = {}
        for ch in s:
            m[ch] = m.get(ch, 0) + 1
        return m

    target = freq_map(word)
    result = []

    for w in word_list:
        if freq_map(w) == target:
            result.append(w)

    return result