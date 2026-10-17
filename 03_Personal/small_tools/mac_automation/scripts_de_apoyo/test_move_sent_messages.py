import argparse
import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).with_name("move_sent_messages.py")
spec = importlib.util.spec_from_file_location("move_sent_messages", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_normalize_folder_path_removes_extra_separators():
    assert module.normalize_folder_path(" //Enviado///Subcarpeta/ ") == "Enviado/Subcarpeta"


def test_validate_move_request_rejects_same_source_and_destination():
    parser = argparse.ArgumentParser()
    args = argparse.Namespace(
        account="Mi cuenta",
        source="Enviado",
        dest="Enviado",
        all=False,
        older_than_days=None,
        subject_contains=None,
    )

    with pytest.raises(SystemExit):
        module.validate_move_request(args, parser)


def test_validate_move_request_requires_at_least_one_filter():
    parser = argparse.ArgumentParser()
    args = argparse.Namespace(
        account="Mi cuenta",
        source="Enviado",
        dest="Archivados",
        all=False,
        older_than_days=None,
        subject_contains=None,
    )

    with pytest.raises(SystemExit):
        module.validate_move_request(args, parser)
