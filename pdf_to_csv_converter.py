import time
import csv

import pandas as pd
import numpy as np

import camelot


COLUMNS = ["id", "date", "voivodeship", "district", "sex", "description"]


def convert_pdf_to_csv(path_in: str, pages: str = "all", remove_new_lines: bool = True) -> pd.DataFrame:
    time_start = time.time()

    data_camelot = camelot.read_pdf(path_in, pages=pages)

    df = pd.concat([x.df for x in data_camelot], axis=0)

    if df.iloc[0, 0] == "NR":
        df = df.iloc[1:, :]

    df.columns = COLUMNS

    df = df.reset_index(drop=True)

    df["id"] = df["id"].replace("", np.nan)
    df["id"] = df["id"].ffill()

    df = df.groupby("id").agg(lambda x: "\n".join(x) if list(x)[-1] != "" else list(x)[0]).reset_index()

    if remove_new_lines:
        df = df.replace(r"\s+", " ", regex=True)

    df = df.astype({"id": "int32"})
    df = df.sort_values(by=["id"])

    print(f"Finished converting in: {time.time() - time_start:.1f} sec")
    return df


if __name__ == "__main__":
    path_in = "nops.pdf"
    path_out = "nops.csv"

    df_nops = convert_pdf_to_csv(path_in=path_in, pages="all", remove_new_lines=True)  # example: "1,3,4" or "1,4-end" or "all"

    df_nops.to_csv(path_out, index=False, encoding="UTF-8", sep=";", quoting=csv.QUOTE_ALL)
    print(f"Data saved to: {path_out}")
