#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

from pathlib import Path
from typing import Any


def get_project_root() -> Path:
    """Get the project root path"""
    return Path(__file__).parent.parent


def get_cwd() -> str:
    """Get current working directory"""
    return os.getcwd()


def search_tools() -> str:
    """Search available tools in directory"""
    dir_path = os.path.join(get_project_root(), "tools")
    tools_available = os.listdir(dir_path)
    for item in tools_available:
        if not item.startswith("_"):
            return os.path.splitext(item)[0]


def copy_files(prefix_path: str, dest: str) -> Any:
    """Copy referenced files to current working dir"""
    shutil.copy(prefix_path, dest)


def prepend_path(base_name: str, resource_path: str) -> str:
    """Prefix VCFanno referenced file"""
    return os.path.join(resource_path, base_name)
