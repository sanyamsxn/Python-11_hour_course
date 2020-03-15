problems='broke, pale, nerdy, short'
print(problems)

#converting it into list using split function\
l=problems.split(", ")                        # splitting elements in  problems by every , present in problems.
print(l)

zl=problems.split("pale")
print(zl)


xl=problems.split("nerdy")
print(xl)

  ##------join fn-------##
joined=' and '.join(l)       #give  space before and after delimeter so to avoid shrinking of the output.
print(joined)

csv=','.join(l)
print(csv)