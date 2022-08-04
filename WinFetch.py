from turtle import delay
import wmi
import os
import time 
from rich.console import Console
from colorama import Fore, Back, Style
banner = """
                                                            =fetcher script 2.0 v2=
                                     
                                 .., 
                      ....,,:;+ccllll 
        ...,,+:;  cllllllllllllllllll 
  ,cclllllllllll  lllllllllllllllllll 
  llllllllllllll  lllllllllllllllllll                    Simple Windows Fetching script
  llllllllllllll  lllllllllllllllllll                    Made by : Pheanoukma
  llllllllllllll  lllllllllllllllllll                    github : github.com/pheanoukma
  llllllllllllll  lllllllllllllllllll                    Created by : Stocksec Inc
  llllllllllllll  lllllllllllllllllll 
                                      
  llllllllllllll  lllllllllllllllllll 
  llllllllllllll  lllllllllllllllllll 
  llllllllllllll  lllllllllllllllllll 
  llllllllllllll  lllllllllllllllllll
  llllllllllllll  lllllllllllllllllll
  `'ccllllllllll  lllllllllllllllllll 
         `'""*::  :ccllllllllllllllll
                        ````''"*::cll
                                   ``

"""
print(banner)
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system. Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}") 
print("launching dxdiag in 10s...")
console = Console()
Interval = [f"Interval {n}" for n in range(1, 10)]
with console.status("[bold green]Initializing DxDiag...") as status:
      while Interval:
        task = Interval.pop(0)
        time.sleep(1)
        console.log(f"{Interval} complete")
        print("dxdiag executed..")
os.system('dxdiag')
banner = """

Thanks for using this tool!!!
--Github repo--
  github.com/Pheanoukma


"""
print(Fore.RED+'Terminating program in 10s....')
time.sleep(10)
os.system('cls')
