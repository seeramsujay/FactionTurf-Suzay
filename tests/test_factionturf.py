import json
from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parent.parent

def test_package_json():
    pkg = REPO_ROOT / "package.json"
    assert pkg.exists()
    data = json.loads(pkg.read_text())
    assert data["name"] == "factionturf"
    assert "express" in data["dependencies"]
    assert "@prisma/client" in data["dependencies"]
    assert "typescript" in data["devDependencies"]

def test_routes_source():
    routes_file = REPO_ROOT / "src" / "routes" / "index.ts"
    assert routes_file.exists()
    content = routes_file.read_text()
    assert "/getInfo" in content
    assert "/postInfo" in content
    assert "/getMPRs" in content
    assert "stackType" in content

def test_server_entrypoint():
    index_file = REPO_ROOT / "src" / "index.ts"
    assert index_file.exists()
    content = index_file.read_text()
    assert "express" in content
    assert "/api" in content
