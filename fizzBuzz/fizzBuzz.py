class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [x for x in range(n)]
        i = 1
        while i<=n:
            if i%3==0 and i%5==0:
                answer[i-1]="FizzBuzz"
            elif i%3==0:
                answer[i-1]="Fizz"
            elif i%5==0:
                answer[i-1]="Buzz"
            else:
                answer[i-1]= str(i)
            i=i+1
        return answer
