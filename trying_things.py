import pandas as pd


df = pd.DataFrame([['ABBOTSFORD', 427000, 448000],
                     ['ABERFELDIE', 534000, 600000]],
                    columns=['Locality', 2005, 2006])

print(df)

df2 = df.set_index('Locality', inplace=True)

print(df2)