

def get_variation_series(data):
    return sorted(data)


def get_statistical_series(data):
    number_freq = dict()
    for num in data:
        if (number_freq.get(num, None) == None):
            number_freq[num] = 0
        number_freq[num] += 1
    return number_freq


def get_mode(nums:dict):
    return max(nums, key=nums.get)


def get_extremes(nums: list):
    sorted_nums: list = sorted(nums)

    output_str: str = f"min: {sorted_nums[0]} "
    output_str += f"max: {sorted_nums[-1]} "

    return output_str
