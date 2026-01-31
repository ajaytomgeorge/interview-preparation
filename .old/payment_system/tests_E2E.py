from fastapi.testclient import TestClient

from main import app

clinet= TestClient(app)

def test_get_ip():
    response = clinet.get("/ip/?id=3")
    print(response)
    assert response.status_code == 2005

