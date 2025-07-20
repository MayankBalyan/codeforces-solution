def max_hikes(t, test_cases):
    results = []
    for case in test_cases:
        n, k, a = case
        i = 0
        count = 0
        while i <= n - k:
            if all(a[i + j] == 0 for j in range(k)):
                count += 1
                i += k + 1
            else:
                i += 1
        results.append(count)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append((n, k, a))
answers = max_hikes(t, test_cases)
for ans in answers:
    print(ans)
