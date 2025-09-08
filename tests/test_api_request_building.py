import pytest

from streetmanager.work.swagger_client.api.default_api import DefaultApi as WorkApi
from streetmanager.lookup.swagger_client.api.default_api import DefaultApi as LookupApi


def test_work_calculate_duration_builds_query_and_headers(monkeypatch):
    api = WorkApi()
    captured = {}

    def fake_call_api(resource_path, method, path_params, query_params, header_params, **kwargs):
        captured.update(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            kwargs=kwargs,
        )
        return None

    monkeypatch.setattr(api.api_client, "call_api", fake_call_api)

    api.calculate_duration(start_date="2024-01-01", end_date="2024-01-31")

    assert captured["resource_path"] == "/duration"
    assert captured["method"] == "GET"
    # Accept header should be set to JSON
    assert captured["header_params"].get("Accept") == "application/json"
    # Query params should include start and end dates
    assert ("startDate", "2024-01-01") in captured["query_params"]
    assert ("endDate", "2024-01-31") in captured["query_params"]


def test_work_add_file_to_work_path_and_content_type(monkeypatch):
    api = WorkApi()
    captured = {}

    def fake_call_api(resource_path, method, path_params, query_params, header_params, body=None, **kwargs):
        captured.update(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            kwargs=kwargs,
        )
        return None

    monkeypatch.setattr(api.api_client, "call_api", fake_call_api)

    body = {"name": "file.json", "data": "{}"}
    api.add_file_to_work(body=body, work_reference_number="WRN123")

    assert captured["resource_path"] == "/works/{workReferenceNumber}/files"
    assert captured["method"] == "POST"
    # Placeholder path param and value should be prepared
    assert captured["path_params"]["workReferenceNumber"] == "WRN123"
    # Content-Type header should be set for JSON body
    assert captured["header_params"].get("Content-Type") == "application/json"
    assert captured["body"] == body


def test_lookup_get_streets_by_query_builds_query(monkeypatch):
    api = LookupApi()
    captured = {}

    def fake_call_api(resource_path, method, path_params, query_params, header_params, **kwargs):
        captured.update(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            kwargs=kwargs,
        )
        return []

    monkeypatch.setattr(api.api_client, "call_api", fake_call_api)

    api.get_streets_by_query("Main Street")

    assert captured["resource_path"] == "/nsg/search"
    assert captured["method"] == "GET"
    assert ("query", "Main Street") in captured["query_params"]
    assert captured["header_params"].get("Accept") == "application/json"


def test_missing_required_parameters_raise_errors():
    work_api = WorkApi()
    lookup_api = LookupApi()

    with pytest.raises(ValueError):
        # body is required
        work_api.add_file_to_work(body=None, work_reference_number="WRN")

    with pytest.raises(ValueError):
        # required query string
        lookup_api.get_streets_by_query(None)

