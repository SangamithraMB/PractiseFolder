from load_data import load_data
from collections import Counter


all_data = load_data()
print(all_data.keys())


# Show help command
def show_help():
    help_text = """
Available commands:
    help            - Shows this help message
    show_countries  - Shows a list of all countries (without duplicates)
    top_countries <num_countries> - Shows the top countries with the most ships
    """
    print(help_text)


# Show countries command
def show_countries(data):
    countries = {ship["COUNTRY"] for ship in data["data"] if ship["COUNTRY"]}
    sorted_countries = sorted(countries)
    return "\n".join(sorted_countries)


# Top countries command
def top_countries(data, num_countries):
    country_counter = Counter(ship["COUNTRY"] for ship in data["data"] if ship["COUNTRY"])
    most_common = country_counter.most_common(num_countries)
    return "\n".join(f"{country}: {count}" for country, count in most_common)


# Main function to handle interactive command line
def main():


    #print("Type 'help' for a list of available commands.")

    while True:
        prompt = input("> ").strip()

        if prompt.lower() == "help":
            show_help()
        elif prompt.lower() == "show_countries":
            print(show_countries(all_data))
        elif prompt.lower().startswith("top_countries"):
            try:
                _, num_countries = prompt.split()
                num_countries = int(num_countries)
                print(top_countries(all_data, num_countries))
            except (IndexError, ValueError):
                print("Usage: top_countries <num_countries>")
        elif prompt.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        else:
            print("Unknown command. Type 'help' for a list of available commands.")


if __name__ == "__main__":
    main()