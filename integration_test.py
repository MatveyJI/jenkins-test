import requests
import subprocess
import time
import sys

def start_service(script, port):
    """Запускает сервис в фоновом режиме"""
    proc = subprocess.Popen([sys.executable, script, str(port)])
    time.sleep(2)  
    return proc

def test_service(url, expected_text):
    """Проверяет, что сервис отвечает корректно"""
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200 and expected_text in resp.text:
            print(f"✓ {url} — OK")
            return True
        else:
            print(f"✗ {url} — FAIL: {resp.status_code}, {resp.text}")
            return False
    except Exception as e:
        print(f"✗ {url} — ERROR: {e}")
        return False

if __name__ == '__main__':
    print("Starting integration test...")
    
    s1 = start_service('service1.py', 5000)
    s2 = start_service('service2.py', 5001)
    
    try:
        success = True
        success &= test_service('http://localhost:5000', 'Service 1')
        success &= test_service('http://localhost:5001', 'Service 2')
        
        print("\nTesting inter-service communication...")
        resp1 = requests.get('http://localhost:5000')
        resp2 = requests.get('http://localhost:5001')
        
        if resp1.status_code == 200 and resp2.status_code == 200:
            print("✓ Both services are reachable and responding")
        else:
            print("✗ Communication test failed")
            success = False
        
        # Итог
        if success:
            print("\n Integration test PASSED")
            sys.exit(0)
        else:
            print("\n Integration test FAILED")
            sys.exit(1)
            
    finally:
        s1.terminate()
        s2.terminate()
        s1.wait()
        s2.wait()