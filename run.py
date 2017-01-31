#!flask/bin/python
import os
from app import app
port = int(os.environ.get("PORT", 33507))
app.run(port=port, debug=True)