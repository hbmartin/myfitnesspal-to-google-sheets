#!/usr/bin/env python3

from datetime import datetime, timedelta
import pygsheets  # type: ignore
import myfitnesspal  # type: ignore
import sys
from typing import List, Dict, Any

from pygsheets import Cell

DATE_FORMAT = "%Y-%m-%d"


def _date_range(start: datetime, end=datetime.today()) -> List[datetime]:
    return [datetime.fromordinal(i) for i in range(start.toordinal(), end.toordinal())]


def _get_col(sheet: pygsheets.Worksheet, index: int) -> List[List[Cell]]:
    """Get column number `index` from the worksheet `sheet`.
    Returns:
        list[pygsheets.Cell]: A list of references to the cells in the column,
            excluding empty cells at the end.
    """
    return sheet.get_values(
        start=(1, index),
        end=(sheet.rows, index),
        returnas="cell",
        include_tailing_empty=False,
    )


def _get_row(sheet: pygsheets.Worksheet, index: int) -> List[List[Cell]]:
    """Get row number `index` from the worksheet `sheet`.
    Returns:
        list[pygsheets.Cell]: A list of references to the cells in the row, excluding
            empty cells at the end.
    """
    return sheet.get_values(
        start=(index, 1),
        end=(index, sheet.cols),
        returnas="cell",
        include_tailing_empty=False,
    )


def _row_to_col_index_dict(headers: List[Cell]) -> Dict[str, int]:
    """Calculate a mapping of cell contents to column index.
    Returns:
        dict[str, int]: {MFP nutrient name: worksheet column index} mapping.
        int: N
    """
    return {h.value: h.col - 1 for h in headers}


def update_sheet_from_mfp(
    username: str, mfp_client: myfitnesspal.Client, wks: pygsheets.Worksheet
):
    last_cell = _get_col(wks, 1)[-1][0]
    row = last_cell.row
    last_date = datetime.strptime(last_cell.value, DATE_FORMAT)

    nutr_to_column = _row_to_col_index_dict(_get_row(wks, 1)[0])

    for day in _date_range(last_date + timedelta(days=1)):
        row += 1
        nutrs: List[Any] = [None] * len(nutr_to_column)
        nutrs[0] = day.strftime(DATE_FORMAT)
        mfp_nutrs = mfp_client.get_date(day, username=username)
        for nutrient, amount in mfp_nutrs.totals.items():
            if nutrient in nutr_to_column:
                nutrs[nutr_to_column[nutrient]] = amount
        wks.update_values((row, 1), [nutrs])


def main():
    try:
        username = sys.argv[1]
    except IndexError:
        print("Supply username as first argument")
        sys.exit()
    print("Connecting to MyFitnessPal...")
    mfp_client = myfitnesspal.Client(username)
    gs_client = pygsheets.authorize()
    print("Opening spreadsheet...")
    # TODO: detect if sheet exists
    sheet = gs_client.open("MFP/" + username)[0]
    update_sheet_from_mfp(username, mfp_client, sheet)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
