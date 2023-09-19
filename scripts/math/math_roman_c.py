# roman numerals
# one to one hundred


# appending roman numerals to a list
def roman():
    # base numerals
    numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    
    roman.nums = []


    for a in numerals:
        roman.nums.append(a)

    for b in numerals:
        bb = "X" + b
        roman.nums.append(bb)

    for c in numerals:
        cc = "XX" + c
        roman.nums.append(cc)

    for d in numerals[0:-1]:
        dd = "XXX" + d
        roman.nums.append(dd)
    roman.nums.append("XL")    

    for e in numerals[:-1]:
        ee = "XL" + e
        roman.nums.append(ee)
    roman.nums.append("L")    

    for f in numerals:
        ff = "L" + f
        roman.nums.append(ff)

    for g in numerals:
        gg = "LX" + g
        roman.nums.append(gg)

    for h in numerals:
        hh = "LXX" + h
        roman.nums.append(hh)

    for i in numerals[:-1]:
        ii = "LXXX" + i
        roman.nums.append(ii)
    roman.nums.append("XC")

    for j in numerals[:-1]:
        jj = "XC" + j
        roman.nums.append(jj)
    roman.nums.append("C")
#  ==============================================

# convert arabic to roman 
def math_roman(num=int):
    roman()

    # finding the appropiate roman numeral
    for n in roman.nums:
        if num - 1 == roman.nums.index(n):
            print(n)

#  ==============================================