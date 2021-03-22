#!/bin/usr/env/python3

import requests
import json
from datetime import datetime

from rich import print
from rich.table import Table
from rich.console import Console
console = Console()

URL = "https://ferien-api.de/api/v1/holidays"
THIS_YEAR = datetime.now().year

def get_http_response():
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/78.0.3904.108 Chrome/78.0.3904.108 Safari/537.36"}
    response = json.loads(requests.get(URL, headers=headers).text)

    dictionary = {}
    for item in response:
        try:
            dictionary.update({str(item["year"]): dictionary[str(item["year"])]})
        except KeyError:
            dictionary.update({str(item["year"]): {}})
        try:
            dictionary[str(item["year"])].update({item["stateCode"]: dictionary[str(item["year"])][item["stateCode"]]})
        except KeyError:
            dictionary[str(item["year"])].update({item["stateCode"]: []})
        arrState = dictionary[str(item["year"])][item["stateCode"]]
        arrState.append({ "name": item["name"], "start": item["start"], "end": item["end"] })
    return dictionary


def get_output_for_year(dictionary, command):
    console.print(command, style="bold green")
    table = Table(show_header=True, header_style="bold")
    table.add_column("State")
    for holiday in dictionary[command]["BY"]:
            table.add_column(holiday["name"])
    for state in dictionary[command]:
        stateArr = dictionary[command][state]
        try:
            table.add_row(state,
            f'{datetime.strptime(stateArr[0]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[0]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
            f'{datetime.strptime(stateArr[1]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[1]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
            f'{datetime.strptime(stateArr[2]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[2]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
            f'{datetime.strptime(stateArr[3]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[3]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
            f'{datetime.strptime(stateArr[4]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[4]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
            f'{datetime.strptime(stateArr[5]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[5]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}')
        except IndexError:
            console.print(f"{state} has less holidays: " + str(stateArr), style="red")
    console.print(table)


def get_output_for_state(dictionary, command):
    console.print(THIS_YEAR, style="bold green")
    table = Table(show_header=True, header_style="bold")
    for holiday in dictionary[str(THIS_YEAR)][command]:
            table.add_column(holiday["name"])
    stateArr = dictionary[str(THIS_YEAR)][command]
    try:
        table.add_row(
        f'{datetime.strptime(stateArr[0]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[0]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
        f'{datetime.strptime(stateArr[1]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[1]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
        f'{datetime.strptime(stateArr[2]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[2]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
        f'{datetime.strptime(stateArr[3]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[3]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
        f'{datetime.strptime(stateArr[4]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[4]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}',
        f'{datetime.strptime(stateArr[5]["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(stateArr[5]["end"], "%Y-%m-%dT00:00Z").strftime("%x")}')
    except IndexError:
        console.print(f"{command} has less holidays: " + str(stateArr), style="red")
    console.print(table)


def get_output_for_holiday(dictionary, command):
    console.print(str(THIS_YEAR), style="bold green")
    table = Table(show_header=True, header_style="bold")
    table.add_column("State")
    table.add_column(command)
    for state in dictionary[str(THIS_YEAR)]:
        for holiday in dictionary[str(THIS_YEAR)][state]:
            if command in holiday["name"]:
                table.add_row(state,
                f'{datetime.strptime(holiday["start"], "%Y-%m-%dT00:00Z").strftime("%x")} - {datetime.strptime(holiday["end"], "%Y-%m-%dT00:00Z").strftime("%x")}')
    console.print(table)


def main(command):
    dictionary = get_http_response()

    try:
        if dictionary[command]:
            get_output_for_year(dictionary, command)
    except KeyError:
        try:
            if dictionary[str(THIS_YEAR)][command.upper()]:
                get_output_for_state(dictionary, command.upper())
        except KeyError:
            try:
                for holiday in dictionary[str(THIS_YEAR)]["BY"]:
                    if command.lower() in holiday["name"]:
                        get_output_for_holiday(dictionary, holiday["name"])
            except KeyError:
                console.print("Wrong command!", style="bold red")


if __name__ == '__main__':
    console.print("[bold]Year[/bold] e.g. 2017 | [bold]State[/bold] e.g. BY | [bold]Holidayname[/bold] e.g. Winter \n")
    console.print("Type in your command:")
    command = input()
    console.print("")
    main(command)