from json import dumps

def image_to_json(img):
    object_to_json = {
        "name": "EndFTs ERC-721 Smart Contract",
        "description": "EndFTs ERC-721 Smart Contract",
        "image": img,
        "attributes": [
          {
            "trait_type": "Developer",
            "value": "UCLA"
          },
          {
            "trait_type": "Website",
            "value": "https://twitter.com/EndFTs"
          }
        ]
    }

    return dumps(object_to_json)