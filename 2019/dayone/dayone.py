import math

masses = open('input.txt', 'r').read().split("\n")

def calculate_fuel_for_module(mass):
    return (math.floor(mass/3) - 2)

def calculate_fuel_for_fuel(total_fuel, remaning_mass):

    remaning_mass = calculate_fuel_for_module(remaning_mass)
    
    if remaning_mass <= 0:
        return total_fuel

    total_fuel += remaning_mass

    return calculate_fuel_for_fuel(total_fuel, remaning_mass)
    

def part_one():
    total_fuel = 0
    for mass in masses:
        
        total_fuel += calculate_fuel_for_module(int(mass))
    
    print(total_fuel)

def part_two():
    total_fuel_for_fuel = 0
    for mass in masses:
        total_fuel_for_fuel += calculate_fuel_for_fuel(0, int(mass))

    print(total_fuel_for_fuel)

part_two()