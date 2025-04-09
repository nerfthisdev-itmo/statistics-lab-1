import matplotlib.pyplot as plt

from stats.variation import Variation


def plot_cdf(variation_series: Variation, dir_path: str):
    nums = variation_series.data
    func = lambda k: variation_series.get_cdf(k)
    x_values = nums.copy()
    x_values.append(min(nums) - 0.5)
    x_values.append(max(nums) + 0.5)
    x_values.sort()

    y = [func(x) for x in x_values]

    plt.step(x_values, y)
    plt.ylabel("F^{*}(x)")
    plt.title("Эмпирическая функция распределения")
    plt.grid(True)
    plt.savefig(dir_path + "/eCDF.pdf")
    plt.savefig(dir_path + "/eCDF.png")
    plt.close()



def plot_polygon(variation_series:Variation, dir_name: str):
    x_vals = list(variation_series.statistical_series.keys())
    y_vals = list(variation_series.statistical_series.values())
    if len(x_vals) != len(y_vals):
        print("ERROR: x_vals: list[float] != y_vals: list[float]")
        return

    plt.plot(x_vals, y_vals, marker="o", color="blue", label="Полигон")

    plt.legend()
    plt.grid(True)
    plt.savefig(dir_name + "/polygon.pdf")
    plt.savefig(dir_name + "/polygon.png")
    plt.close()

def plot_cumulative(variation_series:Variation, dir_name: str): 
    x_vals = list(variation_series.statistical_series.keys())
    y_vals = variation_series.cumulative_values
    if len(x_vals) != len(y_vals):
        print("ERROR: x_vals: list[float] != y_vals: list[float]")
        return

    plt.plot(x_vals, y_vals, marker="o", color="blue", label="Полигон")

    plt.legend()
    plt.grid(True)
    plt.savefig(dir_name + "/cumulative.pdf")
    plt.savefig(dir_name + "/cumulative.png")
    plt.close() 
