from doctest import BLANKLINE_MARKER
import os
from time import sleep
from rich.console import Console
banner = """

                                                                                                                                                                                      
                               &@@@@@@@@@@@@@, /@@@@@@@@@@@@@@#   *@@@@@@@@@@@#    /@@@@@@@@@@@@@@  &@@@/      *@@@@@. /@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@   @@@@@@@@@@@@@@                                
                            .@@@@@@@@@@@@@@#  &@@@@@@@@@@@@@&  %@@@@@@@@@@@@@@@  &@@@@@@@@@@@@@@  (@@@@.   *@@@@@/   &@@@@@@@@@@@@@@. (@@@@@@@@@@@@@@, ,@@@@@@@@@@@@@@(                                 
                           &@@@@#//////.         .@@@@*      .@@@@*      @@@@& .@@@@/            @@@@@//@@@@@@.    .@@@@@//////*     @@@@@////////    &@@@@                                             
                           @@@@@@@@@@@@@       @@@@@       @@@@@      *@@@@. %@@@@            /@@@@@@@@@@@       &@@@@@@@@@@@@@  /@@@@@@@@@@@@@   .@@@@*                                              
                                  .@@@@/      .@@@@/      .@@@@*     .@@@@@  @@@@<            @@@@&    @@@@&               &@@@@  @@@@@            @@@@@                                                
                       @@@@@@@@@@@@@@@       &@@@@       .@@@@@@@@@@@@@@%   @@@@@@@@@@@@@@/ /@@@@      /@@@@   %@@@@@@@@@@@@@@*  @@@@@@@@@@@@@@%  @@@@@@@@@@@@@@@                                       
                                                                                                                                                                           
                                                                       🤲  Black men will always be watching :) 🤲       
                                                                       Check out my github page 🤲 :  https://github.com/Pheanoukma 


"""
print(banner)
console = Console()
tasks = [f"task {n}" for n in range(1, 5)]

with console.status("[bold green]Working on the files...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
print("File loading and initializing....") 
os.system('python WinFetch.py')