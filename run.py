import sys
from app import create_app 
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = create_app()

if __name__ == "__main__":
    # Cambiar `host='127.0.0.1'` o `host='localhost'` a `host='0.0.0.0'`
    app.run(host='0.0.0.0', port=5000, debug=True)

