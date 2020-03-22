#!/usr/bin/env python3
from .term_colours import StandardColours


class InputManager(StandardColours):
    prog_name = "airscript"
    section_type = "attacks"

    def __init__(self, question) -> None:
        self.PS1 = (f"{self.uline.return_colour('airscript')} {self.section_type}"
                    f"({self.red.return_colour(question)}) > ")

    def get(self, highest_val=None, boolean=False, *exclusions):
        while True:

            try:
                value = input(self.PS1).strip()

                if boolean:
                    v_true, v_false = value.startswith("y"), value.startswith("n")

                    if not (v_true or v_false):
                        self.yellow.print_question("Please select between y/n.\n")
                        continue

                    else:
                        return True if v_true else False

                else:
                    v_range = [str(i) for i in range(1, highest_val + 1) if i not in exclusions]
                    return int(v_range[v_range.index(value)])

            except(ValueError, TypeError):
                self.yellow.print_question("Please select a valid integer.\n")
                continue

            except(KeyboardInterrupt, EOFError):
                return None


class TkManager():

    def __init__(self) -> None:
        ...