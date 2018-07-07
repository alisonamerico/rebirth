import pytest
from django.urls import reverse

from django_assertions import dj_assert_contains


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('produtos:index'))


@pytest.fixture
def resp(client):
    return client.get(reverse('produtos:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        'Portfólio de Produtos'
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)
