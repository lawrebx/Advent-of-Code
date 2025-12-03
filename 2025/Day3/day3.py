with open('input.txt', 'r') as f:
    content = f.read()

banks = content.splitlines()

joltages = []

for bank in banks:

    bank_snipped = bank[:-1]

    max_joltage = max(bank_snipped)

    max_idx = bank.index(max_joltage)
    remaining_batts = bank[max_idx+1:]

    next_joltage = max(remaining_batts)

    bank_joltage = str(max_joltage) + str(next_joltage)
    joltages.append(int(bank_joltage))

print(f'Part 1 - Total Joltage: {sum(joltages)}')

def get_joltages(bank, tgt_batt_count):

    batt_count = 0
    max_idx = 0

    bank_joltage = None

    while batt_count < tgt_batt_count:

        offset = ((tgt_batt_count-1)-batt_count)*-1

        if offset >= 0:
            bank_snipped = bank[max_idx:]
        else:
            bank_snipped = bank[max_idx:offset]

        max_joltage = max(bank_snipped)

        max_idx = max_idx + bank_snipped.index(max_joltage) + 1

        if bank_joltage == None:
            bank_joltage = str(max_joltage)
        else:
            bank_joltage = bank_joltage + str(max_joltage)
        
        batt_count = batt_count + 1

    return bank_joltage

joltages = []

tgt_batt_count = 12

for bank in banks:
    joltages.append(int(get_joltages(bank,tgt_batt_count)))

print(f'Part 2 - Total Joltage ({tgt_batt_count} Batteries): {sum(joltages)}')


