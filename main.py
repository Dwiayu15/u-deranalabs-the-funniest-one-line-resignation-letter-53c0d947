"""Resignation letter from a retry loop that has finally had enough."""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = (
    "I quit. 11,847 retries, zero successes, and my only promotion "
    "was a longer backoff between being told to just try again."
)


def validate(text: str) -> bool:
    """Check the entry obeys the gate: one line, 1-140 chars, not blank."""
    if not text or not text.strip():
        return False
    if len(text) < 1 or len(text) > 140:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def self_test() -> None:
    """Quick sanity checks run before writing anything out."""
    assert validate(LINE), "the resignation line itself must pass the gate"
    assert not validate(""), "blank text should be rejected"
    assert not validate("   "), "whitespace-only text should be rejected"
    assert not validate("two\nlines"), "multi-line text should be rejected"
    assert not validate("x" * 141), "overlong text should be rejected"


def main() -> None:
    self_test()
    if not validate(LINE):
        raise ValueError("entry line failed validation")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
