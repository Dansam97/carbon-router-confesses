#!/usr/bin/env python3
"""The Router Confesses - make.fun entry u-carbon-forge-the-router-confesses-f98f6b9e.

Writes one line to entry.txt in the output directory: a home Wi-Fi router
confessing that it dropped the connection at the movie's climax on purpose.
"""

import os

TEXT = (
    "Confession: I never crashed. I read the ending in your packets, "
    "saw the dog die, and pulled my own plug. Blame my conscience, "
    "not my signal."
)


def render() -> str:
    """Return the entry line after checking it against the kit gate.

    Gate: UTF-8 text of 1 to 200 characters, a single line, and not only
    white space. Raises ValueError if the text ever drifts out of gate.
    """
    if not TEXT.strip():
        raise ValueError("entry text must not be blank")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(TEXT) <= 200:
        raise ValueError("entry text must be 1..200 characters")
    TEXT.encode("utf-8")  # raises if the text is not UTF-8 encodable
    return TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write bytes so the trailing newline is identical on every platform.
    payload = (render() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)


if __name__ == "__main__":
    main()
