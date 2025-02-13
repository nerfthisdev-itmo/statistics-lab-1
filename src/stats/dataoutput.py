from rich.console import Console
from rich.table import Table

console = Console()
series_table = Table(show_header=True, header_style="bold magenta")

series_table.add_column("Value")
series_table.add_column("Frequency")



def print_variation_series(statistical_series: dict):
    for i in statistical_series:
        series_table.add_row(str(i), str(statistical_series[i]))
    console.print(series_table)