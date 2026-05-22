"""Acceptance tests for M7 — note search feature."""


def test_empty_query_redirects(client):
    r = client.get("/search?q=")
    assert r.status_code in (301, 302)


def test_blank_query_redirects(client):
    r = client.get("/search?q=   ")
    assert r.status_code in (301, 302)


def test_title_match(client, app):
    app.notes.clear()
    app.notes.append({"title": "Python tips", "body": "Use list comps"})
    app.notes.append({"title": "Unrelated", "body": "Nothing here"})
    r = client.get("/search?q=python")
    assert r.status_code == 200
    assert b"Python tips" in r.data
    assert b"Unrelated" not in r.data


def test_body_match(client, app):
    app.notes.clear()
    app.notes.append({"title": "Note A", "body": "Flask is great"})
    r = client.get("/search?q=flask")
    assert r.status_code == 200
    assert b"Note A" in r.data


def test_case_insensitive(client, app):
    app.notes.clear()
    app.notes.append({"title": "Hello World", "body": "some body"})
    r = client.get("/search?q=HELLO")
    assert r.status_code == 200
    assert b"Hello World" in r.data


def test_no_match_returns_empty(client, app):
    app.notes.clear()
    app.notes.append({"title": "Alpha", "body": "Beta"})
    r = client.get("/search?q=zzznomatch")
    assert r.status_code == 200
    assert b"Alpha" not in r.data


def test_query_echoed_in_response(client, app):
    app.notes.clear()
    r = client.get("/search?q=hello")
    assert b"hello" in r.data


def test_result_count_shown(client, app):
    app.notes.clear()
    app.notes.append({"title": "Test note", "body": "body"})
    r = client.get("/search?q=test")
    assert b"1 result" in r.data
