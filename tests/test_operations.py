from classes.operations import Operations


def test_operations_repr():
    operations = Operations([{'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'}])
    expected_repr = [{'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'}]
    assert operations.__repr__() == f"Operations({expected_repr})"


def test_operations_set_last_operations():
    all_operations = [
        {'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'},
        {'id': 2, 'date': '2022-01-02T12:00:00', 'description': 'Operation 2'},
        {'id': 3, 'description': 'Operation 3'}
    ]
    operations = Operations(all_operations)
    assert len(operations._Operations__last_operations) == 2
    assert operations._Operations__last_operations[0]['id'] == 2
    assert operations._Operations__last_operations[1]['id'] == 1
