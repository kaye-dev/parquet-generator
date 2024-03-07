import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

print('Parquet start')

# CSV ファイルを読み込む
df = pd.read_csv('./data.csv')

# 明示的に型を指定したい場合のみ以下のように列に対して型を指定する
# 'population' 列のデータ型を int32 に変更 (明示的に指定しないと int64 になる)
df['population'] = df['population'].astype('int32')

# DataFrame を Parquet ファイルに変換
table = pa.Table.from_pandas(df, preserve_index=False)

# Parquet ファイルとして保存
pq.write_table(table, './data.parquet')

# Parquet ファイルのパスを指定
file_path = './data.parquet'

# Parquet ファイルを読み込む
parquet_file = pq.ParquetFile(file_path)

# ファイルのスキーマ情報を取得
schema = parquet_file.schema

# スキーマ情報から列名とデータ型を表示
for field in schema:
    print(f'Column name: {field.name}, Data type: {field.physical_type}')

print('Parquet file has been created successfully.')
