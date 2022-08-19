import json
import py_vapid

# Included in py_vapid
from cryptography.hazmat.primitives import serialization

def format_string(value):
    """Formats a string to a JSON-like format"""
    return json.dumps(value).replace('"', '')

# Create new instance and generate a new set of keys
vapid = py_vapid.Vapid()
vapid.generate_keys()

# Generate the applicationServerKey value to embed in the HTML site
raw_pub = vapid.public_key.public_bytes(
    serialization.Encoding.X962,
    serialization.PublicFormat.UncompressedPoint
)

# Output a .env file to be used on the server
print("APPLICATION_SERVER_KEY={}\nPRIVATE_KEY={}\nPUBLIC_KEY={}".format(
    format_string(py_vapid.b64urlencode(raw_pub)),
    format_string(str(vapid.private_pem(), 'utf-8')),
    format_string(str(vapid.public_pem(), 'utf-8'))))
