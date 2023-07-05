#!/usr/bin/env python3
# Lab Space CLI
# A CLI for the Lab Space project.
# Github: https://github.com/lewisevans2007/lab_space_cli
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import sys
import subprocess
import curses

supported_languages = [
    "c",
    "c++",
    "python",
    "rust",
    "bash",
    "nodejs",
    "typescript",
    "go",
    "elixir",
    "assembly",
    "fortran",
    "java",
    "r",
    "d",
    "lisp",
    "php",
    "haskell",
    "f#",
]


def print_menu(stdscr, selected_idx):
    stdscr.clear()
    stdscr.addstr("Please choose a language:\n")
    for i, lang in enumerate(supported_languages):
        if i == selected_idx:
            stdscr.addstr(f"> {lang.capitalize()}\n")
        else:
            stdscr.addstr(f"  {lang.capitalize()}\n")
    stdscr.refresh()


def select_language():
    curses.wrapper(select_language_wrapper)


def select_language_wrapper(stdscr):
    selected_idx = 0
    while True:
        print_menu(stdscr, selected_idx)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected_idx = max(selected_idx - 1, 0)
        elif key == curses.KEY_DOWN:
            selected_idx = min(selected_idx + 1, len(supported_languages) - 1)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            curses.endwin()
            language = supported_languages[selected_idx]
            # start docker container
            image_string = f"ghcr.io/lewisevans2007/lab_space_{language}:latest"
            print(f"Starting {image_string} container")
            subprocess.run(["docker", "run", "-it", "--rm", image_string], check=True)
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter a valid command")
    elif sys.argv[1] == "help":
        print("Lab Space CLI")
        print("A cli for managing lab space docker containers")
        print("Commands:")
        print("lab_space run <LANGUAGE>")
        print("lab_space help")
        print("Languages available:")
        for lang in supported_languages:
            print(lang.capitalize())
    elif sys.argv[1] == "run":
        if len(sys.argv) < 3:
            select_language()
        else:
            language = sys.argv[2].lower()
            if language in supported_languages:
                # start docker container
                image_string = f"ghcr.io/lewisevans2007/lab_space_{language}:latest"
                print(f"Starting {image_string} container")
                subprocess.run(
                    ["docker", "run", "-it", "--rm", image_string], check=True
                )
            else:
                print("Sorry that language is not supported yet")
                print("Please chose one of the following languages:")
                for i, lang in enumerate(supported_languages):
                    print(f"{i+1}: {lang.capitalize()}")
    else:
        print("Please enter a valid command")
