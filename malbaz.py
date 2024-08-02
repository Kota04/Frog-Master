from malwarebazaar import Bazaar
import pprint
bazaar = Bazaar("94c71513ba8373d70882b2d7c14fa8b4")
hash = input("Enter the hash value: ")
responce = bazaar.query_hash(hash)
pprint.pp(responce)
