import pytest

from django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'COK Store',
        'Contato',
        'Copyright',
        'href="/contato/"',
    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)


def test_contact_status_code(client):
    response = client.get('/contato/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Rua Jataúba 161',
        'Recife, PE',
        '(81) 9 8888-8888',
        'name@example.com',
        'Segunda - Sexta: 9:00 às 17:00',
    ]
)
def test_contact_content(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
