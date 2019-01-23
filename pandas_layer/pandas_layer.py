import pandas as pd
import numpy as np


def read_csv_from_s3(bucket: str,
                     key: str,
                     separator: str = ",",
                     encoding: str = "utf-8"):
    s3_url = 's3://{bucket}/{key}'.format(bucket=bucket, key=key)
    return pd.read_csv(s3_url,
                       sep=separator,
                       encoding=encoding)
