from lib import mode, median, mean, console
from config import read_config
from rich.prompt import Confirm
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingTypeStubs]
from matplotlib import ticker

"""Display the calculated data"""


def display_data(genre_revenues: list[float], other_revenues: list[float]):
    config: dict[str, str | bool] = read_config()
    genre: str = str(config["genre"]).strip().replace('"', "")
    plt.rcParams['figure.figsize'] = [12, 8] # Set larger figure size to stop text clipping off window

    # Genre Variables
    try:
        genre_mode_result = mode(genre_revenues)
        genre_median_result = median(genre_revenues)
        genre_mean_result = mean(genre_revenues)
    except ValueError:
        console.print(
            " Fatal error while computing results - please check the data. ",
            style="white on red",
        )
        exit(1)  # Make sure to exit, as we cannot continue

    console.print(f"[bold]{genre} Movies - Revenue Mode:[/]", genre_mode_result)
    console.print(f"[bold]{genre} Movies - Median Revenue:[/]", genre_median_result)
    console.print(f"[bold]{genre} Movies - Mean Revenue:[/]", genre_mean_result)
    console.print()

    if Confirm.ask("[bold]Show a graph of this data?[/]"):
        console.print("[bold yellow]Close the graph window to continue program execution[/]")
        console.print()  # Padding
        # Create bar chart
        plt.bar(  # pyright: ignore[reportUnknownMemberType] Can't change a library
            ["Mode", "Median", "Mean"],
            [genre_mode_result, genre_median_result, genre_mean_result],
        )
        plt.ylim(100000, 200000000)  # pyright: ignore[reportUnknownMemberType]
        plt.xlabel("Categories")  # pyright: ignore[reportUnknownMemberType]
        plt.ylabel("Revenue (hundred millions) (US Dollars)")  # pyright: ignore[reportUnknownMemberType]
        plt.title(f"{genre} Movies - Revenue Statistics")  # pyright: ignore[reportUnknownMemberType]
        plt.ticklabel_format(style="plain", axis="y")
        plt.ylim(0, 250_000_000)  # pyright: ignore[reportUnknownMemberType]
        plt.gca().get_yaxis().set_major_formatter(
            ticker.FuncFormatter(lambda x, y: format(int(x), ","))  # pyright: ignore[reportUnknownArgumentType, reportUnknownLambdaType]
        )
        plt.show()  # pyright: ignore[reportUnknownMemberType]

    # Other Movie Variables
    try:
        other_mode_result = mode(other_revenues)
        other_median_result = median(other_revenues)
        other_mean_result = mean(other_revenues)
    except ValueError:
        console.print(
            " Fatal error while computing results - please check the data. ",
            style="white on red",
        )
        exit(1)

    console.print(f"[bold]Non-{genre} Movies - Revenue Mode:[/]", other_mode_result)
    console.print(f"[bold]Non-{genre} Movies - Median Revenue:[/]", other_median_result)
    console.print(f"[bold]Non-{genre} Movies - Mean Revenue:[/]", other_mean_result)
    console.print()

    if Confirm.ask("[bold]Show a graph of this data?[/]"):
        console.print("[bold yellow]Close the graph window to continue program execution[/]")
        console.print()  # Padding
        # Create bar chart
        plt.bar(  # pyright: ignore[reportUnknownMemberType] Same as above
            ["Mode", "Median", "Mean"],
            [other_mode_result, other_median_result, other_mean_result],
        )
        plt.ylim(100000, 200000000)  # pyright: ignore[reportUnknownMemberType]
        plt.xlabel("Categories")  # pyright: ignore[reportUnknownMemberType]
        plt.ylabel("Revenue (hundred millions) (US Dollars)")  # pyright: ignore[reportUnknownMemberType]
        plt.title(f"Non-{genre} Movies - Revenue Statistics")  # pyright: ignore[reportUnknownMemberType]
        plt.ticklabel_format(style="plain", axis="y")
        plt.ylim(0, 250_000_000)  # pyright: ignore[reportUnknownMemberType]
        plt.gca().get_yaxis().set_major_formatter(
            ticker.FuncFormatter(lambda x, y: format(int(x), ","))  # pyright: ignore[reportUnknownArgumentType, reportUnknownLambdaType]
        )
        plt.show()  # pyright: ignore[reportUnknownMemberType]

    if Confirm.ask("[bold]Show a combined graph of all data?[/]"):
        console.print("[bold yellow]Close the graph window to continue program execution[/]")
        console.print()  # Padding
        bar_colors = [
            "tab:blue",
            "tab:orange",
            "tab:blue",
            "tab:orange",
            "tab:blue",
            "tab:orange",
        ]

        plt.bar(  # pyright: ignore[reportUnknownMemberType] Same as above
            [
                f"{genre} Mode",
                f"Non-{genre} Mode",
                f"{genre} Median",
                f"Non-{genre} Median",
                f"{genre} Mean",
                f"Non-{genre} Mean",
            ],
            [
                genre_mode_result,
                other_mode_result,
                genre_median_result,
                other_median_result,
                genre_mean_result,
                other_mean_result,
            ],
            color=bar_colors,
        )
        plt.ticklabel_format(style="plain", axis="y")
        plt.ylim(0, 250_000_000)  # pyright: ignore[reportUnknownMemberType]
        plt.gca().get_yaxis().set_major_formatter(
            ticker.FuncFormatter(lambda x, y: format(int(x), ","))  # pyright: ignore[reportUnknownArgumentType, reportUnknownLambdaType]
        )
        plt.show()  # pyright: ignore[reportUnknownMemberType]

    console.print()  # Padding

    # Checks
    hypothesis_mode_result: bool = genre_mode_result > other_mode_result
    hypothesis_median_result: bool = genre_median_result > other_median_result
    hypothesis_mean_result: bool = genre_mean_result > other_mean_result
    correct_counter: int = 0

    # Was going to figure out a more elegant solution to this, but it works and I'm running out of time
    if hypothesis_mean_result:
        correct_counter += 1
    if hypothesis_median_result:
        correct_counter += 1
    if hypothesis_mean_result:
        correct_counter += 1

    console.print("Is the hypothesis correct?", style="bold")
    console.print(
        "[b]In relation to mode:[/]",
        "[bold green]Yes[/]" if hypothesis_mode_result else "[bold red]No[/]",
    )
    console.print(
        "[b]In relation to median:[/]",
        "[bold green]Yes[/]" if hypothesis_median_result else "[bold red]No[/]",
    )
    console.print(
        "[b]In relation to mean:[/]",
        "[bold green]Yes[/]" if hypothesis_mean_result else "[bold red]No[/]",
    )

    # If all are true, the hypothesis is correct
    if correct_counter == 3:
        console.print(
            "All are true, thus the hypothesis has been proven correct.",
            style="bold green",
        )
    elif correct_counter > 1:
        console.print(
            "Some are true, but others are false, thus we cannot reliably determine the hypothesis.",
            style="bold yellow",
        )
    else:
        console.print(
            "All are false, thus the hypothesis has been proven false.",
            style="bold red",
        )
