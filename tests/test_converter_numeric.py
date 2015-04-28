import schematec.converters as converters


def test_zero():
    assert converters.numeric(0) == 0


def test_positive_number():
    assert converters.numeric(1) == 1


def test_negative_number():
    assert converters.numeric(-1) == -1


def test_long():
    assert converters.numeric(1L) == 1


def test_positive_number_string():
    assert converters.numeric('1') == 1


def test_negative_number_string():
    assert converters.numeric('-1') == -1


def test_positive_number_unicode_string():
    assert converters.numeric(u'1') == 1


def test_negative_number_unicode_string():
    assert converters.numeric(u'-1') == -1
