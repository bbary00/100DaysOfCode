import csv 


def read_rolls():
    all_pairs = dict()
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            all_pairs.update(read_roll(row))
        return all_pairs


def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']
    return {name: row}
