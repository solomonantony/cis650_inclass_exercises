class ItemsError(Exception):
    pass
class RangeError(Exception):
    pass
def parse_grade(record):
    try:
        items = record.split()
        if len(items) != 3: 
            raise ItemsError("Not 3 items")
        else:
            id, name, grade = items[0], items[1], int(items[2])
        grade = int(grade)
        if grade < 0 or grade > 100: raise RangeError
    except ItemsError:
        print("Must have three items")
    except ValueError:
        print("Grade must be an integer")
    except RangeError:
        print('Grade must be in the 0 to 100 range.')
    else:
        return id, name, grade

print(parse_grade('101 Ana 185'))

