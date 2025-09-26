class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        while iterations>0:
            d = 2* init
            init = init -d * learning_rate
            iterations-=1


        return round(init,5)