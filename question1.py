from __future__ import annotations

import re


def is_valid_contact_number(number: str) -> bool:
    pattern = r"^(\+?(\d{1,2}))?[-.\s]?(\()?(\d{3})(?(3)\))?[-.\s]?(\d{3})[-.\s]?(\d{4})$"  # noqa: E501
    return re.match(pattern, number) is not None
