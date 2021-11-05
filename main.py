"""DISCLAIMER : i know that the random librairy from python is way better than this,
but i wanted to know how it work, so it was the best thing to do imo"""

class MyRandom:
    """all the numbers that you will see are big primes numbers"""
    def __init__(self, seed=None):
        import time
        self.increment=256487683
        if seed==None:
            self.seed=self.get_seed(time.time())
        else:
            self.seed=self.get_seed(seed)
        self.current_number=self.seed + self.increment
            
    def get_seed(self,a):
        return a*5456163703 + self.increment

    def _randint_0_to_x(self,x):
        """int x : the upper born of the interval
        before the +2 I did a x=x+1 because i had only a few 0, and the result is equal to result -1 to balance
        but I had only a few result = x, so i put a +2 and it works well, what was interesting was the '10': 4593-tf        
        result with x=10 BEFORE the +2 on 1000000 iterations : 
        {'0': 91692, '1': 92478, '2': 97879, '3': 98463, '4': 94353, '5': 97201, '6': 97406, '7': 94479, '8': 97684, '9': 92432, '10': 45933}
        result with x=10 AFTER the +2 on 1000000 iterations : 
        {'0': 91960, '1': 94014, '2': 90705, '3': 94403, '4': 92273, '5': 81919, '6': 92722, '7': 88258, '8': 91000, '9': 89246, '10': 93500}"""
        x=x+2
        result=-1
        while result < 0 or result > x-2:
            self.current_number = self.current_number*self.seed + self.increment
            self.current_number=self.current_number%(x*(x+100000000))
            result=round(self.current_number/(x+100000000))-1
        return result
    
    def randint(self,a,b):
        a,b=int(a),int(b)
        assert a<b,"a must be lesser than b !"
        return self._randint_0_to_x(b-a)+a
    
    def _randrange_0_to_x(self,x):
        """float or int x : the upper born of the interval"""
        x=x+2
        result=-1
        while result < 0 or result > x-2:
            self.current_number = self.current_number*self.seed + self.increment
            self.current_number=self.current_number%(x*(x+100000000))
            result=self.current_number/(x+100000000)-1
        return result
    
    def randrange(self,a,b):
        assert a<b,"a must be lesser than b !"
        # doing %1 or %0 doesnt have any sense so we compute bigger numbers and then we divide them to get a number between 0 and 1
        if -1<=b<=1:
            b*=10
            a*=10
            return (self._randrange_0_to_x(b-a)+a)/10
        return self._randrange_0_to_x(b-a) +a
        
if __name__ == "__main__":
    R=MyRandom() 
    for _ in range(10):
        print(R.randint(0,10), end=" ")
