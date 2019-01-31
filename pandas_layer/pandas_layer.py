import pandas as pd
import numpy as np
import re

import boto3

s3 = boto3.resource('s3')


def read_csv_from_s3(bucket: str,
                     key: str,
                     separator: str = ",",
                     encoding: str = "utf-8"):
    s3_url = 's3://{bucket}/{key}'.format(bucket=bucket, key=key)
    return pd.read_csv(s3_url,
                       sep=separator,
                       encoding=encoding)


def write_json_to_s3(bucket: str, key: str, data):
    s3.Object(bucket, key).put(Body=data)


def match_s3_key(event):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        p = re.compile(r'^(\w+)/(\w+)/(\w+)/(\w+)/(\d+)/([^/]+)[.](csv?)$', flags=re.IGNORECASE)
        m = p.match(key)
        if not m:
            raise ValueError('S3 key does not satisfy pattern')

        (condition, confidentiality, dataset, version, edition, prefix, suffix) = m.groups()
        return bucket, key, {'condition': condition,
                             'confidentiality': confidentiality,
                             'dataset': dataset,
                             'version': version,
                             'edition': edition,
                             'prefix': prefix,
                             'suffix': suffix
                             }
