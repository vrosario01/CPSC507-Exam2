from problem1 import filter_grades


def test_all_lessthan_num(capsys):
    filter_grades({'Ben': 70, 'Marge': 79, 'Billy': 68, 'Sam': 50}, 80)
    assert capsys.readouterr().out == ""

    filter_grades({'Jo': 55, 'Matt': 65, 'May': 80, 'Lewis': 83}, 84)
    assert capsys.readouterr().out == ""


def test_all_above_threshold(capsys):
    filter_grades({'May': 95, 'Bob': 98, 'Lewis': 87, 'Todd': 90}, 85)
    assert capsys.readouterr().out == "'May'\n'Bob'\n'Lewis'\n'Todd'\n"

    filter_grades({'Joe': 85, 'Bobby': 82, 'Yelitza': 100, 'Katy': 94}, 82)
    assert capsys.readouterr().out == "'Joe'\n'Yelitza'\n'Katy'\n"


def test_all_grades_are_threshold(capsys):
    filter_grades({'May': 95, 'Bob': 95, 'Lewis': 95, 'Todd': 95}, 95)
    assert capsys.readouterr().out == ""