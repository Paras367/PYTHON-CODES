import tkinter as tk
from tkinter import messagebox
elements = {
    'H': {'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'shells': [1], 'category': 'nonmetal'},
    'He': {'name': 'Helium', 'atomic_number': 2, 'atomic_mass': 4.0026, 'shells': [2], 'category': 'noble gas'},
    'Li': {'name': 'Lithium', 'atomic_number': 3, 'atomic_mass': 6.94, 'shells': [2, 1], 'category': 'alkali metal'},
    'Be': {'name': 'Beryllium', 'atomic_number': 4, 'atomic_mass': 9.0122, 'shells': [2, 2], 'category': 'alkaline earth metal'},
    'B': {'name': 'Boron', 'atomic_number': 5, 'atomic_mass': 10.81, 'shells': [2, 3], 'category': 'metalloid'},
    'C': {'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'shells': [2, 4], 'category': 'nonmetal'},
    'N': {'name': 'Nitrogen', 'atomic_number': 7, 'atomic_mass': 14.007, 'shells': [2, 5], 'category': 'nonmetal'},
    'O': {'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'shells': [2, 6], 'category': 'nonmetal'},
    'F': {'name': 'Fluorine', 'atomic_number': 9, 'atomic_mass': 18.998, 'shells': [2, 7], 'category': 'nonmetal'},
    'Ne': {'name': 'Neon', 'atomic_number': 10, 'atomic_mass': 20.18, 'shells': [2, 8], 'category': 'noble gas'},
    'Na': {'name': 'Sodium', 'atomic_number': 11, 'atomic_mass': 22.990, 'shells': [2, 8, 1], 'category': 'alkali metal'},
    'Mg': {'name': 'Magnesium', 'atomic_number': 12, 'atomic_mass': 24.305, 'shells': [2, 8, 2], 'category': 'alkaline earth metal'},
    'Al': {'name': 'Aluminium', 'atomic_number': 13, 'atomic_mass': 26.982, 'shells': [2, 8, 3], 'category': 'post-transition metal'},
    'Si': {'name': 'Silicon', 'atomic_number': 14, 'atomic_mass': 28.085, 'shells': [2, 8, 4], 'category': 'metalloid'},
    'P': {'name': 'Phosphorus', 'atomic_number': 15, 'atomic_mass': 30.974, 'shells': [2, 8, 5], 'category': 'nonmetal'},
    'S': {'name': 'Sulphur', 'atomic_number': 16, 'atomic_mass': 32.06, 'shells': [2, 8, 6], 'category': 'nonmetal'},
    'Cl': {'name': 'Chlorine', 'atomic_number': 17, 'atomic_mass': 35.45, 'shells': [2, 8, 7], 'category': 'nonmetal'},
    'Ar': {'name': 'Argon', 'atomic_number': 18, 'atomic_mass': 39.948, 'shells': [2, 8, 8], 'category': 'noble gas'},
    'K': {'name': 'Potassium', 'atomic_number': 19, 'atomic_mass': 39.098, 'shells': [2, 8, 8, 1], 'category': 'alkali metal'},
    'Ca': {'name': 'Calcium', 'atomic_number': 20, 'atomic_mass': 40.078, 'shells': [2, 8, 8, 2], 'category': 'alkaline earth metal'},
    'Sc': {'name': 'Scandium', 'atomic_number': 21, 'atomic_mass': 44.956, 'shells': [2, 8, 9, 2], 'category': 'transition metal'},
    'Ti': {'name': 'Titanium', 'atomic_number': 22, 'atomic_mass': 47.867, 'shells': [2, 8, 10, 2], 'category': 'transition metal'},
    'V': {'name': 'Vanadium', 'atomic_number': 23, 'atomic_mass': 50.942, 'shells': [2, 8, 11, 2], 'category': 'transition metal'},
    'Cr': {'name': 'Chromium', 'atomic_number': 24, 'atomic_mass': 51.996, 'shells': [2, 8, 13, 1], 'category': 'transition metal'},
    'Mn': {'name': 'Manganese', 'atomic_number': 25, 'atomic_mass': 54.938, 'shells': [2, 8, 13, 2], 'category': 'transition metal'},
    'Fe': {'name': 'Iron', 'atomic_number': 26, 'atomic_mass': 55.845, 'shells': [2, 8, 14, 2], 'category': 'transition metal'},
    'Co': {'name': 'Cobalt', 'atomic_number': 27, 'atomic_mass': 58.933, 'shells': [2, 8, 15, 2], 'category': 'transition metal'},
    'Ni': {'name': 'Nickel', 'atomic_number': 28, 'atomic_mass': 58.693, 'shells': [2, 8, 16, 2], 'category': 'transition metal'},
    'Cu': {'name': 'Copper', 'atomic_number': 29, 'atomic_mass': 63.546, 'shells': [2, 8, 18, 1], 'category': 'transition metal'},
    'Zn': {'name': 'Zinc', 'atomic_number': 30, 'atomic_mass': 65.38, 'shells': [2, 8, 18, 2], 'category': 'transition metal'},
    'Ga': {'name': 'Gallium', 'atomic_number': 31, 'atomic_mass': 69.723, 'shells': [2, 8, 18, 3], 'category': 'post-transition metal'},
    'Ge': {'name': 'Germanium', 'atomic_number': 32, 'atomic_mass': 72.63, 'shells': [2, 8, 18, 4], 'category': 'metalloid'},
    'As': {'name': 'Arsenic', 'atomic_number': 33, 'atomic_mass': 74.922, 'shells': [2, 8, 18, 5], 'category': 'metalloid'},
    'Se': {'name': 'Selenium', 'atomic_number': 34, 'atomic_mass': 78.971, 'shells': [2, 8, 18, 6], 'category': 'nonmetal'},
    'Br': {'name': 'Bromine', 'atomic_number': 35, 'atomic_mass': 79.904, 'shells': [2, 8, 18, 7], 'category': 'nonmetal'},
    'Kr': {'name': 'Krypton', 'atomic_number': 36, 'atomic_mass': 83.798, 'shells': [2, 8, 18, 8], 'category': 'noble gas'},
    'Rb': {'name': 'Rubidium', 'atomic_number': 37, 'atomic_mass': 85.468, 'shells': [2, 8, 18, 8, 1], 'category': 'alkali metal'},
    'Sr': {'name': 'Strontium', 'atomic_number': 38, 'atomic_mass': 87.62, 'shells': [2, 8, 18, 8, 2], 'category': 'alkaline earth metal'},
    'Y': {'name': 'Yttrium', 'atomic_number': 39, 'atomic_mass': 88.906, 'shells': [2, 8, 18, 9, 2], 'category': 'transition metal'},
    'Zr': {'name': 'Zirconium', 'atomic_number': 40, 'atomic_mass': 91.224, 'shells': [2, 8, 18, 10, 2], 'category': 'transition metal'},
    'Nb': {'name': 'Niobium', 'atomic_number': 41, 'atomic_mass': 92.906, 'shells': [2, 8, 18, 12, 1], 'category': 'transition metal'},
    'Mo': {'name': 'Molybdenum', 'atomic_number': 42, 'atomic_mass': 95.95, 'shells': [2, 8, 18, 13, 1], 'category': 'transition metal'},
    'Tc': {'name': 'Technetium', 'atomic_number': 43, 'atomic_mass': 98, 'shells': [2, 8, 18, 13, 2], 'category': 'transition metal'},
    'Ru': {'name': 'Ruthenium', 'atomic_number': 44, 'atomic_mass': 101.07, 'shells': [2, 8, 18, 15, 1], 'category': 'transition metal'},
    'Rh': {'name': 'Rhodium', 'atomic_number': 45, 'atomic_mass': 102.91, 'shells': [2, 8, 18, 16, 1], 'category': 'transition metal'},
    'Pd': {'name': 'Palladium', 'atomic_number': 46, 'atomic_mass': 106.42, 'shells': [2, 8, 18, 18], 'category': 'transition metal'},
    'Ag': {'name': 'Silver', 'atomic_number': 47, 'atomic_mass': 107.87, 'shells': [2, 8, 18, 18, 1], 'category': 'transition metal'},
    'Cd': {'name': 'Cadmium', 'atomic_number': 48, 'atomic_mass': 112.41, 'shells': [2, 8, 18, 18, 2], 'category': 'transition metal'},
    'In': {'name': 'Indium', 'atomic_number': 49, 'atomic_mass': 114.82, 'shells': [2, 8, 18, 18, 3], 'category': 'post-transition metal'},
    'Sn': {'name': 'Tin', 'atomic_number': 50, 'atomic_mass': 118.71, 'shells': [2, 8, 18, 18, 4], 'category': 'post-transition metal'},
    'Sb': {'name': 'Antimony', 'atomic_number': 51, 'atomic_mass': 121.76, 'shells': [2, 8, 18, 18, 5], 'category': 'metalloid'},
    'Te': {'name': 'Tellurium', 'atomic_number': 52, 'atomic_mass': 127.60, 'shells': [2, 8, 18, 18, 6], 'category': 'metalloid'},
    'I': {'name': 'Iodine', 'atomic_number': 53, 'atomic_mass': 126.90, 'shells': [2, 8, 18, 18, 7], 'category': 'nonmetal'},
    'Xe': {'name': 'Xenon', 'atomic_number': 54, 'atomic_mass': 131.29, 'shells': [2, 8, 18, 18, 8], 'category': 'noble gas'},
    'Cs': {'name': 'Cesium', 'atomic_number': 55, 'atomic_mass': 132.91, 'shells': [2, 8, 18, 18, 8, 1], 'category': 'alkali metal'},
    'Ba': {'name': 'Barium', 'atomic_number': 56, 'atomic_mass': 137.33, 'shells': [2, 8, 18, 18, 8, 2], 'category': 'alkaline earth metal'},
    'La': {'name': 'Lanthanum', 'atomic_number': 57, 'atomic_mass': 138.91, 'shells': [2, 8, 18, 18, 9, 2], 'category': 'lanthanide'},
    'Ce': {'name': 'Cerium', 'atomic_number': 58, 'atomic_mass': 140.12, 'shells': [2, 8, 18, 19, 9, 2], 'category': 'lanthanide'},
    'Pr': {'name': 'Praseodymium', 'atomic_number': 59, 'atomic_mass': 140.91, 'shells': [2, 8, 18, 21, 8, 2], 'category': 'lanthanide'},
    'Nd': {'name': 'Neodymium', 'atomic_number': 60, 'atomic_mass': 144.24, 'shells': [2, 8, 18, 22, 8, 2], 'category': 'lanthanide'},
    'Pm': {'name': 'Promethium', 'atomic_number': 61, 'atomic_mass': 145, 'shells': [2, 8, 18, 23, 8, 2], 'category': 'lanthanide'},
    'Sm': {'name': 'Samarium', 'atomic_number': 62, 'atomic_mass': 150.36, 'shells': [2, 8, 18, 24, 8, 2], 'category': 'lanthanide'},
    'Eu': {'name': 'Europium', 'atomic_number': 63, 'atomic_mass': 151.96, 'shells': [2, 8, 18, 25, 8, 2], 'category': 'lanthanide'},
    'Gd': {'name': 'Gadolinium', 'atomic_number': 64, 'atomic_mass': 157.25, 'shells': [2, 8, 18, 25, 9, 2], 'category': 'lanthanide'},
    'Tb': {'name': 'Terbium', 'atomic_number': 65, 'atomic_mass': 158.93, 'shells': [2, 8, 18, 27, 8, 2], 'category': 'lanthanide'},
    'Dy': {'name': 'Dysprosium', 'atomic_number': 66, 'atomic_mass': 162.50, 'shells': [2, 8, 18, 28, 8, 2], 'category': 'lanthanide'},
    'Ho': {'name': 'Holmium', 'atomic_number': 67, 'atomic_mass': 164.93, 'shells': [2, 8, 18, 29, 8, 2], 'category': 'lanthanide'},
    'Er': {'name': 'Erbium', 'atomic_number': 68, 'atomic_mass': 167.26, 'shells': [2, 8, 18, 30, 8, 2], 'category': 'lanthanide'},
    'Tm': {'name': 'Thulium', 'atomic_number': 69, 'atomic_mass': 168.93, 'shells': [2, 8, 18, 31, 8, 2], 'category': 'lanthanide'},
    'Yb': {'name': 'Ytterbium', 'atomic_number': 70, 'atomic_mass': 173.05, 'shells': [2, 8, 18, 32, 8, 2], 'category': 'lanthanide'},
    'Lu': {'name': 'Lutetium', 'atomic_number': 71, 'atomic_mass': 174.97, 'shells': [2, 8, 18, 32, 9, 2], 'category': 'lanthanide'},
    'Hf': {'name': 'Hafnium', 'atomic_number': 72, 'atomic_mass': 178.49, 'shells': [2, 8, 18, 32, 10, 2], 'category': 'transition metal'},
    'Ta': {'name': 'Tantalum', 'atomic_number': 73, 'atomic_mass': 180.95, 'shells': [2, 8, 18, 32, 11, 2], 'category': 'transition metal'},
    'W': {'name': 'Tungsten', 'atomic_number': 74, 'atomic_mass': 183.84, 'shells': [2, 8, 18, 32, 12, 2], 'category': 'transition metal'},
    'Re': {'name': 'Rhenium', 'atomic_number': 75, 'atomic_mass': 186.21, 'shells': [2, 8, 18, 32, 13, 2], 'category': 'transition metal'},
    'Os': {'name': 'Osmium', 'atomic_number': 76, 'atomic_mass': 190.23, 'shells': [2, 8, 18, 32, 14, 2], 'category': 'transition metal'},
    'Ir': {'name': 'Iridium', 'atomic_number': 77, 'atomic_mass': 192.22, 'shells': [2, 8, 18, 32, 15, 2], 'category': 'transition metal'},
    'Pt': {'name': 'Platinum', 'atomic_number': 78, 'atomic_mass': 195.08, 'shells': [2, 8, 18, 32, 17, 1], 'category': 'transition metal'},
    'Au': {'name': 'Gold', 'atomic_number': 79, 'atomic_mass': 196.97, 'shells': [2, 8, 18, 32, 18, 1], 'category': 'transition metal'},
    'Hg': {'name': 'Mercury', 'atomic_number': 80, 'atomic_mass': 200.59, 'shells': [2, 8, 18, 32, 18, 2], 'category': 'transition metal'},
    'Tl': {'name': 'Thallium', 'atomic_number': 81, 'atomic_mass': 204.38, 'shells': [2, 8, 18, 32, 18, 3], 'category': 'post-transition metal'},
    'Pb': {'name': 'Lead', 'atomic_number': 82, 'atomic_mass': 207.2, 'shells': [2, 8, 18, 32, 18, 4], 'category': 'post-transition metal'},
    'Bi': {'name': 'Bismuth', 'atomic_number': 83, 'atomic_mass': 208.98, 'shells': [2, 8, 18, 32, 18, 5], 'category': 'post-transition metal'},
    'Po': {'name': 'Polonium', 'atomic_number': 84, 'atomic_mass': 209, 'shells': [2, 8, 18, 32, 18, 6], 'category': 'metalloid'},
    'At': {'name': 'Astatine', 'atomic_number': 85, 'atomic_mass': 210, 'shells': [2, 8, 18, 32, 18, 7], 'category': 'metalloid'},
    'Rn': {'name': 'Radon', 'atomic_number': 86, 'atomic_mass': 222, 'shells': [2, 8, 18, 32, 18, 8], 'category': 'noble gas'},
    'Fr': {'name': 'Francium', 'atomic_number': 87, 'atomic_mass': 223, 'shells': [2, 8, 18, 32, 18, 8, 1], 'category': 'alkali metal'},
    'Ra': {'name': 'Radium', 'atomic_number': 88, 'atomic_mass': 226, 'shells': [2, 8, 18, 32, 18, 8, 2], 'category': 'alkaline earth metal'},
    'Ac': {'name': 'Actinium', 'atomic_number': 89, 'atomic_mass': 227, 'shells': [2, 8, 18, 32, 18, 9, 2], 'category': 'actinide'},
    'Th': {'name': 'Thorium', 'atomic_number': 90, 'atomic_mass': 232.04, 'shells': [2, 8, 18, 32, 18, 10, 2], 'category': 'actinide'},
    'Pa': {'name': 'Protactinium', 'atomic_number': 91, 'atomic_mass': 231.04, 'shells': [2, 8, 18, 32, 20, 9, 2], 'category': 'actinide'},
    'U': {'name': 'Uranium', 'atomic_number': 92, 'atomic_mass': 238.03, 'shells': [2, 8, 18, 32, 21, 9, 2], 'category': 'actinide'},
    'Np': {'name': 'Neptunium', 'atomic_number': 93, 'atomic_mass': 237, 'shells': [2, 8, 18, 32, 22, 9, 2], 'category': 'actinide'},
    'Pu': {'name': 'Plutonium', 'atomic_number': 94, 'atomic_mass': 244, 'shells': [2, 8, 18, 32, 24, 8, 2], 'category': 'actinide'},
    'Am': {'name': 'Americium', 'atomic_number': 95, 'atomic_mass': 243, 'shells': [2, 8, 18, 32, 25, 8, 2], 'category': 'actinide'},
    'Cm': {'name': 'Curium', 'atomic_number': 96, 'atomic_mass': 247, 'shells': [2, 8, 18, 32, 25, 9, 2], 'category': 'actinide'},
    'Bk': {'name': 'Berkelium', 'atomic_number': 97, 'atomic_mass': 247, 'shells': [2, 8, 18, 32, 27, 8, 2], 'category': 'actinide'},
    'Cf': {'name': 'Californium', 'atomic_number': 98, 'atomic_mass': 251, 'shells': [2, 8, 18, 32, 28, 8, 2], 'category': 'actinide'},
    'Es': {'name': 'Einsteinium', 'atomic_number': 99, 'atomic_mass': 252, 'shells': [2, 8, 18, 32, 29, 8, 2], 'category': 'actinide'},
    'Fm': {'name': 'Fermium', 'atomic_number': 100, 'atomic_mass': 257, 'shells': [2, 8, 18, 32, 30, 8, 2], 'category': 'actinide'},
    'Md': {'name': 'Mendelevium', 'atomic_number': 101, 'atomic_mass': 258, 'shells': [2, 8, 18, 32, 31, 8, 2], 'category': 'actinide'},
    'No': {'name': 'Nobelium', 'atomic_number': 102, 'atomic_mass': 259, 'shells': [2, 8, 18, 32, 32, 8, 2], 'category': 'actinide'},
    'Lr': {'name': 'Lawrencium', 'atomic_number': 103, 'atomic_mass': 266, 'shells': [2, 8, 18, 32, 32, 8, 3], 'category': 'actinide'},
    'Rf': {'name': 'Rutherfordium', 'atomic_number': 104, 'atomic_mass': 267, 'shells': [2, 8, 18, 32, 32, 10, 2], 'category': 'transition metal'},
    'Db': {'name': 'Dubnium', 'atomic_number': 105, 'atomic_mass': 268, 'shells': [2, 8, 18, 32, 32, 11, 2], 'category': 'transition metal'},
    'Sg': {'name': 'Seaborgium', 'atomic_number': 106, 'atomic_mass': 269, 'shells': [2, 8, 18, 32, 32, 12, 2], 'category': 'transition metal'},
    'Bh': {'name': 'Bohrium', 'atomic_number': 107, 'atomic_mass': 270, 'shells': [2, 8, 18, 32, 32, 13, 2], 'category': 'transition metal'},
    'Hs': {'name': 'Hassium', 'atomic_number': 108, 'atomic_mass': 277, 'shells': [2, 8, 18, 32, 32, 14, 2], 'category': 'transition metal'},
    'Mt': {'name': 'Meitnerium', 'atomic_number': 109, 'atomic_mass': 278, 'shells': [2, 8, 18, 32, 32, 15, 2], 'category': 'unknown'},
    'Ds': {'name': 'Darmstadtium', 'atomic_number': 110, 'atomic_mass': 281, 'shells': [2, 8, 18, 32, 32, 17, 1], 'category': 'unknown'},
    'Rg': {'name': 'Roentgenium', 'atomic_number': 111, 'atomic_mass': 282, 'shells': [2, 8, 18, 32, 32, 17, 2], 'category': 'unknown'},
    'Cn': {'name': 'Copernicium', 'atomic_number': 112, 'atomic_mass': 285, 'shells': [2, 8, 18, 32, 32, 18, 2], 'category': 'transition metal'},
    'Nh': {'name': 'Nihonium', 'atomic_number': 113, 'atomic_mass': 286, 'shells': [2, 8, 18, 32, 32, 18, 3], 'category': 'post-transition metal'},
    'Fl': {'name': 'Flerovium', 'atomic_number': 114, 'atomic_mass': 289, 'shells': [2, 8, 18, 32, 32, 18, 4], 'category': 'post-transition metal'},
    'Mc': {'name': 'Moscovium', 'atomic_number': 115, 'atomic_mass': 290, 'shells': [2, 8, 18, 32, 32, 18, 5], 'category': 'post-transition metal'},
    'Lv': {'name': 'Livermorium', 'atomic_number': 116, 'atomic_mass': 293, 'shells': [2, 8, 18, 32, 32, 18, 6], 'category': 'post-transition metal'},
    'Ts': {'name': 'Tennessine', 'atomic_number': 117, 'atomic_mass': 294, 'shells': [2, 8, 18, 32, 32, 18, 7], 'category': 'halogen'},
    'Og': {'name': 'Oganesson', 'atomic_number': 118, 'atomic_mass': 294, 'shells': [2, 8, 18, 32, 32, 18, 8], 'category': 'noble gas'}
}

category_colors = {
    'alkali metal': 'lightcoral',
    'alkaline earth metal': 'orange',
    'transition metal': 'gold',
    'post-transition metal': 'lightslategray',
    'metalloid': 'lightgreen',
    'nonmetal': 'skyblue',
    'halogen': 'deepskyblue',
    'noble gas': 'plum',
    'lanthanide': 'lightpink',
    'actinide': 'lightyellow',
    'unknown': 'lightgray'
}

layout = [
    ["H"] + ["" for _ in range(16)] + ["He"],
    ["Li", "Be"] + ["" for _ in range(10)] + ["B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg"] + ["" for _ in range(10)] + ["Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
    [],
    ["" for _ in range(2)] + ["Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
    ["" for _ in range(2)] + ["Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]
]


def show_element_details(symbol):
    data = elements.get(symbol, {})
    info = f"{data.get('name')} (Z={data.get('atomic_number')})\nAtomic Mass: {data.get('atomic_mass')}\nShells: {data.get('shells')}"
    messagebox.showinfo(symbol, info)

    
def show_trend():
    top = tk.Toplevel()
    top.title("Atomic Mass Trend")
    canvas = tk.Canvas(top, width=1000, height=400, bg="white")
    canvas.pack()

    values = [(v['atomic_number'], v['atomic_mass']) for v in elements.values() if v.get('atomic_mass')]
    values.sort()
    max_mass = max(v[1] for v in values)

    for i in range(1, len(values)):
        x1 = values[i - 1][0] * 8
        y1 = 350 - values[i - 1][1] * (300 / max_mass)
        x2 = values[i][0] * 8
        y2 = 350 - values[i][1] * (300 / max_mass)
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
        canvas.update()
        canvas.after(10)

root = tk.Tk()
root.title("Interactive Periodic Table")
root.geometry("1250x700")

frame = tk.Frame(root)
frame.pack(pady=10)

hover_label = tk.Label(root, text="", font=("Arial", 10))
hover_label.pack()

def on_enter(e, symbol):
    data = elements.get(symbol, {})
    hover_label.config(text=f"{symbol}: {data.get('name', '')} (Z={data.get('atomic_number', '')})")

def on_leave(e):
    hover_label.config(text="")

for r, row in enumerate(layout):
    for c, symbol in enumerate(row):
        if symbol:
            data = elements.get(symbol, {})
            cat = data.get("category", "unknown")
            color = category_colors.get(cat, "lightgray")
            btn = tk.Button(frame, text=symbol, width=5, height=2,
                            bg=color, command=lambda s=symbol: show_element_details(s))
            btn.grid(row=r, column=c, padx=2, pady=2)
            btn.bind("<Enter>", lambda e, s=symbol: on_enter(e, s))
            btn.bind("<Leave>", on_leave)

tk.Button(root, text="Show Atomic Mass Trend", font=("Arial", 12),
          command=show_trend, bg="lightblue").pack(pady=10)

root.mainloop()


# ©SOFTWARELABS
# BY - PARAS DHIMAN (Co-Founder)
# CONTACT:
#     softwarelabschd@gmail.com
