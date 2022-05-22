import pandas as pd
from hashlib import md5

def solution(filename):
    df = pd.read_csv(filename)
    df_new = df.iloc[range(1,len(df),2), 2]
    df_new = df_new.reset_index(drop=True)
    concat = ''.join(str(i) for i in df_new)
    return md5(concat.encode("utf-8")).hexdigest()


def main():
    sol = solution("annual-enterprise-survey-2020-financial-year-provisional-csv.csv")
    print(sol)


    #Test case
    #sol = solution("testcase.csv")
    #assert(sol == "821fa74b50ba3f7cba1e6c53e8fa6845")

if __name__ == "__main__":
    main()