from utils.api_client import APIClient
from utils.logger import setup_logger

logger = setup_logger()


def test_auth_flow():
    """
    Test authentication token generated with username and password
    """
    logger.info("Testing Authorization")
    api = APIClient()
    payload = api.load_api_data()["admin_credentials"]

    response = api.post('/auth', payload)
    logger.info(f"Response: {response.json()}")
    assert response.status_code == 200, f"Response code is {response.status_code}, but 200 was expected"
    assert 'token' in response.json()
    logger.info("Authorization Successful!")
