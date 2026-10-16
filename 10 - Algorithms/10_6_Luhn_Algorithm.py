def verify_card_number(card_num: str):
    dub_arr = []
    sum_arr = []
    chrat = []

    for c in range(len(card_num)):
        if card_num[c].isdigit():
            chrat.append(int(card_num[c]))  
 
    for i in range(len(chrat)):
        if len(chrat)%2 != 0:
            if i%2 != 0:
                dub_arr.append(chrat[i] * 2)
            else:
                dub_arr.append(chrat[i])
       
        else:
            if i%2 != 0:
                dub_arr.append(chrat[i])
            else:
                dub_arr.append(chrat[i] * 2)

    for d in dub_arr:
        if d > 9:
            sum_arr.append(d - 9)
        else:
            sum_arr.append(d)

    dig_sum = sum(sum_arr)

    if dig_sum % 10 != 0:
        return 'INVALID!'
    else:
        return 'VALID!'

print(verify_card_number('4111-1111-1111-1111'))