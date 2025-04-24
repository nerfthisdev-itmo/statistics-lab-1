from typing import List
import matplotlib.pyplot as plt
from numpy import var

from stats.interval import IntervalVariationSeries
from stats.variation import Variation


def plot_cdf(variation_series: Variation | IntervalVariationSeries, dir_path: str):
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



def plot_polygon(variation_series:Variation | IntervalVariationSeries, dir_name: str):
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

def plot_cumulative(variation_series:Variation | IntervalVariationSeries, dir_name: str): 
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

def plot_ogive(variation_series: IntervalVariationSeries, dir_name: str):
    
    plt.plot(variation_series.cumulative_values, variation_series.bin_centers, 
        marker="o",
        color="blue",
        label="Огивная кривая",)

    if variation_series.median is not None:
        plt.axhline(
            y=variation_series.median,
            color="red",
            linestyle="--",
            linewidth=1.5,
            label=f"Медиана ({variation_series.median:.2f})",
        )

    plt.legend()
    plt.grid(True)
    plt.savefig(dir_name + "/ogive.pdf")
    plt.savefig(dir_name + "/ogive.png")
    plt.close()


def boxplot_for_two_lists(x, y:IntervalVariationSeries | Variation, dir_name: str):
    # Создаем график с двумя subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Боксплот для первого набора данных
    ax1.boxplot(x.data, vert=True, patch_artist=True)
    ax1.set_title("Первый набор данных")
    ax1.set_ylabel("Значения")
    ax1.grid(True)

    ax2.boxplot(y.data, vert=True, patch_artist=True)
    ax2.set_title("Второй набор данных")
    ax2.grid(True)

    plt.suptitle("Сравнение распределений данных")
    plt.tight_layout()

    plt.savefig(dir_name + "/boxplot.pdf")
    plt.savefig(dir_name + "/boxplot.png")

    plt.close()
