from pykakasi import kakasi


jp = "綴じ眼のシオラ"

kks = kakasi()

result = kks.convert(
    jp
)

furi = " ".join(
[
x["hira"]
for x in result
])


print(
"\nJP:\n"
)

print(
jp
)

print(
"\nFURI:\n"
)

print(
furi
)