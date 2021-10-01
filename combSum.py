import collections

def combSum(candidates, target):
    dp = collections.defaultdict(list)
    dp[0] = [[]]
    candidates.sort()
    for c in candidates:
        for t in range(c, target + 1):
            for comb_t_m_c in dp[t-c]:
                dp[t].append(comb_t_m_c + [c])
    return dp[target]

if __name__ == "__main__":
    print(combSum([2,3,6,7], 7))