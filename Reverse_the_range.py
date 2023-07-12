class Solution:
    @staticmethod
    def Reverse_the_range(array,B,C):
        i,j=B,C
        while i<j:
            array[i],array[j]=array[j],array[i]
            i+=1
            j-=1

if __name__ == '__main__':
    array=list(map(int,input().split()))
    B=int(input())
    C = int(input())
    ob=Solution()
    ob.Reverse_the_range(array,B,C)
    print(*array)
