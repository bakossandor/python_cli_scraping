import requests
import click
from bs4 import BeautifulSoup

r = requests.get("https://www.betexplorer.com/soccer/england/premier-league/fixtures/")
soup = BeautifulSoup(r.text, 'html.parser')

def extract_data(soup):
    table_rows = soup.find("table", class_="table-main").find_all("tr")
    time = soup.find_all("td", class_="table-main__datetime")
    print(time)
    lines = []
    for idx, i in enumerate(table_rows):
        try:
            match_array = i.find("td", class_="h-text-left").find_all("span")
            def exact_time(idx):
                if time[idx].string != "":
                    return time[idx].string
                else:
                    return exact_time(idx - 1)

            match = {
                "home": match_array[0].string,
                "away": match_array[1].string,
                "time": exact_time(idx)
            }
            lines.append(match)
        except:
            pass
    return lines

@click.command()
def cli():
    click.echo(extract_data(soup))