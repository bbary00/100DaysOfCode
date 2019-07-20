import csv
import collections

data = []

Record = collections.namedtuple(
    'Record',
    'name, age, gender, raceethnicity, month, day, year, streetaddress, '
    'city, state, latitude, longitude, state_fp, county_fp, tract_ce, '
    'geo_id, county_id, namelsad, lawenforcementagency, cause, armed, '
    'pop, share_white, share_black, share_hispanic, p_income, h_income, '
    'county_income, comp_income, county_bucket, nat_bucket, pov, urate, '
    'college'
)


def init():
    with open('./data/police_killings.csv', 'r', encoding='utf-8',
              errors='ignore') as f:
        reader = csv.DictReader(f)
        return list(reader)


def killing_by_race(data):
    print(f"Total number of killing: {len(data)}")
    white = [case for case in data if case['raceethnicity'] == 'White']
    black = [case for case in data if case['raceethnicity'] == 'Black']
    unknown = [case for case in data if case['raceethnicity'] == 'Unknown']
    else_race = [case for case in data if case not in white+black+unknown]
    print(f"Where white: {len(white)} black: {len(black)} unknown:"
          f" {len(unknown)} and else different races: {len(else_race)}")


def age_info(data):
    ages = [int(case['age']) for case in data if case['age'].isdigit()]
    print(f"The average age is {sum(ages)//len(ages)} where the youngest is "
          f"{min(ages)} and the oldest is {max(ages)}.")


all_data = init()
killing_by_race(all_data)
age_info(all_data)
