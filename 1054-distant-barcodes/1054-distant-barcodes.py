from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        heap = [(-v, k) for k, v in Counter(barcodes).items()]
        heapq.heapify(heap)
        answer = []
        prev = (0, 0)
        while heap:
            v, k = heapq.heappop(heap)
            answer.append(k)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (v+1, k)
        return answer