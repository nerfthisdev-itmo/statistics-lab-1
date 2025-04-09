import matplotlib.pyplot as plt


def plot_cdf(nums: list[float], func, dir_path: str):
    x_values = nums.copy()
    x_values.append(min(nums) - 0.5)
    x_values.append(max(nums) + 0.5)
    x_values.sort()

    y = [func(x) for x in x_values]

    plt.step(x_values, y)
    plt.ylabel("F^{*}(x)")
    plt.title("Эмпирическая функция распределения")
    plt.grid(True)
    plt.savefig(dir_path + "eCDF.pdf")
    plt.savefig(dir_path + "eCDF.png")
    plt.close()



def plot_polygon(x_vals: list[float], y_vals: list[float], dir_name: str):
    if len(x_vals) != len(y_vals):
        print("ERROR: x_vals: list[float] != y_vals: list[float]")
        return

    plt.plot(x_vals, y_vals, marker="o", color="blue", label="Полигон")

    plt.legend()
    plt.grid(True)
    plt.savefig(dir_name + "polygon.pdf")
    plt.savefig(dir_name + "polygon.png")
    plt.close()
