import tkinter as tk
import math
import random

class Planet:
    def __init__(self, name, distance, size, colors, speed, features=None):
        self.name = name
        self.distance = distance  # Distance from sun
        self.size = size         # Planet size
        self.colors = colors     # List of colors for realistic appearance
        self.speed = speed       # Orbital speed
        self.angle = 0           # Current angle position
        self.x = 0              # Current x position
        self.y = 0              # Current y position
        self.features = features or []  # Special features like rings, spots, etc.
        self.rotation = 0        # Planet rotation for surface features

class SolarSystem:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Realistic Solar System Simulation")
        self.root.geometry("900x700")
        
        # Create canvas for drawing
        self.canvas = tk.Canvas(self.root, width=900, height=650, bg='#000011')
        self.canvas.pack()
        
        # Center of the solar system
        self.center_x = 450
        self.center_y = 325
        
        # Create planets with realistic colors and features
        self.planets = [
            Planet("Mercury", 70, 4, ["#8C7853", "#B8860B", "#A0522D"], 0.08),
            Planet("Venus", 95, 6, ["#FFC649", "#FFB347", "#FF8C00"], 0.06),
            Planet("Earth", 130, 7, ["#6B93D6", "#87CEEB", "#228B22", "#8B4513"], 0.05, ["continents"]),
            Planet("Mars", 165, 5, ["#CD5C5C", "#A0522D", "#8B4513"], 0.04, ["polar_caps"]),
            Planet("Jupiter", 230, 20, ["#D2691E", "#CD853F", "#F4A460", "#DEB887"], 0.02, ["great_red_spot", "bands"]),
            Planet("Saturn", 300, 16, ["#FAD5A5", "#DEB887", "#F4A460"], 0.015, ["rings"]),
            Planet("Uranus", 370, 10, ["#4FD0E7", "#87CEEB", "#B0E0E6"], 0.01, ["tilt"]),
            Planet("Neptune", 440, 9, ["#4169E1", "#0000CD", "#191970"], 0.008, ["storms"])
        ]
        
        # Control variables
        self.running = False
        self.speed_multiplier = 1.0
        self.show_names = True
        self.show_orbits = True
        
        # Create control buttons
        self.create_controls()
        
        # Start the simulation
        self.animate()
    
    def create_controls(self):
        # Frame for controls
        control_frame = tk.Frame(self.root, bg='black')
        control_frame.pack(pady=10)
        
        # Start/Stop button
        self.start_button = tk.Button(control_frame, text="Start", command=self.toggle_simulation,
                                     bg='#333333', fg='white', font=('Arial', 10))
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Speed control
        tk.Label(control_frame, text="Speed:", bg='black', fg='white').pack(side=tk.LEFT, padx=5)
        self.speed_scale = tk.Scale(control_frame, from_=0.1, to=3.0, resolution=0.1, 
                                   orient=tk.HORIZONTAL, command=self.update_speed,
                                   bg='#333333', fg='white', highlightbackground='black')
        self.speed_scale.set(1.0)
        self.speed_scale.pack(side=tk.LEFT, padx=5)
        
        # Reset button
        reset_button = tk.Button(control_frame, text="Reset", command=self.reset_simulation,
                               bg='#333333', fg='white', font=('Arial', 10))
        reset_button.pack(side=tk.LEFT, padx=5)
        
        # Toggle names
        names_button = tk.Button(control_frame, text="Toggle Names", command=self.toggle_names,
                               bg='#333333', fg='white', font=('Arial', 10))
        names_button.pack(side=tk.LEFT, padx=5)
        
        # Toggle orbits
        orbits_button = tk.Button(control_frame, text="Toggle Orbits", command=self.toggle_orbits,
                                bg='#333333', fg='white', font=('Arial', 10))
        orbits_button.pack(side=tk.LEFT, padx=5)
    
    def toggle_simulation(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Stop")
        else:
            self.start_button.config(text="Start")
    
    def update_speed(self, value):
        self.speed_multiplier = float(value)
    
    def reset_simulation(self):
        for planet in self.planets:
            planet.angle = 0
            planet.rotation = 0
        self.running = False
        self.start_button.config(text="Start")
    
    def toggle_names(self):
        self.show_names = not self.show_names
    
    def toggle_orbits(self):
        self.show_orbits = not self.show_orbits
    
    def calculate_positions(self):
        # Update planet positions
        for planet in self.planets:
            if self.running:
                planet.angle += planet.speed * self.speed_multiplier
                planet.rotation += planet.speed * self.speed_multiplier * 5  # Planets rotate faster
                
                # Keep angles between 0 and 2*pi
                if planet.angle > 2 * math.pi:
                    planet.angle -= 2 * math.pi
                if planet.rotation > 2 * math.pi:
                    planet.rotation -= 2 * math.pi
            
            # Calculate x,y coordinates
            planet.x = self.center_x + planet.distance * math.cos(planet.angle)
            planet.y = self.center_y + planet.distance * math.sin(planet.angle)
    
    def draw_gradient_circle(self, x, y, radius, colors):
        # Create a gradient effect by drawing multiple circles
        for i in range(radius, 0, -1):
            # Calculate which color to use based on distance from center
            color_index = min(int((radius - i) / radius * len(colors)), len(colors) - 1)
            color = colors[color_index]
            
            # Add some variation for texture
            if i < radius * 0.8:
                self.canvas.create_oval(x - i, y - i, x + i, y + i,
                                       fill=color, outline=color)
    
    def draw_planet_features(self, planet):
        x, y = planet.x, planet.y
        
        # Earth features
        if "continents" in planet.features:
            # Draw continents as darker spots
            for i in range(3):
                offset_x = math.cos(planet.rotation + i * 2) * (planet.size * 0.6)
                offset_y = math.sin(planet.rotation + i * 2) * (planet.size * 0.6)
                self.canvas.create_oval(x + offset_x - 2, y + offset_y - 2,
                                       x + offset_x + 2, y + offset_y + 2,
                                       fill="#228B22", outline="#228B22")
        
        # Mars polar caps
        if "polar_caps" in planet.features:
            # White spots at "poles"
            self.canvas.create_oval(x - 2, y - planet.size + 1,
                                   x + 2, y - planet.size + 3,
                                   fill="white", outline="white")
            self.canvas.create_oval(x - 2, y + planet.size - 3,
                                   x + 2, y + planet.size - 1,
                                   fill="white", outline="white")
        
        # Jupiter's Great Red Spot and bands
        if "great_red_spot" in planet.features:
            # Great Red Spot
            spot_x = x + math.cos(planet.rotation) * (planet.size * 0.5)
            spot_y = y + math.sin(planet.rotation) * (planet.size * 0.5)
            self.canvas.create_oval(spot_x - 3, spot_y - 2,
                                   spot_x + 3, spot_y + 2,
                                   fill="#8B0000", outline="#8B0000")
        
        if "bands" in planet.features:
            # Horizontal bands
            for i in range(-1, 2):
                band_y = y + i * (planet.size * 0.4)
                self.canvas.create_line(x - planet.size, band_y,
                                       x + planet.size, band_y,
                                       fill="#8B4513", width=2)
        
        # Saturn's rings
        if "rings" in planet.features:
            # Draw rings
            for ring_size in [planet.size + 8, planet.size + 12, planet.size + 16]:
                self.canvas.create_oval(x - ring_size, y - ring_size//4,
                                       x + ring_size, y + ring_size//4,
                                       outline="#DAA520", width=2)
        
        # Neptune storms
        if "storms" in planet.features:
            # Draw storm spots
            storm_x = x + math.cos(planet.rotation + 1) * (planet.size * 0.4)
            storm_y = y + math.sin(planet.rotation + 1) * (planet.size * 0.4)
            self.canvas.create_oval(storm_x - 2, storm_y - 2,
                                   storm_x + 2, storm_y + 2,
                                   fill="#000080", outline="#000080")
    
    def draw_solar_system(self):
        # Clear canvas
        self.canvas.delete("all")
        
        # Draw stars in background
        for _ in range(100):
            star_x = random.randint(0, 900)
            star_y = random.randint(0, 650)
            self.canvas.create_oval(star_x, star_y, star_x + 1, star_y + 1,
                                   fill="white", outline="white")
        
        # Draw orbital paths
        if self.show_orbits:
            for planet in self.planets:
                self.canvas.create_oval(
                    self.center_x - planet.distance, self.center_y - planet.distance,
                    self.center_x + planet.distance, self.center_y + planet.distance,
                    outline="#333333", width=1
                )
        
        # Draw sun with realistic appearance
        sun_colors = ["#FFD700", "#FFA500", "#FF4500", "#FF6347"]
        self.draw_gradient_circle(self.center_x, self.center_y, 20, sun_colors)
        
        # Sun corona effect
        for i in range(8):
            ray_angle = i * math.pi / 4
            ray_x = self.center_x + math.cos(ray_angle) * 25
            ray_y = self.center_y + math.sin(ray_angle) * 25
            ray_end_x = self.center_x + math.cos(ray_angle) * 30
            ray_end_y = self.center_y + math.sin(ray_angle) * 30
            self.canvas.create_line(ray_x, ray_y, ray_end_x, ray_end_y,
                                   fill="#FFD700", width=2)
        
        if self.show_names:
            self.canvas.create_text(self.center_x, self.center_y - 35, text="Sun", 
                                   fill="white", font=("Arial", 10, "bold"))
        
        # Draw planets with realistic appearance
        for planet in self.planets:
            # Draw planet with gradient
            self.draw_gradient_circle(planet.x, planet.y, planet.size, planet.colors)
            
            # Draw planet features
            self.draw_planet_features(planet)
            
            # Draw planet names
            if self.show_names:
                self.canvas.create_text(planet.x, planet.y + planet.size + 15, 
                                       text=planet.name, fill="white", 
                                       font=("Arial", 9, "bold"))
        
        # Draw title
        self.canvas.create_text(450, 25, text="Realistic Solar System Simulation", 
                               fill="white", font=("Arial", 18, "bold"))
        
        # Draw realistic info
        info_text = "Realistic colors, gradients, and planetary features included!"
        self.canvas.create_text(450, 45, text=info_text, 
                               fill="gray", font=("Arial", 10))
    
    def animate(self):
        # Calculate new positions
        self.calculate_positions()
        
        # Draw everything
        self.draw_solar_system()
        
        # Schedule next frame (approximately 60 FPS)
        self.root.after(16, self.animate)
    
    def run(self):
        self.root.mainloop()

# Create and run the solar system simulation
if __name__ == "__main__":
    print("Starting Realistic Solar System Simulation...")
    print("Features:")
    print("- Realistic planet colors and gradients")
    print("- Earth: continents visible")
    print("- Mars: polar ice caps")
    print("- Jupiter: Great Red Spot and bands")
    print("- Saturn: prominent ring system")
    print("- Neptune: storm systems")
    print("- Sun: corona rays and gradient")
    print("- Starfield background")
    print("")
    print("Controls:")
    print("- Start/Stop: Begin/pause animation")
    print("- Speed: Adjust orbital speed")
    print("- Reset: Return to starting positions")
    print("- Toggle Names: Show/hide planet names")
    print("- Toggle Orbits: Show/hide orbital paths")
    print("Close the window to exit.")
    
    solar_system = SolarSystem()
    solar_system.run()


# ©SOFTWARELABS
# BY - PARAS DHIMAN (Co-Founder)
# CONTACT:
#     softwarelabschd@gmail.com
