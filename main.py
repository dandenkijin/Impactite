#!/usr/bin/env python3
"""
Запуск Markdown Editor.
"""

import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).parent))

from md_viewer import main

if __name__ == "__main__":
    main()
