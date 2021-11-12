#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:55:51 2021

@author: Ege Dogan Dursun
Phone: +90(507)0558665
EMail: esa.ege@gmail.com

"Fin Challenge"

Thanks for your time and consideration.

BR,
"""

import tick_generator
import combined_generator

#Hyper-parameters for generators
N_EXAMPLE_TICKS = 10
N_INSTRUMENTS = 10
N_EXCHANGES = 5

#Test the functionality of the tick generator
def test_tick_generator(n_instruments=N_INSTRUMENTS, 
                        n_amount_generations=N_EXAMPLE_TICKS):
    tick_gen = tick_generator.tick_generator(n_instruments)
    for i in range(0, n_amount_generations):
        print("Generation ", (i+1))
        print(next(tick_gen), end="\n\n")
    print("____________")
        
#Test the functionality of the method to concatenate the different exchanges / randomized instrument amounts version
def test_exchanges_concatenator_randomized_instruments(n_exchanges=N_EXCHANGES):
    ticks = tick_generator.exchanges_concatenator(n_exchanges)
    for exchange_name, generator in ticks.items():
        print("Exchange Name: ", exchange_name)
        print("Generator: ", generator)
        print("Generate a Tick: ")
        print(next(generator), end="\n\n")
    print("____________")
  
#Test the functionality of the method to concatenate the different exchanges / non-randomized instrument amounts version
def test_exchanges_concatenator_non_randomized_instruments(n_exchanges=N_EXCHANGES, 
                                                    n_instruments=N_INSTRUMENTS):
    ticks = tick_generator.exchanges_concatenator(n_exchanges, n_instruments)
    for exchange_name, generator in ticks.items():
        print("Exchange Name: ", exchange_name)
        print("Generator: ", generator)
        print("Generate a Tick: ")
        print(next(generator), end="\n\n")
    print("____________")
    
#MAIN REQUIREMENT : TEST THE FUNCTIONALITY OF THE COMBINED TICK GENERATOR METHOD
def test_combined_generator(ticks=tick_generator.exchanges_concatenator(N_EXCHANGES, N_INSTRUMENTS)):
    gen = next(combined_generator.combine(ticks))
    print(gen)
    print("____________")
    

#Call the methods from the main
if __name__ == '__main__':
    test_tick_generator()
    test_exchanges_concatenator_randomized_instruments()
    test_exchanges_concatenator_non_randomized_instruments()
    test_combined_generator()
