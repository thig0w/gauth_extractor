import base64
from loguru import logger
import protobuff.gauth_pb2 as pb
#
# def get_payload_from_otp_url(otp_url: str, i: int, source: str) -> Optional[pb.MigrationPayload]:
#     '''Extracts the otp migration payload from an otp url. This function is the core of the this appliation.'''
#     if not is_opt_url(otp_url, source):
#         return None
#     parsed_url = urlparse.urlparse(otp_url)
#     if verbose >= LogLevel.DEBUG: log_debug(f"parsed_url={parsed_url}")
#     try:
#         params = urlparse.parse_qs(parsed_url.query, strict_parsing=True)
#     except Exception:  # workaround for PYTHON <= 3.10
#         params = {}
#     if verbose >= LogLevel.DEBUG: log_debug(f"querystring params={params}")
#     if 'data' not in params:
#         log_error(f"could not parse query parameter in input url\nsource: {source}\nurl: {otp_url}")
#         return None
#     data_base64 = params['data'][0]
#     if verbose >= LogLevel.DEBUG: log_debug(f"data_base64={data_base64}")
#     data_base64_fixed = data_base64.replace(' ', '+')
#     if verbose >= LogLevel.DEBUG: log_debug(f"data_base64_fixed={data_base64_fixed}")
#     data = base64.b64decode(data_base64_fixed, validate=True)
#     payload = pb.MigrationPayload()
#     try:
#         payload.ParseFromString(data)
#     except Exception as e:
#         abort(f"Cannot decode otpauth-migration migration payload.\n"
#               f"data={data_base64}", e)
#     if verbose >= LogLevel.DEBUG: log_debug(f"\n{i}. Payload Line", payload, sep='\n')
#
#     return payload

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

