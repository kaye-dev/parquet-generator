import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

print('Parquet start')

# CSV ファイルを読み込む
df = pd.read_csv('./data.csv')

# DataFrame を Parquet ファイルに変換
table = pa.Table.from_pandas(df)

# Parquet ファイルとして保存
pq.write_table(table, './data.parquet')

print('Parquet file has been created successfully.')
