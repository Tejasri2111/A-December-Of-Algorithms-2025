heights = list(map(int, input().split()))
N = len(heights)

peaks = []

for i in range(1, N - 1):
    if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
        peaks.append(i)

if peaks:
    print(*peaks)
else:
    print(-1)
