from unittest import mock


@mock.patch('lms.views.user_view.get_all_user')
def test_get_user_list(mock_get_user_list, client, sample_user, result_user):
    mock_get_user_list.return_value = [sample_user]
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json[0] == result_user


@mock.patch('lms.views.user_view.get_all_user')
def test_get_user_list_empty(mock_get_user_list, client):
    mock_get_user_list.return_value = []
    response = client.get('/users/')
    assert response.status_code == 204


@mock.patch('lms.views.user_view.get_user_info')
def test_get_user_detail(mock_get_user, client, sample_user, result_user):
    mock_get_user.return_value = sample_user
    response = client.get('/users/raj/')
    assert response.status_code == 200
    assert  response.json == result_user


@mock.patch('lms.views.user_view.get_user_info')
def test_get_user_empty(mock_get_user_info, client):
    mock_get_user_info.return_value = None
    response = client.get('/users/raj/')
    assert response.status_code == 204


@mock.patch('lms.views.user_view.get_user_info')
@mock.patch('lms.views.user_view.add_user')
def test_add_user(mock_add_user, mock_get_user_list, client, result_user):
    new_user = {"email": "raj@gmail.com", "name": "raj", "username": "raj"}
    mock_get_user_list.return_value = None
    response = client.post('/users/', json=new_user)
    mock_add_user.assert_called_once()
    assert response.status_code == 201
    assert response.json == result_user


@mock.patch('lms.views.user_view.get_user_info')
def test_add_user_existing(mock_get_user_list, client, sample_user):
    new_user = {"email": "raj@gmail.com", "name": "raj", "username": "raj"}
    mock_get_user_list.return_value = sample_user
    response = client.post('/users/', json=new_user)
    assert response.status_code == 400
