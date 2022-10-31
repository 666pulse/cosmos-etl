import json
from cosmosetl.domain.event import CosmEvent
from cosmosetl.utils import b64decode

class CosmEventMapper:
    def json_dict_to_event(self, json_dict, tx_hash=None, height=None):
        event = CosmEvent()

        event.event_type = json_dict.get("type")

        _keys = []
        _values = []

        for attr in json_dict.get("attributes", []):
            _key = b64decode(attr.get('key', ''))
            _value = b64decode(attr.get('value', ''))

            _keys.append(_key)
            _values.append(_value)

        event.tx_hash = tx_hash
        event.height = height

        if len(_keys) > 0:
            event.keys = "-".join(_keys)
            event.values = "-".join(_values)
        else:
            event.keys = ""
            event.values = ""

        return event

    def event_to_dict(self, event):
        return {
            "type": "event",
            "event_type": event.event_type,
            "height": event.height,
            "tx_hash": event.tx_hash,
            "keys": event.keys,
            "values": event.values,
        }
