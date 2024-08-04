class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        lista_ordenada = sorted(intervals, key=lambda x: x[1])
        t=len(intervals)
        pre=lista_ordenada[0][1]
        k=0
        for i in range(1,t):
            if lista_ordenada[i][0] < pre: 
                k+=1
            else:
                pre=lista_ordenada[i][1]
        return k
    def __Pruebas(self):
        intervals = [[1,100],[11,22],[1,11],[2,12]]
        print(self.eraseOverlapIntervals(intervals))
    def __init__(self) -> None:
        self.__Pruebas()
xx = Solution()
