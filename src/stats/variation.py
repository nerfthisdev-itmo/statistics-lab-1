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

        output_str: str = f"min: {sorted_nums[0]} "
        output_str += f"max: {sorted_nums[-1]} "

        return output_str

'''
TODO: calculate: mode, range, expected value, standard diviation, CDF

'''