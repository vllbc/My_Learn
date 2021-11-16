from collections import namedtuple

Test = namedtuple("Test", ['name', 'age', 'sex'])

def test_for_test(name: str, year: int, sex: str) -> Test:
    return Test(
        name=name.title(),
        age=2021 - year,
        sex=sex
    )

name,age,sex = test_for_test('wlb', 2002, 'male')
print(name, age, sex)