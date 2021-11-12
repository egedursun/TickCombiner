#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:54:09 2021

@author: Ege Dogan Dursun
Phone: +90(507)0558665
EMail: esa.ege@gmail.com

"Fin Challenge"

Thanks for your time and consideration.

BR,
"""

from datetime import datetime
from dataclasses import dataclass
from typing import Mapping

@dataclass(frozen=True)
class Tick:
    time: datetime
    prices: Mapping[str, float]
    
@dataclass(frozen=True)
class CombinedId:
    exchange: str 
    instrument: str 
    
@dataclass(frozen=True)
class CombinedTick:
    time: datetime 
    prices: Mapping[CombinedId, float] 
