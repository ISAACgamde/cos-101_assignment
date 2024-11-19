import math
from email.headerregistry import Group
from typing import Generator

# Constants
g = 9.81  # Acceleration due to gravity in m/s^2


# Function to calculate maximum height of a projectile
def calculate_max_height(initial_velocity):
    return (initial_velocity ** 2) / (2 * g)


# Function to calculate range of a projectile
def calculate_range(initial_velocity, angle_of_launch):
    angle_in_radians = math.radians(angle_of_launch)
    return (initial_velocity ** 2) * math.sin(2 * angle_in_radians) / g


# Function to calculate gravitational force between two masses
def calculate_gravitational_force(m1, m2, distance):
    G = 6.67430 * 10 ** -11  # Gravitational constant in m^3 kg^-1 s^-2
    return G * (m1 * m2) / (distance ** 2)


# Function to calculate kinetic energy
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)


# Function to calculate current, voltage, or resistance (Ohm's Law)
def ohms_law(value1, value2, value_type):
    if value_type == "voltage":
        return value1 * value2  # V = I * R
    elif value_type == "current":
        return value1 / value2  # I = V / R
    elif value_type == "resistance":
     return value1 / value2  # R = V / I
    else:
        return None


def main():
    print("Physics Calculator")
    print("Select a calculation:")
    print("a. Maximum Height of a Projectile")
    print("b. Range of a Projectile")
    print("c. Gravitational Force Between Two Objects")
    print("d. Kinetic Energy")
    print("e. Ohm's Law (Voltage, Current, Resistance)")

    choice = input("Enter the number of the calculation you want to perform: ")

    if choice == 'a':  # Maximum Height of a Projectile
        initial_velocity = float(input("Enter the initial velocity (m/s): "))
        height = calculate_max_height(initial_velocity)
        print(f"Maximum height = {height:.2f} meters")

    elif choice == 'b':  # Range of a Projectile
        initial_velocity = float(input("Enter the initial velocity (m/s): "))
        angle_of_launch = float(input("Enter the launch angle (degrees): "))
        range_ = calculate_range(initial_velocity, angle_of_launch)
        print(f"Range of the projectile = {range_:.2f} meters")

    elif choice == 'c':  # Gravitational Force
        m1 = float(input("Enter the mass of the first object (kg): "))
        m2 = float(input("Enter the mass of the second object (kg): "))
        distance = float(input("Enter the distance between the two objects (m): "))
        force = calculate_gravitational_force(m1, m2, distance)
        print(f"Gravitational force = {force:.2e} N")

    elif choice == 'd':  # Kinetic Energy
        mass = float(input("Enter the mass of the object (kg): "))
        velocity = float(input("Enter the velocity of the object (m/s): "))
        ke = calculate_kinetic_energy(mass, velocity)
        print(f"Kinetic energy = {ke:.2f} Joules")

    elif choice == 'e':  # Ohm's Law
        value_type = input("Enter the quantity you want to calculate (voltage, current, or resistance): ").lower()

        if value_type == "voltage":
            current = float(input("Enter current (A): "))
            resistance = float(input("Enter resistance (Ω): "))
            voltage = ohms_law(current, resistance, "voltage")
            print(f"Voltage = {voltage:.2f} V")

        elif value_type == "current":
            voltage = float(input("Enter voltage (V): "))
            resistance = float(input("Enter resistance (Ω): "))
            current = ohms_law(voltage, resistance, "current")
            print(f"Current = {current:.2f} A")

        elif value_type == "resistance":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))
            resistance = ohms_law(voltage, current, "resistance")
            print(f"Resistance = {resistance:.2f} Ω")

        else:
            print("Invalid option for Ohm's law. Please choose 'voltage', 'current', or 'resistance'.")

    else:
        print("Invalid choice, please restart the program and choose a valid option.")


if __name__ == "__main__":
    main()

