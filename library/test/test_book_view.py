from unittest import mock


@mock.patch('lms.views.book_view.get_all_book')
def test_get_book_list(mock_get_book_list, client, sample_book, result_book_list):
    mock_get_book_list.return_value = [sample_book]
    response = client.get('/books/')
    assert response.status_code == 200
    assert response.json == result_book_list


@mock.patch('lms.views.book_view.get_all_book')
def test_get_book_list_empty(mock_get_book_list, client):
    mock_get_book_list.return_value = []
    response = client.get('/books/')
    assert response.status_code == 204


@mock.patch('lms.views.book_view.get_book_info')
def test_get_book_detail(mock_get_book_detail, client, sample_book, result_book):
    mock_get_book_detail.return_value = sample_book
    response = client.get('/books/1/')
    assert response.status_code == 200
    assert response.json == result_book


@mock.patch('lms.views.book_view.add_book')
def test_add_book(mock_add_user, client, result_book):
    new_book = {"name": "python", "publisher": "raj", "author": "raj"}
    response = client.post('/books/', json=new_book)
    mock_add_user.assert_called_once()
    assert response.status_code == 201
    assert response.json == result_book


@mock.patch('lms.views.book_view.get_book_info')
def test_get_book_empty(mock_get_book_detail, client):
    mock_get_book_detail.return_value = None
    response = client.get('/books/1/')
    assert response.status_code == 204
