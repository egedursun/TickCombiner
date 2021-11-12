#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:57:08 2021

@author: Ege Dogan Dursun
Phone: +90(507)0558665
EMail: esa.ege@gmail.com

"Fin Challenge"

Thanks for your time and consideration.

BR,
"""

import string
import random as r
import data_model as dm
from datetime import datetime as dt
import copy

#Update the prices and assume a slightly expanding market environment
def update_prices(prices):
    for key, value in prices.items():
        #Assume a slight bull market :))
        prices[key] += r.randint(-2, 3)
    return prices

#Tick generator
def tick_generator(n_instruments=10):
    
    #Generate dummy instruments and initial prices
    prices = {}
    for i in range(0, n_instruments):
        #Initialize random instrument names
        random_name = "".join(r.choices(string.ascii_uppercase + string.digits, k = 4))  
        
        #Initialize random starting prices
        random_starting_price = r.randint(100, 500)
        
        #Assign the instrument name and price to the map
        prices[random_name] = random_starting_price
    
    #Get current time
    cur_time = dt.now()
    
    #Instantiate the initial tick
    cur_tick = dm.Tick(cur_time, prices)
    new_tick = copy.deepcopy(cur_tick)
    
    #Handle the yield to satisfy the generator purpose
    while True:
        #Update datetime to current datetime to generate the new Tick
        cur_time = dt.now()
        #Update the prices to update the new Tick
        prices = update_prices(prices)
    
        #Generate the new tick
        yield new_tick 
        
        #Copy the instantiated tick as frozen classes are immutable / needed to instantiate new Ticks
        new_tick = dm.Tick(cur_time, prices)
        new_tick = copy.deepcopy(new_tick)
        

#Tick generator for multiple exchanges with different instruments and different prices
def exchanges_concatenator(n_exchanges, n_instruments=None):
    
    #Define ticks that will store the exchange informations as well as the generators regarding those exchanges
    ticks = {}
    
    #If amount of randomized instruments per exchange is given, create constant amount of instruments, otherwise select between 3
     #to 10 instruments per exchange.
    randomized_n_instruments = False
    if n_instruments == None:
        randomized_n_instruments = True
    
    #Create the generators for the exchanges
    for i in range(0, n_exchanges):
        #Assign random exchange names
        random_exch_name = "".join(r.choices(string.ascii_uppercase + string.digits, k = 8))  
        
        #If randomized, create instruments per exchange accordingly.
        if randomized_n_instruments:
            n_instruments = r.randint(3, 10)
            
        #Instantiate the generators and add the resulting generator to the ticks
         #with its randomly generated exchange name
        new_gen = tick_generator(n_instruments)
        ticks[random_exch_name] = new_gen
    
    #Return the ticks mapping
    return ticks