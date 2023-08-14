import base64
from loguru import logger
import protobuff.gauth_pb2 as pb

def extract_from_url(url):
    logger.debug(f"Extracting from {url}")
    data = base64.b64decode(url, validate=True)
    logger.debug(f"base 64 decoded: {data}")
    message = pb.MigrationPayload()
    logger.debug(f"Parsing from data")
    message.ParseFromString(data)
    logger.debug(f"extracted {message.otp_parameters}")
    secret = str(base64.b32encode(message.otp_parameters[0].secret), 'utf-8')
    logger.debug(f"base32 secret: {secret}")



if __name__ == "__main__":
    logger.debug(f"Starting Job")

