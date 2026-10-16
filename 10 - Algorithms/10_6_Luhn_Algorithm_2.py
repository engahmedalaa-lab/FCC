def verify_card_number(card_number):
    digits_list = [int(d) for d in card_number if d.isdigit()]

    total = 0

    digits_list.reverse()

    for ind, digit in enumerate(digits_list):
        if ind % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return "VALID!" if total % 10 == 0 else "INVALID!"

print(verify_card_number('453914889'))
print(verify_card_number('4 5 3 9 14889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('1234 5678 9012 3456'))