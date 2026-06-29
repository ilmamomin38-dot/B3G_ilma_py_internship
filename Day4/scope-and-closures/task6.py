def make_validator(min_value):
    def validata(num):
        return num>=min_value
    return validata

validator_10=make_validator(10)
validator_50=make_validator(50)
print(validator_10(5))
print(validator_10(15))
print(validator_10(20))
print(validator_50(20))
print(validator_50(50))
print(validator_50(34))