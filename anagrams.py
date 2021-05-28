def anagrams(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    l1 = sorted([c for c in s1]) # O(n.logn) + O(n)
    l2 = sorted([c for c in s2]) # O(n.logn) + O(n)
    # 2*(O(n.logn) + O(n))
    return l1 == l2

