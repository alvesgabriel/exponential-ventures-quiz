def test_home_status_code(client):
    resp = client.get("/")
    assert resp.status_code == 200
