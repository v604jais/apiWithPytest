import requests
from Get import Get   

def test_get_api():
    g = Get(1)
    res = g.get_api(1)
    json_data = res.json()
    print("✅ Status Code:", res.status_code)
    print("✅ Response Body:")
     # If response is a list
    if isinstance(json_data, list):
        for item in json_data:
            for key, value in item.items():
                print(f"{key} : {value}")
    else:
        for key, value in res.json().items():
            print(f"{key} : {value}")

    assert res is not None
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
     # Checking if "name" exists in each item of the list
    for item in json_data:
        assert "name" in item, "Missing 'name' key in one of the response items"

    first_item = json_data[0]
    # checking the type of 'id'
    assert isinstance(first_item["id"], str), "'id' should be a string"