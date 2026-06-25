import pytest

import civicaccess.main as main_module


@pytest.fixture(autouse=True)
def isolated_default_data_dir(monkeypatch, tmp_path):
    monkeypatch.setenv("CIVICACCESS_DATA_DIR", str(tmp_path / "civicaccess-data"))
    yield
    main_module._dispose_review_repository()
    main_module._review_db_url = None
