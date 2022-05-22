import pandas as pd
from hashlib import md5

def solution(filename):
    df = pd.read_csv(filename)
    df = df.reset_index(drop=True)
    df_new = df.iloc[range(2,len(df),2), 3]
    df_string = df_new.to_string() 
    return md5(df_string.encode("utf-8")).hexdigest()


def main():
    #sol = solution("annual-enterprise-survey-2020-financial-year-provisional-csv.csv")
    sol = solution("testcase.csv")
    assert(sol == "821fa74b50ba3f7cba1e6c53e8fa6845")

if __name__ == "__main__":
    main()