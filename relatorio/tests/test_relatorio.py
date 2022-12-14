

def test_sales(client):
    response = client.get("/sales")
    assert response.status_code == 200 
    assert "Vagem" in response.text   

def test_best_sellers(client):
    response = client.get("/best_sellers")
    assert response.status_code == 200 
    assert '{"Menssage":"No items sold"}' not in response.text


def test_amount_sales(client):
    response = client.get("/amount_sales")
    assert response.status_code == 200 
    assert '{"Menssage":"No items sold"}' not in response.text


def test_top_ten(client):
    response = client.get("/top_ten")
    assert response.status_code == 200 
    assert '{"Menssage":"No items sold"}' not in response.text


def test_less_sold(client):
    response = client.get("/less_sold")
    assert response.status_code == 200 
    assert '{"Menssage":"No items sold"}' not in response.text


def test_get_iten(client):
    response = client.get("/get_iten/Vagem")
    assert response.status_code == 200 
    assert '{"Menssage": "iten not found"}' not in response.text


# def test_clean_table(client):
#     response = client.delete('/clean_table')
#     print(response.text)
#     assert response.status_code == 204 
    
