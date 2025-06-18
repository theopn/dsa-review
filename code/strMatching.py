def bruteForceMatch(T, P):  # P is the "pattern" string we wish to find in T
    n, m = len(T), len(P)
    for i in range(n - m):
        j = 0
        while j < m and T[i + j] == P[j]:
            j += 1
        if j == m:
            return i

    return -1


def failure(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    return lps


def kmp(T, pattern):
    n, m = len(T), len(pattern)
    lps = failure(pattern)
    i, j = 0, 0
    while i < n:
        if T[i] == pattern[j]:
            if j == m - 1:
                return i - j
            else:
                i += 1
                j += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    return -1


def bruteForceMatchTest():
    T = 'ABACDABE'
    P = 'ABD'
    print(bruteForceMatch(T, P))

    T = 'BANANA'
    P = 'ANA'
    print(bruteForceMatch(T, P))

    T = 'ABACAABACCABACAB'
    P = 'ABACAB'
    print(bruteForceMatch(T, P))


def kmpTest():
    T = 'ABACDABE'
    P = 'ABD'
    print(kmp(T, P))

    T = 'BANANA'
    P = 'ANA'
    print(kmp(T, P))

    T = 'ABACAABACCABACAB'
    P = 'ABACAB'
    print(kmp(T, P))

    T = 'ABABCAABACCABABCAB'
    P = 'ABABCAB'
    print(kmp(T, P))


if __name__ == "__main__":
    bruteForceMatchTest()
    kmpTest()
