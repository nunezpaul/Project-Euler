'''
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total

how many letters 1 - 1000?

For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage
'''

numbers = range(1, 1000)

hundreds = {'0': 0, '1': len('onehundred'), '2': len('twohundred'), '3': len('threehundred'), '4':len('fourhundred'), '5':len('fivehundred'), '6':len('sixhundred'), '7':len('sevenhundred'), '8': len('eighthundred'), '9':len('ninehundred')}

tens = {'0': 0, '1': 0, '2': len('twenty'), '3': len('thirty'), '4':len('forty'), '5':len('fifty'), '6':len('sixty'), '7':len('seventy'), '8': len('eighty'), '9':len('ninety')}

ones = {'0': 0, '1': 3, '2': 3, '3': 5, '4':4, '5':4, '6':3, '7':5, '8': 5, '9':4}

teens = {'10': len('ten'), '11': len('eleven'), '12': len('twelve'), '13': len('thirteen'), '14': len('fourteen'), '15': len('fifteen'), '16': len('sixteen'), '17':  len('seventeen'), '18': len('eighteen'), '19': len('nineteen')}


num2word_len = 0

for i in numbers:  
    
    number = list(str(i).zfill(3))
    
    num2word_len += hundreds[number[0]]
    
    if number[0] != '0' and number[1]+number[2] != '00':
        #adding the 'and' if there is a hundred that is not followed by 00
        num2word_len+=3
        
    
    if number[1] == '1':
        num2word_len += teens[number[1]+number[2]]
    else:
        num2word_len += tens[number[1]]
        num2word_len += ones[number[2]]

num2word_len += len('onethousand')
