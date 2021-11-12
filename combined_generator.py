#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:46:57 2021

@author: Ege Dogan Dursun
Phone: +90(507)0558665
EMail: esa.ege@gmail.com

"Fin Challenge"

Thanks for your time and consideration.

BR,
"""

from datetime import datetime
from typing import Mapping
from typing import Generator
import data_model

#The project asked for the development of this method. This method generates combined ticks accordingly
def combine(ticks: Mapping[str, Generator[data_model.Tick, None, None]]) -> Generator[data_model.CombinedTick, None, None]:
    
    while True:
        #Instantiate a mapping for the results
        prices = {}
        #Traverse the input Ticks
        for exchange_name, generator in ticks.items():
            #Take the exchange name
            comb_exchange_name = exchange_name
            #Use the generators to get the next price data
            cur_generation = next(generator)
            #For each instrument take the price
            for instrument_name, price in cur_generation.prices.items():
                #Take the instrument name and price
                comb_instrument_name = instrument_name
                comb_price = price
                
                #create the combined ID
                combined_id = data_model.CombinedId(comb_exchange_name, comb_instrument_name)
                
                #Assign the information to the prices
                prices[combined_id] = comb_price
        
        #Take the datetime for combined tick
        cur_datetime = datetime.now()
        
        #Instantiate the combined Tick
        comb_generator = data_model.CombinedTick(cur_datetime, prices)
        
        #Yield the resulting CombinedTick
        yield comb_generator