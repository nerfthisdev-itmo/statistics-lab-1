from stats.variation import *
from stats.dataoutput import *

def main():
    nums = [1, 2, 1, 1, 0, 2, 1, 1, 1, 3, 1, 1, 1, 4, 2, 2, 2, 2, 0, 1, 4, 3, 3, 1, 1, 0, 0, 1, 2, 2, 4, 5, 3, 3, 3, 2, 2,2, 1,1, 2, 1, 0, 2, 2, 2, 1, 1, 3, 3, 4, 0, 2, 2, 2, 1, 3, 1, 3, 2]
    x = Variation(nums)
    print(x.statistical_series)
    print_variation_series(x.statistical_series)
    

if __name__ == "__main__":
    main()