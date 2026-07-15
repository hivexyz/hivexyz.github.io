#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path


def usage() -> None:
    print(
        "Usage:\n"
        "  python scripts/create_post_dirs.py <post-slug>\n\n"
        "Example:\n"
        "  python scripts/create_post_dirs.py 2026q3/test_img\n\n"
        "This will create:\n"
        "  - content/posts/2026q3/test_img  (Page Bundle directory)\n"
        "  Place images alongside index.md inside this directory."
    )


def normalize_slug(raw: str) -> str:
    slug = raw.strip().strip("/\\")
    slug = slug.replace("\\", "/")

    if not slug or slug.startswith("/") or ".." in slug.split("/"):
        raise ValueError(f"Invalid post slug: {raw}")

    if "/" not in slug:
        raise ValueError(
            "Post slug should include at least one directory level, "
            "for example: 2026q3/test_img"
        )

    return slug


def main() -> int:
    if len(sys.argv) != 2:
        usage()
        return 1

    try:
        slug = normalize_slug(sys.argv[1])
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    page_bundle_dir = Path("content/posts") / slug

    page_bundle_dir.mkdir(parents=True, exist_ok=True)

    print("Created Page Bundle directory:")
    print(f"  {page_bundle_dir.as_posix()}")
    print(f"\nNext steps:")
    print(f"  1. Create {page_bundle_dir.as_posix()}/index.md")
    print(f"  2. Place images directly in {page_bundle_dir.as_posix()}/")
    print(f"  3. Reference images in markdown as: ![alt](image.png)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
