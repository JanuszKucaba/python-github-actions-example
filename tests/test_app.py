from app import index


def test_index():
    assert index() == 'Test CI/CD!'