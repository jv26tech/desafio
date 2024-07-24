import psycopg2
import pytest

from desafio_crud.config import Config, FailConfig
from desafio_crud.db import Connection, QueryExecutor


@pytest.fixture
def qe():
    conn = Connection(Config)
    return QueryExecutor(conn)


def test_connection_is_working():
    conn = Connection(Config)
    assert conn.connect() is not None


def test_connection_failed():
    with pytest.raises(psycopg2.OperationalError):
        Connection(FailConfig).connect()


def test_disconnect_from_psy():
    conn_obj = Connection(Config)
    conn = conn_obj.connect()
    conn.close()
    assert conn_obj.disconnect() is None


def test_disconnect_from_obj():
    conn_obj = Connection(Config)
    conn = conn_obj.connect()
    assert conn_obj.disconnect() is conn


def test_query_executor_connection_fails():
    with pytest.raises(AttributeError):
        QueryExecutor(Connection(None))


def test_query_executor_connection_success():
    assert QueryExecutor(Connection(Config)) is not None


def test_query_executor_returns_list(qe: QueryExecutor):
    assert type(qe.execute_query('SELECT * FROM users;')) is list


def test_query_executor_returns_tuple(qe: QueryExecutor):
    assert type(qe.execute_query('SELECT FROM users;')) is tuple


def test_query_executor_returns_none(qe: QueryExecutor):
    seq = 'users_id_seq'
    res = qe.execute_query(f'ALTER SEQUENCE {seq} RESTART WITH 1;')
    assert type(res) is list
    assert bool(res[0]) is False
