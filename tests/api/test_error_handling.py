from utils.api_client import APIClient


def test_404_error():
    """
    Test 404 error when resource in API request is not found
    """
    api = APIClient()
    response = api.get('/unknown/9999')
    assert response.status_code == 404