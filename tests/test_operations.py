from classes.operations import Operations


def test_operations_repr():
    operations = Operations([{'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'}])
    expected_repr = [{'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'}]
    assert operations.__repr__() == f"Operations({expected_repr})"

