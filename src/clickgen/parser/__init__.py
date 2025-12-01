#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List, Optional, Tuple, Type, Union
from pathlib import Path

from clickgen.parser.base import BaseParser
from clickgen.parser.png import MultiPNGParser, SinglePNGParser

__all__ = ["SinglePNGParser", "MultiPNGParser", "open_blob"]

PARSERS: List[Type[BaseParser]] = [SinglePNGParser, MultiPNGParser]


def open_blob(
    blob: Union[bytes, List[bytes]],
    hotspot: Tuple[int, int],
    sizes: Optional[List[int]] = None,
    delay: Optional[int] = None,
    resized_blobs: Optional[Dict[int, Union[bytes, List[bytes]]]] = None,
) -> BaseParser:
    for parser in PARSERS:
        if parser.can_parse(blob):
            return parser(blob, hotspot, sizes, delay, resized_blobs)  # type: ignore
    raise ValueError("Unsupported file format")
