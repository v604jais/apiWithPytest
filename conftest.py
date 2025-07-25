import pytest
from datetime import datetime

@pytest.fixture(scope="session")
def test_setup():
    print("\n[Setup] Initializing resources...")

    # Setup code here (e.g., connect to DB, open browser)
    yield

    print("\n[Teardown] Releasing resources...")
    # Teardown code here (e.g., close DB/browser)

@pytest.fixture(scope="function")
def time_taken():
    starttime=datetime.now()
    yield
    endtime=datetime.now()    
    print("time taken by method",endtime-starttime)

 