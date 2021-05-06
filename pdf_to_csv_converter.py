import time
import csv

import pandas as pd

import camelot


COLUMNS = ["id", "date", "voivodeship", "district", "sex", "description"]


def convert_pdf_to_csv(path_in: str, pages: str = "all", remove_new_lines: bool = True) -> pd.DataFrame:
    time_start = time.time()

    data_camelot = camelot.read_pdf(path_in, pages=pages)
    dfs_pages = [x.df for x in data_camelot]

    df_all = dfs_pages[0]

    for df_page in dfs_pages[1:]:
        df_all = _add_new_page(df_all, df_page)

    df_all = _remove_header(df_all)

    df_all.columns = COLUMNS

    df_all = df_all.reset_index(drop=True)

    if remove_new_lines:
        df_all = df_all.replace(r"\s+", " ", regex=True)

    df_all = df_all.astype({"id": "int32"})
    df_all = df_all.sort_values(by=["id"])

    print(f"Finished converting in: {time.time() - time_start:.1f} sec")
    return df_all


def _add_new_page(all: pd.DataFrame, page: pd.DataFrame) -> pd.DataFrame:
    if all.iloc[-1, 0] == "" or page.iloc[0, 0] == "":
        all.iloc[-1] = _merge_rows(all.iloc[-1, :], page.iloc[0, :])
        page = page.iloc[1:, :]
    all = pd.concat([all, page])
    return all


def _merge_rows(row1: pd.Series, row2: pd.Series):
    return row1.combine(row2, lambda x, y: _concatenate_text(x, y))


def _concatenate_text(x, y):
    if x == "":
        return y
    if y == "":
        return x

    return f"{x}\n{y}"


def _remove_header(df: pd.DataFrame) -> pd.DataFrame:
    if df.iloc[0, 0] == "NR":
        df = df.iloc[1:, :]
    return df


if __name__ == "__main__":
    path_in = "nops.pdf"
    path_out = "nops.csv"

    df_nops = convert_pdf_to_csv(path_in=path_in, pages="all", remove_new_lines=True)  # example: "1,3,4" or "1,4-end" or "all"

    df_nops.to_csv(path_out, index=False, encoding="UTF-8", sep=";", quoting=csv.QUOTE_ALL)
    print(f"Data saved to: {path_out}")
