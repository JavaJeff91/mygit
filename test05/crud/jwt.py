import jwt, Crypto.PublicKey.RSA as RSA, datetime

key = RSA.generate(2048)
priv_pem = key.exportKey()
pub_pem = key.publickey().exportKey()
payload = { 'url': 'xiaorui.cc', 'name': 'ruifengyun','level':'low' };
priv_key = RSA.importKey(priv_pem)
pub_key = RSA.importKey(pub_pem)
token = jwt.generate_jwt(payload, priv_key, 'RS256', datetime.timedelta(minutes=5))
header, claims = jwt.verify_jwt(token, pub_key, ['RS256'])
for k in payload: assert claims[k] == payload[k]