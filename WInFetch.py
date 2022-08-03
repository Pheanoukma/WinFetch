import wmi

banner = """


                                 .., 
                      ....,,:;+ccllll 
        ...,,+:;  cllllllllllllllllll 
  ,cclllllllllll  lllllllllllllllllll 
  llllllllllllll  lllllllllllllllllll                    Simple Windows Fetching script
  llllllllllllll  lllllllllllllllllll                    Made by : Pheanoukma
  llllllllllllll  lllllllllllllllllll                    github : github.com/pheanoukma
  llllllllllllll  lllllllllllllllllll 
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
