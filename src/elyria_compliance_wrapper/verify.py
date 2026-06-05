from .crypto import sha256_json


def check_packet(packet):
    stored = packet.get("packet_hash")
    if stored is None:
        return False
    copy = dict(packet)
    copy.pop("packet_hash", None)
    return sha256_json(copy) == stored
