import time
from utils.api_client import APIClient
from jsonschema import validate
from utils.logger import setup_logger

logger = setup_logger()


def test_create_booking_and_response_time_and_schema():
    """
    Test to test Create booking api and assert the response
    time is less than 3 seconds and validate the response schema
    """

    logger.info("Testing Creating Booking....")
    api = APIClient()
    payload = api.load_api_data()["create_booking_data"]

    start = time.time()
    response = api.post('/booking', payload)
    duration = time.time() - start

    # verify response code
    assert response.status_code == 200
    logger.info("Booking Created Successfully!")
    # verify response schema
    logger.info("Verifying response schema...")
    schema = api.load_schemas()
    validate(instance=response.json(), schema=schema)
    logger.info("Response schema verified.")
    # verify response time
    logger.info("Verifying response time is less than 3 seconds....")
    assert duration < 3
    logger.info(f"Response time is {duration}")


def test_get_booking():
    """
    Test Read booking API
    """
    api = APIClient()
    booking_id = api.create_booking_id()
    response = api.get(f'/booking/{booking_id}')
    # verify response code
    assert response.status_code == 200


def test_update_booking():
    """
    Test update booking API
    """
    api = APIClient()
    booking_id = api.create_booking_id()
    headers = api.create_admin_headers()
    payload = api.load_api_data()["create_booking_data"]
    response = api.put(f'/booking/{booking_id}', payload, headers=headers)
    # verify response code
    assert response.status_code == 200


def test_delete_booking():
    """
    Test Delete booking API
    """
    api = APIClient()
    booking_id = api.create_booking_id()
    headers = api.create_admin_headers()
    response = api.delete(f'/booking/{booking_id}', headers=headers)
    # verify response code
    assert response.status_code == 201
