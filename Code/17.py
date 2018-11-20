a1 = 'one'
a2 = 'two'
a3 = 'three'
a4 = 'four'
a5 = 'five'
a6 = 'six'
a7 = 'seven'
a8 = 'eight'
a9 = 'nine'

a10 = 'ten'
a11 = 'eleven'
a12 = 'twelve'
a13 = 'thirteen'
a14 = 'fourteen'
a15 = 'fifteen'
a16 = 'sixteen'
a17 = 'seventeen'
a18 = 'eighteen'
a19 = 'nineteen'

a20 = 'twenty'
a30 = 'thirty'
a40 = 'forty'
a50 = 'fifty'
a60 = 'sixty'
a70 = 'seventy'
a80 = 'eighty'
a90 = 'ninety'

a100 = 'hundred'
aand = 'and'
a1000 = 'thousand'

one_nine = len(a1) + len(a2) + len(a3) + len(a4) + len(a5) + len(a6) + len(a7) + len(a8) + len(a9)
ten_nineteen = len(a10) + len(a11) + len(a12) + len(a13) + len(a14) + len(a15) + len(a16) + len(a17) + len(a18) + len(a19)
twenty_ninetynine = 10 * (len(a20) + len(a30) + len(a40) + len(a50) + len(a60) + len(a70) + len(a80) + len(a90)) + 8 * one_nine
one_ninetynine = one_nine + ten_nineteen + twenty_ninetynine

onehundred_ninehundredandninetynine = 100 * one_nine + 900 * len(a100) + 99 * 9 * len(aand) + 9 * one_ninetynine
onethousand = len(a1) + len(a1000)

print(one_ninetynine + onehundred_ninehundredandninetynine + onethousand)