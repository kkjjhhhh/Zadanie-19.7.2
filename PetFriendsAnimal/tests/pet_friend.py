from api.apily import PetFriends
from set.settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_api_key_for_fasle_user(email=false_email, password=valid_password):
    status = pf.get_api_key(email, password)
    assert status == 400

def test_get_api_key_for_false_user(email=valid_email, password=false_password):
    status = pf.get_api_key(email, password)
    assert status == 400

def test_get_all_pets_with_fasle_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key:10, filter)
    assert status == 403

def test_get_all_pets_with_false_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key:GIT, filter)
    assert status == 403

