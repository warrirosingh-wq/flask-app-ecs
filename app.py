from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, welcome to DevOps Zero To Hero (Junoon  Batch 9)'

@app.route('/health')
def health():
    return 'Server is up and running'
def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
