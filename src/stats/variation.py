import numpy as np

class Variation:    
    def __init__(self, data):
        self.data = data
        self.statistical_series = self.get_statistical_series()
        self.mode = self.get_mode()
        self.extremes = self.get_extremes()
        
        
        
    
    def get_variation_series(self):
        return sorted(self.data)


    def get_statistical_series(self):
        data = self.data
        number_freq = dict()
        for num in data:
            if (number_freq.get(num, None) == None):
                number_freq[num] = 0
            number_freq[num] += 1
        return number_freq


    def get_mode(self):
        return max(self.statistical_series, key=self.statistical_series.get)


    def get_extremes(self):
        sorted_nums: list = sorted(self.data)
        
        self.max = sorted_nums[-1]
        self.min = sorted_nums[0]

        output_str: str = f"min: {sorted_nums[0]} "
        output_str += f"max: {sorted_nums[-1]} "

        return output_str


'''
TODO: calculate: standard diviation, CDF
'''

class IntervalVariationSeries:
    def __init__(self, data):
        self.data = np.array(data)
        self.min = np.min(self.data)
        self.max = np.max(self.data)
        self.range = self.max - self.min
        self.n = len(self.data)
        self.k = int(1 + np.log2(self.n))
        self.h = self.range / self.k
        self.bins = np.arange(self.min, self.max + self.h, self.h)
    
    def get_intervals(self):
        return [(round(self.bins[i], 4), round(self.bins[i+1], 4)) for i in range(len(bins) - 1)]
    
    def get_frequencies(self):
        hist, _ = np.histogram(self.data, bins=self.bins)
        return hist
    
    def show(self):
        intervals = self.get_intervals()
        frequencies = self.get_frequencies()
        for (start, end), freq in zip(intervals, frequencies):
            print(f"[{start}, {end}) → {freq}")