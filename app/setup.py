import json
import py_vapid
import secrets

# Included in py_vapid
from cryptography.hazmat.primitives import serialization

def format_string(value):
    """Formats a string to a JSON-like format"""
    return json.dumps(value).replace('"', '')

# Create new instance and generate a new set of keys
vapid = py_vapid.Vapid()
vapid.generate_keys()

# Given how PEM key is generated, we can make a similar approach to have the same key in DER format
# See: https://github.com/web-push-libs/vapid/blob/a60bcc820a381d46576ade2a22df5480ab4f154c/python/py_vapid/__init__.py#L203
private_key_der = vapid.private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Generate the applicationServerKey value to embed in the HTML site
raw_pub = vapid.public_key.public_bytes(
    serialization.Encoding.X962,
    serialization.PublicFormat.UncompressedPoint
)

# Output a .env file to be used on the server
print("APPLICATION_SERVER_KEY={}\nPRIVATE_KEY_PEM={}\nPUBLIC_KEY_PEM={}\nPRIVATE_KEY_DER={}\nSECRET_KEY={}".format(
    format_string(py_vapid.b64urlencode(raw_pub)),
    format_string(str(vapid.private_pem(), 'utf-8')),
    format_string(str(vapid.public_pem(), 'utf-8')),
    format_string(py_vapid.utils.b64urlencode(private_key_der)),
    secrets.token_hex()))
