from datetime import datetime, timedelta
import pygsheets
import myfitnesspal

FMT = "%Y-%m-%d"
client = myfitnesspal.Client("HaroldMartin128")
gc = pygsheets.authorize()


def __date_range(start, end=datetime.today()):
    return [datetime.fromordinal(i) for i in range(start.toordinal(), end.toordinal())]


def __get_col(wks, index):
    return wks.get_values(
        start=(1, index),
        end=(wks.rows, index),
        returnas="cell",
        include_tailing_empty=False,
    )


def __get_row(wks, index):
    return wks.get_values(
        start=(index, 1),
        end=(index, wks.cols),
        returnas="cell",
        include_tailing_empty=False,
    )


def __row_to_col_index_dict(headers):
    return {h.value: h.col - 1 for h in headers}


def update_sheet_from_mfp(username):
    wks = gc.open("MFP/" + username)[0]
    # TODO: detect if sheet exists

    last_cell = __get_col(wks, 1)[-1][0]
    row = last_cell.row
    last_date = datetime.strptime(last_cell.value, FMT)

    nutr_to_column = __row_to_col_index_dict(__get_row(wks, 1)[0])

    for day in __date_range(last_date + timedelta(days=1)):
        row += 1
        nutrs = [None] * len(nutr_to_column)
        nutrs[0] = day.strftime(FMT)
        mfp_nutrs = client.get_date(day, username=username)
        for nutrient, amount in mfp_nutrs.totals.items():
            if nutrient in nutr_to_column:
                nutrs[nutr_to_column[nutrient]] = amount
        wks.update_values((row, 1), [nutrs])


update_sheet_from_mfp("HaroldMartin128")
