import Test_python_mocks.mocker.mock1 as mock1
from Test_python_mocks.mocker.mock1 import create_player
 
class MockResponse:
 
    @staticmethod
    def get_info():
        return {"name": "test", "level" : 200}
 
def test_create_player(monkeypatch):
 
    def mock_get(*args, **kwargs):
        return MockResponse()
 
    monkeypatch.setattr('mock1.Player', mock_get)
 
    expected_value = {"name": "test", "level" : 200}
    assert create_player() == expected_value