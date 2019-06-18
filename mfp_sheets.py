from datetime import datetime, timedelta
import pygsheets
import myfitnesspal

FMT = "%Y-%m-%d"

gc = pygsheets.authorize()
wks = gc.open("MFP")[0]
last_cell = wks.get_values(
    start=(1, 1), end=(wks.rows, 1), returnas="cell", include_tailing_empty=False
)[-1][0]
row = last_cell.row
last_date = datetime.strptime(last_cell.value, FMT)

headers = last_cell = wks.get_values(
    start=(1, 1), end=(1, wks.cols), returnas="cell", include_tailing_empty=False
)[0]
nutr_to_column = {}
for h in headers:
    nutr_to_column[h.value] = h.col - 1

date_range = [
    datetime.fromordinal(i)
    for i in range(
        (last_date + timedelta(days=1)).toordinal(), datetime.today().toordinal()
    )
]

client = myfitnesspal.Client("HaroldMartin128")
for day in date_range:
    row += 1
    nutrs = [None] * len(nutr_to_column)
    nutrs[0] = day.strftime(FMT)
    mfp_nutrs = client.get_date(day)
    for nutrient, amount in mfp_nutrs.totals.items():
        if nutrient in nutr_to_column:
            nutrs[nutr_to_column[nutrient]] = amount
    wks.update_values((row, 1), [nutrs])
