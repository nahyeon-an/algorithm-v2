def solve(s):
    if len(s) == 1:
        return [[s]]

    def is_palindrome(word):
        start = 0
        last = len(word) - 1
        while start < last:
            if word[start] != word[last]:
                return False
            start += 1
            last -= 1
        return True

    ans = []
    for j in range(1, len(s) + 1):
        sub = s[:j]

        if is_palindrome(sub):
            if j < len(s):
                results = solve(s[j:])
                for result in results:
                    ans.append([sub] + result)
            else:
                ans.append([sub])

    return ans


if __name__ == '__main__':
    solve("a")
    solve("aa")
    solve("abb")
    solve("aaab")
    solve("abcaa")
    solve("abbab")
