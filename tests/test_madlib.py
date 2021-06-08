import pytest
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("assets/test.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual=parse_template('life is really {Adjective},and there is no {verb}')    
    expected=['Adjective','verb'],'life is really $,and there is no $'
    assert actual == expected

def test_merge():
    actual=merge('life is really $,and there is no $',['boring','thing to do '])  
    excepted=  'life is really boring,and there is no thing to do $'


@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
