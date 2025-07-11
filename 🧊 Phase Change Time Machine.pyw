import turtle
import random
import math
import time
import colorsys
from collections import deque

class Vector3D:
    """3D Vector for realistic physics - no numpy needed"""
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = float(x), float(y), float(z)
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        mag = self.magnitude()
        if mag > 0:
            return Vector3D(self.x/mag, self.y/mag, self.z/mag)
        return Vector3D(0, 0, 0)
    
    def to_2d(self, camera_distance=500):
        """Project 3D to 2D screen coordinates"""
        if self.z + camera_distance > 0:
            screen_x = (self.x * camera_distance) / (self.z + camera_distance)
            screen_y = (self.y * camera_distance) / (self.z + camera_distance)
            return screen_x, screen_y
        return self.x, self.y

class PhysicsEngine:
    """Advanced physics simulation"""
    def __init__(self):
        self.temperature = 273.15  # Kelvin
        self.pressure = 1.0
        self.gravity = Vector3D(0, -0.05, 0)
        self.time_step = 0.02
        self.viscosity = 0.5
        self.intermolecular_force = 0.3
        
    def update_state_properties(self, state):
        """Update physics for different matter states"""
        if state == "solid":
            self.temperature = 200
            self.viscosity = 0.9
            self.intermolecular_force = 0.8
        elif state == "liquid":
            self.temperature = 300
            self.viscosity = 0.5
            self.intermolecular_force = 0.4
        elif state == "gas":
            self.temperature = 400
            self.viscosity = 0.1
            self.intermolecular_force = 0.1
        elif state == "plasma":
            self.temperature = 10000
            self.viscosity = 0.05
            self.intermolecular_force = 0.01
        elif state == "bec":
            self.temperature = 0.001
            self.viscosity = 0.95
            self.intermolecular_force = 0.9

class AdvancedParticle:
    """Professional particle with quantum effects"""
    def __init__(self, position, state, particle_id):
        self.position = position
        self.velocity = Vector3D(
            random.uniform(-1, 1), 
            random.uniform(-1, 1), 
            random.uniform(-1, 1)
        )
        self.acceleration = Vector3D(0, 0, 0)
        self.state = state
        self.id = particle_id
        self.mass = 1.0
        self.charge = random.choice([-1, 0, 1])
        self.spin = random.uniform(0, 2 * math.pi)
        self.energy = random.uniform(0.5, 2.0)
        self.wave_function = 0
        self.lifetime = random.randint(500, 1500)
        self.age = 0
        self.trail = deque(maxlen=15)
        
        # Create turtle for this particle
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.setup_appearance()
    
    def setup_appearance(self):
        """Setup particle look based on state"""
        if self.state == "solid":
            self.turtle.shape("square")
            self.turtle.color("lightblue")
            self.size = 0.8
        elif self.state == "liquid":
            self.turtle.shape("circle")
            self.turtle.color("blue")
            self.size = 0.6
        elif self.state == "gas":
            self.turtle.shape("circle")
            self.turtle.color("red")
            self.size = 0.4
        elif self.state == "plasma":
            self.turtle.shape("triangle")
            self.turtle.color("magenta")
            self.size = 0.5
        elif self.state == "bec":
            self.turtle.shape("circle")
            # Quantum color effect
            hue = (time.time() + self.id * 0.1) % 1.0
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
            self.turtle.color(color)
            self.size = 1.0
    
    def apply_forces(self, physics_engine, other_particles):
        """Apply realistic forces"""
        self.acceleration = Vector3D(0, 0, 0)
        
        # Gravity (except for plasma)
        if self.state != "plasma":
            self.acceleration = self.acceleration + physics_engine.gravity
        
        # Intermolecular forces
        for other in other_particles:
            if other.id != self.id:
                dx = other.position.x - self.position.x
                dy = other.position.y - self.position.y
                dz = other.position.z - self.position.z
                distance = math.sqrt(dx**2 + dy**2 + dz**2)
                
                if distance > 0 and distance < 100:
                    force_strength = 0
                    
                    if self.state == "solid":
                        # Strong short-range attraction
                        if distance < 40:
                            force_strength = physics_engine.intermolecular_force * (40 - distance) / 40 * 0.02
                    elif self.state == "liquid":
                        # Moderate attraction
                        if distance < 25:
                            force_strength = physics_engine.intermolecular_force * (25 - distance) / 25 * 0.01
                    elif self.state == "plasma":
                        # Electromagnetic forces
                        if self.charge != 0 and other.charge != 0:
                            force_strength = (self.charge * other.charge) / (distance**2) * 0.005
                    elif self.state == "bec":
                        # Quantum coherence
                        if distance < 60:
                            force_strength = math.cos(distance * 0.1) * 0.008
                    
                    if force_strength != 0:
                        force_x = force_strength * dx / distance
                        force_y = force_strength * dy / distance
                        force_z = force_strength * dz / distance
                        self.acceleration = self.acceleration + Vector3D(force_x, force_y, force_z)
        
        # Viscosity damping
        damping = self.velocity * (-physics_engine.viscosity * 0.02)
        self.acceleration = self.acceleration + damping
        
        # Random thermal motion
        thermal_force = physics_engine.temperature * 0.0001
        self.acceleration = self.acceleration + Vector3D(
            random.uniform(-thermal_force, thermal_force),
            random.uniform(-thermal_force, thermal_force),
            random.uniform(-thermal_force, thermal_force)
        )
    
    def update_quantum_properties(self):
        """Update quantum effects"""
        self.wave_function = math.sin(time.time() * 5 + self.id * 0.5) * self.energy
        self.spin += 0.05
        self.age += 1
        
        # Quantum tunneling for BEC
        if self.state == "bec" and random.random() < 0.005:
            self.position.x += random.uniform(-30, 30)
            self.position.y += random.uniform(-30, 30)
        
        # Particle decay/regeneration
        if self.age > self.lifetime:
            self.age = 0
            self.lifetime = random.randint(500, 1500)
            self.energy = random.uniform(0.5, 2.0)
    
    def update_position(self, physics_engine):
        """Update particle position"""
        # Store trail
        screen_pos = self.position.to_2d()
        self.trail.append(screen_pos)
        
        # Update physics
        self.velocity = self.velocity + self.acceleration * physics_engine.time_step
        self.position = self.position + self.velocity * physics_engine.time_step
        
        # Boundary conditions with realistic collisions
        if abs(self.position.x) > 350:
            self.position.x = 350 if self.position.x > 0 else -350
            self.velocity.x *= -0.7
        if abs(self.position.y) > 250:
            self.position.y = 250 if self.position.y > 0 else -250
            self.velocity.y *= -0.7
        if abs(self.position.z) > 100:
            self.position.z = 100 if self.position.z > 0 else -100
            self.velocity.z *= -0.7
        
        self.update_quantum_properties()
    
    def render(self, camera_angle=0):
        """Render particle with 3D effects"""
        screen_x, screen_y = self.position.to_2d()
        
        # 3D rotation effect
        rotated_x = screen_x * math.cos(camera_angle) - screen_y * math.sin(camera_angle)
        rotated_y = screen_x * math.sin(camera_angle) + screen_y * math.cos(camera_angle)
        
        # Size based on Z-depth
        depth_factor = 1.0 - (abs(self.position.z) / 200)
        render_size = self.size * max(0.3, depth_factor)
        
        # Draw particle
        self.turtle.goto(rotated_x, rotated_y)
        self.turtle.shapesize(render_size, render_size)
        self.turtle.showturtle()
        
        # Draw trails for special states
        if self.state in ["plasma", "bec"] and len(self.trail) > 2:
            self.turtle.pendown()
            self.turtle.pensize(1)
            for i in range(len(self.trail) - 1):
                alpha = i / len(self.trail)
                self.turtle.goto(self.trail[i][0], self.trail[i][1])
            self.turtle.penup()
        
        # Quantum wave visualization for BEC
        if self.state == "bec":
            self.turtle.pendown()
            self.turtle.pensize(1)
            wave_radius = 15 + abs(self.wave_function) * 5
            for angle in range(0, 360, 30):
                wave_x = rotated_x + wave_radius * math.cos(math.radians(angle))
                wave_y = rotated_y + wave_radius * math.sin(math.radians(angle))
                self.turtle.goto(wave_x, wave_y)
            self.turtle.penup()

class PhaseTransitionEffect:
    """Visual effects for state changes"""
    def __init__(self):
        self.effect_turtle = turtle.Turtle()
        self.effect_turtle.penup()
        self.effect_turtle.speed(0)
        self.effect_turtle.hideturtle()
    
    def create_effect(self, from_state, to_state):
        """Create transition effects"""
        self.effect_turtle.goto(0, 0)
        self.effect_turtle.pendown()
        
        if from_state == "solid" and to_state == "liquid":
            # Melting effect
            self.effect_turtle.color("lightblue")
            self.effect_turtle.pensize(3)
            for i in range(10):
                self.effect_turtle.circle(i * 5)
        
        elif from_state == "liquid" and to_state == "gas":
            # Evaporation effect
            self.effect_turtle.color("white")
            self.effect_turtle.pensize(2)
            for i in range(20):
                self.effect_turtle.goto(random.uniform(-100, 100), i * 5)
        
        elif from_state == "gas" and to_state == "plasma":
            # Ionization effect
            self.effect_turtle.color("yellow")
            self.effect_turtle.pensize(1)
            for i in range(30):
                angle = random.uniform(0, 2 * math.pi)
                length = random.uniform(20, 80)
                end_x = length * math.cos(angle)
                end_y = length * math.sin(angle)
                self.effect_turtle.goto(end_x, end_y)
                self.effect_turtle.goto(0, 0)
        
        elif to_state == "bec":
            # Quantum coherence effect
            self.effect_turtle.color("cyan")
            self.effect_turtle.pensize(1)
            for radius in range(5, 100, 10):
                self.effect_turtle.circle(radius)
        
        self.effect_turtle.penup()
        self.effect_turtle.clear()

class PhaseChangeMachine:
    """Main game engine - IDLE compatible"""
    def __init__(self):
        # Setup screen
        self.screen = turtle.Screen()
        self.screen.title("🧊 Phase Change Time Machine - Professional Physics")
        self.screen.bgcolor("black")
        self.screen.setup(width=1000, height=700)
        self.screen.tracer(0)
        
        # Game components
        self.physics_engine = PhysicsEngine()
        self.particles = []
        self.current_state = "solid"
        self.camera_angle = 0
        self.score = 0
        self.level = 1
        self.transition_effects = PhaseTransitionEffect()
        
        # Create HUD
        self.create_hud()
        
        # Create particles
        self.create_particle_system()
        
        # Setup controls
        self.setup_controls()
        
        # Game state
        self.running = True
        self.frame_count = 0
        
        print("🧊 Phase Change Time Machine Started!")
        print("Controls:")
        print("1-5: Change states (Solid, Liquid, Gas, Plasma, BEC)")
        print("Arrow keys: Rotate camera and adjust temperature")
        print("ESC: Exit game")
        
        # Start game loop
        self.game_loop()
    
    def create_hud(self):
        """Create game interface"""
        self.hud = turtle.Turtle()
        self.hud.hideturtle()
        self.hud.penup()
        self.hud.color("white")
        self.hud.goto(-480, 300)
        
        self.state_display = turtle.Turtle()
        self.state_display.hideturtle()
        self.state_display.penup()
        self.state_display.color("cyan")
        self.state_display.goto(-480, 270)
        
        self.physics_display = turtle.Turtle()
        self.physics_display.hideturtle()
        self.physics_display.penup()
        self.physics_display.color("yellow")
        self.physics_display.goto(-480, 240)
        
        self.instructions = turtle.Turtle()
        self.instructions.hideturtle()
        self.instructions.penup()
        self.instructions.color("lightgreen")
        self.instructions.goto(-480, -300)
        self.instructions.write("1-5: States | Arrows: Camera/Temp | ESC: Exit", font=("Arial", 12, "normal"))
    
    def create_particle_system(self):
        """Create particle system"""
        self.particles = []
        for i in range(30):  # Reduced for better performance in IDLE
            x = random.uniform(-200, 200)
            y = random.uniform(-150, 150)
            z = random.uniform(-50, 50)
            position = Vector3D(x, y, z)
            particle = AdvancedParticle(position, self.current_state, i)
            self.particles.append(particle)
    
    def setup_controls(self):
        """Setup keyboard controls"""
        self.screen.listen()
        self.screen.onkey(lambda: self.change_state("solid"), "1")
        self.screen.onkey(lambda: self.change_state("liquid"), "2")
        self.screen.onkey(lambda: self.change_state("gas"), "3")
        self.screen.onkey(lambda: self.change_state("plasma"), "4")
        self.screen.onkey(lambda: self.change_state("bec"), "5")
        self.screen.onkey(self.rotate_left, "Left")
        self.screen.onkey(self.rotate_right, "Right")
        self.screen.onkey(self.temp_up, "Up")
        self.screen.onkey(self.temp_down, "Down")
        self.screen.onkey(self.exit_game, "Escape")
    
    def change_state(self, new_state):
        """Change matter state"""
        if new_state != self.current_state:
            print(f"Phase transition: {self.current_state} → {new_state}")
            
            # Create visual effect
            self.transition_effects.create_effect(self.current_state, new_state)
            
            # Update state
            old_state = self.current_state
            self.current_state = new_state
            self.physics_engine.update_state_properties(new_state)
            
            # Update particles
            for particle in self.particles:
                particle.state = new_state
                particle.setup_appearance()
            
            # Score and level
            self.score += 150
            if self.score > self.level * 1000:
                self.level += 1
                print(f"Level up! Now level {self.level}")
    
    def rotate_left(self):
        self.camera_angle -= 0.1
    
    def rotate_right(self):
        self.camera_angle += 0.1
    
    def temp_up(self):
        self.physics_engine.temperature += 100
        print(f"Temperature increased to {self.physics_engine.temperature:.1f}K")
    
    def temp_down(self):
        self.physics_engine.temperature = max(0.1, self.physics_engine.temperature - 100)
        print(f"Temperature decreased to {self.physics_engine.temperature:.1f}K")
    
    def exit_game(self):
        self.running = False
        print("Thanks for playing!")
    
    def update_hud(self):
        """Update display"""
        self.hud.clear()
        self.hud.write(f"Score: {self.score} | Level: {self.level} | Frame: {self.frame_count}", 
                      font=("Arial", 14, "bold"))
        
        self.state_display.clear()
        self.state_display.write(f"State: {self.current_state.upper()}", 
                                font=("Arial", 12, "bold"))
        
        self.physics_display.clear()
        self.physics_display.write(
            f"Temp: {self.physics_engine.temperature:.1f}K | Particles: {len(self.particles)}", 
            font=("Arial", 10, "normal")
        )
    
    def game_loop(self):
        """Main game loop - optimized for IDLE"""
        while self.running:
            try:
                self.frame_count += 1
                
                # Update physics (every frame)
                for particle in self.particles:
                    particle.apply_forces(self.physics_engine, self.particles)
                    particle.update_position(self.physics_engine)
                
                # Render (every 2nd frame for performance)
                if self.frame_count % 2 == 0:
                    # Clear old particles
                    for particle in self.particles:
                        particle.turtle.hideturtle()
                    
                    # Render particles
                    for particle in self.particles:
                        particle.render(self.camera_angle)
                    
                    # Update HUD
                    self.update_hud()
                    
                    # Update screen
                    self.screen.update()
                
                # Control frame rate
                time.sleep(0.03)  # ~30 FPS for smooth IDLE performance
                
            except turtle.Terminator:
                break
            except KeyboardInterrupt:
                break
        
        print("Game ended!")
        self.screen.bye()

# Start the game
if __name__ == "__main__":
    try:
        game = PhaseChangeMachine()
    except Exception as e:
        print(f"Error starting game: {e}")
        print("Make sure you're running this in Python IDLE!")
