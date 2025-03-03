"""
words 의 원소는 모두 같은 길이를 가지는 단어임
concatened string : words 의 순열의 모든 스트링을 concat 한 후보군들 (순열의 순열)
s 에서 concatened string 시작 인덱스를 리스트로 리턴해라

1 <= s.length <= 10 ** 4
words.length <= 5000
words[i] <= 30

simple
1) words 의 순열 풀을 만듦
2) s 에 1의 원소가 시작하는 지점을 찾아서 인덱스 포함

words[i] 길이를 이용. l 이라 할 때 (window size)
s 에서 l 개 씩 읽음 -> words 에 들어있다면 words 에서 제외. -> 없는 것을 빼려고 시도한다면 words 를 초기화 후 다시 시작.
words 가 비어있게 되면 hit 임

s.length 가 l 의 배수가 아니라면..?
words 에 대한 dictionary
{
    "bar" : [0, 12]
    "foo" : [3, 9]
}
=> (0, 3), (9, 12)
0 + 3 = 3,
9 + 3 = 12
---
12 + 3 = 15 -> 여기서 foo 가 나와야 함
3 + 3 = 6 -> 여기서 bar 가 나와야 함
"""
from collections import Counter


def slow_solve(s, words):
    matches = []
    matches_word = []
    window_size = len(words[0])

    for i in range(len(s) - window_size + 1):
        word = s[i:i + window_size]
        if word in words:
            matches.append(i)
            matches_word.append(word)

    ans = []

    for i in range(len(matches) - len(words) + 1):
        available = words.copy()
        prev = -1
        for j in range(i, len(matches)):
            if matches_word[j] in available:
                if i == j:
                    available.remove(matches_word[j])
                    prev = matches[j]
                else:
                    if prev > -1 and matches[j] == prev + window_size:
                        available.remove(matches_word[j])
                        prev = matches[j]

        if len(available) == 0:
            ans.append(matches[i])

    return ans


def find_substring(s, words):
    """
    time complexity ? len(s) * len(words) * len(words[0])
    """

    word_size = len(words[0])
    window_size = len(words[0]) * len(words)
    words_counter = Counter(words)

    """
    window_size = len(words) * len(words[0]) 
    step = 1
    s 를 슬라이딩 -> window_size 안에 words counter 와 일치한다면 시작점을 추가
    """

    ans = []

    i = 0
    while i < len(s) - window_size + 1:
        sub_string = s[i:i + window_size]

        memo = {}
        flag = True
        for j in range(0, window_size, word_size):
            word = sub_string[j:j + word_size]

            if word in words_counter and memo.get(word, 0) < words_counter[word]:
                if word in memo:
                    memo[word] += 1
                else:
                    memo[word] = 1
            else:
                # 존재하지 않는 단어이거나 더 많이 나온 단어
                flag = False
                break

        if flag:
            ans.append(i)

        i += 1

    print(ans)

    return ans


assert find_substring("barfoothefoobarman", ["foo", "bar"]) == [0,9]
assert find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
assert find_substring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [6,9,12]
assert find_substring("ababababab", ["ababa","babab"]) == [0]
assert find_substring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]) == [13]
