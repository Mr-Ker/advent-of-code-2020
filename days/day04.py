from days.day import Day
import re


class Passport():
    def __init__(self, **kwargs):
        self.passport_key_values = kwargs

    def is_birth_year_valid(self):
        try:
            birth_year = int(self.passport_key_values['byr'])
        except KeyError:
            return False

        result = False
        if birth_year >= 1920 and birth_year <= 2002:
            result = True

        return result

    def is_issue_year_valid(self):
        try:
            issue_year = int(self.passport_key_values['iyr'])
        except KeyError:
            return False

        result = False
        if issue_year >= 2010 and issue_year <= 2020:
            result = True

        return result

    def is_expiration_year_valid(self):
        try:
            expiration_year = int(self.passport_key_values['eyr'])
        except KeyError:
            return False

        result = False
        if expiration_year >= 2020 and expiration_year <= 2030:
            result = True

        return result

    def is_height_valid(self):
        try:
            height = self.passport_key_values['hgt']
        except KeyError:
            return False

        result = False

        match = re.match(r"([0-9]+)([a-z]+)", height, re.I)
        if match:
            height, unit = match.groups()
            height = int(height)

            if unit == 'cm' and height >= 150 and height <= 193:
                result = True
            elif unit == 'in' and height >= 59 and height <= 76:
                result = True

        return result

    def is_hair_color_valid(self):
        try:
            hair_colour = self.passport_key_values['hcl']
        except KeyError:
            return False

        match = re.match(r"^#([0-9]|[a-f]){6}$", hair_colour, re.I)
        return match and len(hair_colour) == 7

    def is_eye_color_valid(self):
        try:
            eye_colour = self.passport_key_values['ecl']
        except KeyError:
            return False

        return eye_colour in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_passport_id_valid(self):
        try:
            passport_id = self.passport_key_values['pid']
        except KeyError:
            return False

        match = re.match(r"^[0-9]{9}$", passport_id, re.I)
        return match

    def is_valid(self):
        return (self.is_birth_year_valid() and self.is_issue_year_valid() and
                self.is_expiration_year_valid() and self.is_height_valid() and
                self.is_hair_color_valid() and self.is_eye_color_valid() and
                self.is_passport_id_valid())

    def contains_all_mandatory_fields(self):
        return (('byr' in self.passport_key_values)
                and ('iyr' in self.passport_key_values)
                and ('eyr' in self.passport_key_values)
                and ('hgt' in self.passport_key_values)
                and ('hcl' in self.passport_key_values)
                and ('ecl' in self.passport_key_values)
                and ('pid' in self.passport_key_values))


class Day04(Day):
    def __init__(self):
        super().__init__()
        self.passports = []
        self.parse_passerports()

    def parse_passerports(self):
        passport = {}
        for line in self.lines:
            if line != "":
                key_values = line.split(" ")
                for key_value in key_values:
                    key, value = key_value.split(":")
                    passport[key] = value
            else:
                self.passports.append(Passport(**passport))
                passport = {}
        if passport is not None:
            self.passports.append(Passport(**passport))

    def part1(self):
        result = 0
        for passport in self.passports:
            if passport.contains_all_mandatory_fields():
                result += 1
        return result

    def part2(self):
        result = 0
        for passport in self.passports:
            if passport.is_valid():
                result += 1
        return result
