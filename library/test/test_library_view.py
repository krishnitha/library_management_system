from http import HTTPStatus
from unittest import mock
from lms.serializer.book_serializer import books, book
from lms.serializer.library_serializer import user_book_schema
from lms.serializer.user_serializer import users


@mock.patch('lms.views.library_view.redirect')
def test_get_book_list(mock_get_book_list, client, sample_book, result_book_list):
    mock_get_book_list.return_value = (result_book_list, HTTPStatus.OK)
    response = client.get('/library/books/')
    assert response.status_code == 200
    assert response.json == result_book_list


@mock.patch('lms.views.library_view.redirect')
def test_get_book_list_empty(mock_get_book_list, client):
    mock_get_book_list.return_value = (books.dump([]), HTTPStatus.NO_CONTENT)
    response = client.get('/library/books/')
    assert response.status_code == 204


@mock.patch('lms.views.library_view.redirect')
def test_get_book_detail(mock_get_book_detail, client, sample_book, result_book):
    mock_get_book_detail.return_value = (result_book, HTTPStatus.OK)
    response = client.get('library/books/1/')
    assert response.status_code == 200
    assert response.json == result_book


@mock.patch('lms.views.library_view.redirect')
def test_get_book_empty(mock_get_book_detail, client):
    mock_get_book_detail.return_value = (book.dump({}), HTTPStatus.NO_CONTENT)
    response = client.get('/library/books/1/')
    assert response.status_code == 204


@mock.patch('lms.views.library_view.redirect')
def test_add_book(mock_add_book, client, result_book):
    new_book = {"name": "python", "publisher": "raj", "author": "raj"}
    mock_add_book.return_value = (result_book, HTTPStatus.CREATED)
    response = client.post('/library/books/', json=new_book)
    assert response.status_code == 201
    assert response.json == result_book


@mock.patch('lms.views.library_view.redirect')
def test_get_user_list(mock_get_user_list, client, sample_user, result_user_list):
    mock_get_user_list.return_value = (result_user_list, HTTPStatus.OK)
    response = client.get('/library/users/')
    assert response.status_code == 200
    assert response.json == result_user_list


@mock.patch('lms.views.library_view.redirect')
def test_get_user_list_empty(mock_get_user_list, client):
    mock_get_user_list.return_value = (users.dump([]), HTTPStatus.NO_CONTENT)
    response = client.get('/library/users/')
    assert response.status_code == 204


@mock.patch('lms.views.library_view.get_user_book')
def test_get_library_user_book(mock_get_user_book, client):
    mock_get_user_book.return_value = []
    response = client.get('/library/users/raj/')
    assert response.status_code == 400


@mock.patch('lms.views.library_view.get_book_info')
@mock.patch('lms.views.library_view.get_user_info')
@mock.patch('lms.views.library_view.get_user_book')
def test_get_library_user_book_1(mock_get_user_book, mock_user_info, mock_book_info,
                                 client, sample_library, sample_user, sample_book):
    user_book = {'author': 'raj', 'id': None, 'name': 'python', 'publisher': 'raj'}
    user_book_association = {'books': [user_book], 'email': 'raj@gmail.com',
                             'name': 'raj', 'username': 'raj'}
    mock_get_user_book.return_value = [sample_library]
    mock_user_info.return_value = sample_user
    mock_book_info.return_value = sample_book
    response = client.get('/library/users/raj/')
    assert response.status_code == 200
    assert response.json == user_book_schema.dump(user_book_association)


@mock.patch('lms.views.library_view.redirect')
def test_add_user(mock_add_book, client, result_user):
    new_user = {"email": "raj@gmail.com", "name": "raj", "username": "raj"}
    mock_add_book.return_value = (result_user, HTTPStatus.CREATED)
    response = client.post('/library/users/', json=new_user)
    assert response.status_code == 201
    assert response.json == result_user


@mock.patch('lms.views.library_view.redirect')
def test_add_user_exist(mock_add_book, client, result_user):
    new_user = {"email": "raj@gmail.com", "name": "raj", "username": "raj"}
    mock_add_book.return_value = (result_user, HTTPStatus.BAD_REQUEST)
    response = client.post('/library/users/', json=new_user)
    assert response.status_code == 400
    assert response.json == result_user


@mock.patch('lms.views.library_view.add_user_book')
@mock.patch('lms.views.library_view.get_book_info')
@mock.patch('lms.views.library_view.get_user_info')
def test_libray_issue_no_user(mock_user_info, mock_book_info, mock_add_user_book, client,
                              sample_user, sample_book, sample_library, result_library):
    mock_user_info.return_value = sample_user
    mock_book_info.return_value = sample_book
    response = client.post('/library/users/raj/books/1/')
    assert response.status_code == 201
    assert response.json == result_library


@mock.patch('lms.views.library_view.get_book_info')
@mock.patch('lms.views.library_view.get_user_info')
def test_libray_issue_no_user(mock_user_info, mock_book_info, client, sample_book):
    mock_user_info.return_value = None
    mock_book_info.return_value = sample_book
    response = client.post('/library/users/raj/books/1/')
    assert response.status_code == 400


@mock.patch('lms.views.library_view.get_book_info')
@mock.patch('lms.views.library_view.get_user_info')
def test_libray_issue_no_book(mock_user_info, mock_book_info, client, sample_user):
    mock_user_info.return_value = sample_user
    mock_book_info.return_value = None
    response = client.post('/library/users/raj/books/1/')
    assert response.status_code == 400


@mock.patch('lms.views.library_view.add_user_book')
@mock.patch('lms.views.library_view.get_book_info')
@mock.patch('lms.views.library_view.get_user_info')
def test_libray_issue(mock_user_info, mock_book_info, mock_add_user_book, client,
                      sample_user, sample_book, sample_library, result_library):
    mock_user_info.return_value = sample_user
    mock_book_info.return_value = sample_book
    response = client.post('/library/users/raj/books/1/')
    assert response.status_code == 201
    assert response.json == result_library
