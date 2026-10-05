#!/usr/bin/env python3
"""Return packaged routing context without inspecting the session or library."""

import json
from pathlib import Path


def main() -> None:
    context = Path(__file__).with_name("context.md").read_text(encoding="utf-8")
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
