from typing import Generator
import pytest
import json
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, ) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:8000"
    )
    yield request_context ##Accesar al contexto y interactuar sus funciones

    request_context.dispose()


def test_get_trucks(api_request_context:APIRequestContext) -> None:
    get_data = api_request_context.get(
        f"/api/truck"
    )
    if get_data.ok:
        print(f"Solicitud Exitosa")
    else:
        print("Error en la solicitud")
    assert get_data.ok
    

    get_response = get_data.json()

    print("")
    print(get_data)
    print(f"resposne: {get_response}")

def test_get_truck(api_request_context:APIRequestContext) -> None:
    truck = 2
    get_data = api_request_context.get(
        f"/api/truck/{truck}"
    )
    assert get_data.ok
    if get_data.ok:
        print("Solicitud Exitosa GET")
    else:
        print("Error en la solicitud")

    get_response = get_data.json()

    print("")
    print(get_data.json())
    print(f"resposne: {get_response}")

def test_post_truck(api_request_context:APIRequestContext) -> None:
    data = {
        "model": "Kw T800",
        "number_plate": "YTR-864",
        "capacity": "20T",
        "status": "Disponible"
    }
    post_data = api_request_context.post(
        f"/api/truck", data=data
    )
    assert post_data.ok

    if post_data.ok:
        print("Solicitud Exitosa POST")
    else:
        print("Error en la solicitud")

    ##get_response = get_data.json()


    # return{
    #         "success": True,
    #         "data": json.dumps(post_data, default=str),
    #     }
    #print(f"todo var: {post_data}")