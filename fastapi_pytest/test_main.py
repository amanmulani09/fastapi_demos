from fastapi.testclient import TestClient # import TestClient 
from main import app # Import app from original 

client = TestClient(app)


# create test cases 

def test_create_task():
    response = client.post(
        "/task",
        json={"id":"1","title":"Test Title","completed":False}
    )
    
    assert response.status_code == 200 # assert means equal to or to check with 
    assert response.json()['title'] == "Test Title"
    
    
def test_get_tasks():
    response = client.get('/tasks')
    
    assert response.status_code == 200
    assert isinstance(response.json(),list)
    

def test_get_task_by_id():
    response = client.get('/task/1')
    
    assert response.status_code == 200
    assert response.json()['id'] == 1
    
    
def test_task_not_found():
    response = client.get('task/999')
    
    assert response.status_code == 404
    print(response.json())
    assert response.json()['detail'] == "Task Not Found"