import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

print(df)
print("")
for index in df.index:

    df.at[index, 'Gaji'] = (lambda x: x + x * (5/100))(df.at[index, 'Gaji'])
print("Dataframe dengan peningkatan gaji 5%")
print(df)
print("")

for index in df.index:
    df.at[index, 'Gaji'] = (lambda x, y: x * (1 + 2/100) if y > 30 else x)(df.at[index, 'Gaji'], df.at[index, 'Usia'])
print("Dataframe dengan peningkatan gaji tambahan 2% lagi jika Usia diatas 30 tahun")
print(df)

