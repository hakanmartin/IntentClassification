import pandas as pd

df = pd.read_excel("/Users/hakanmartin/PycharmProjects/pythonProject1/Test-1000-3.xlsx")

# "TR" sütunundaki metinlerin ilk harfini büyük harfe dönüştür
df["TR"] = df["TR"].apply(lambda x: x[0].upper() + x[1:] if isinstance(x, str) else x)

df.to_excel("/Users/hakanmartin/PycharmProjects/pythonProject1/Test-1000-3.xlsx", index=False)


# Cumlelerin ilk harflerini buyuk harf yapma...