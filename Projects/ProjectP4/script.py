import pandas as pd

df = pd.read_csv('clicks.csv')

print(df.head(5))

df['is_purchase'] = df.click_day.apply(
lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

print(df.head(5))
print('\n')

purchase_counts = df.groupby(['group', 'is_purchase']).user_id.count().reset_index()
print(purchase_counts)