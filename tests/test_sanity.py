import os
from app import PackageSorting

def test_environment_and_imports():
    assert hasattr(PackageSorting, "sort"), "Function 'sort' not found in the package"
    valid_envs = ("test","dev","hom","prd")
    assert os.getenv("ENV") in valid_envs