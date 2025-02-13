from rich.console import Console
from rich.table import Table

console = Console()
series_table = Table(show_header=True, header_style="bold magenta")

series_table.add_column("Value")
series_table.add_column("Frequency")



def print_variation_series(statistical_series: dict):
    series_table.add_row(statistical_series.values)
    series_table.add_row(statistical_series.keys)
    console.print(series_table)