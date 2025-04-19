def solve(s: str):
    """
    smallest in lexicographical order
    문자열의 위치는 같아야 한다고 함

    bcabc
    01114
    bca -> 이미 등장한 b(3) 을 보고 a(2) 보다 앞에 있는 b 를 제거하여 cab -> c(4) 를 보고 a(2) 보다 앞에 있는 c 를 제거하여 abc
    [0,1,2] -> [1,2,3] -> [2,3,4] (문자를 인덱스로 표현)
    memo[b] = 0, memo[c] = 1, ...
    이미 등장 -> 'b' in memo
    a(2) 보다 앞에 있는 b  => memo[b] < memo[a] -> a랑만 비교하는게 아니라 자신보다 작은 모든 문자가 존재하는지를 비교해야 함 (ex. cbcba -> bca)
    이러면 s 에 등장한 모든 문자를 미리 찾아둬야 함

    ex. cdbca
    문자별 등장횟수 -> a:1, b:1, c:2, d:1
    st = [c d] -> d > b 이지만 count(d) ==0 이니까 그냥 넣어야함 -> [c d b]

    cdbcab
    등장횟수 -> a:1, b:2, c:2, d:1
    st = [c d] -> a:1, b:2, c:1, d:0
    st = [c d b] -> a:1, b:1, c:1, d:0
    st = st[-1] > a and count > 0
    """
    # 등장한 모든 문자 찾기 -> max length : 26
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    print(counts)

    ans = []
    for c in s:
        while ans:
            if ans[-1] > c and counts[ans[-1]] > 0 and c not in ans:
                ans.pop()
            else:
                break

        if c not in ans:
            ans.append(c)
        counts[c] -= 1

    return "".join(ans)


solve("bcabc")
solve("cbacdcbc")
solve("cdadabcc")
solve("bbcaac")
solve("abacb")