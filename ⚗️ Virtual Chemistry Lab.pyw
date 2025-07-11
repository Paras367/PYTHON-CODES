import turtle
import math
import time
import random

class ChemistryLab:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("lightgray")
        self.screen.title("⚗️ Virtual Chemistry Lab - Titration Simulator")
        self.screen.setup(1000, 700)
        
       
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        
        
        self.titration_types = {
            "1": {"name": "Strong Acid + Strong Base", "acid": "HCl", "base": "NaOH", 
                  "acid_pka": -7, "base_pkb": -7, "endpoint": 7.0},
            "2": {"name": "Weak Acid + Strong Base", "acid": "CH3COOH", "base": "NaOH", 
                  "acid_pka": 4.75, "base_pkb": -7, "endpoint": 8.7},
            "3": {"name": "Strong Acid + Weak Base", "acid": "HCl", "base": "NH3", 
                  "acid_pka": -7, "base_pkb": 4.75, "endpoint": 5.3},
            "4": {"name": "Weak Acid + Weak Base", "acid": "CH3COOH", "base": "NH3", 
                  "acid_pka": 4.75, "base_pkb": 4.75, "endpoint": 7.0}
        }
        
       
        self.burette_x = 150
        self.burette_y = 200
        self.beaker_x = 0
        self.beaker_y = -150
        
       
        self.ph_data = []
        self.volume_data = []
        self.current_ph = 1.0
        self.volume_added = 0.0
        self.max_volume = 50.0
        self.titrant_rate = 0.5
        self.selected_titration = None
        self.endpoint_reached = False
        
       
        self.ph_colors = {
            1: "#FF0000", 2: "#FF4500", 3: "#FF8C00", 4: "#FFA500",
            5: "#FFFF00", 6: "#ADFF2F", 7: "#00FF00", 8: "#00CED1",
            9: "#0000FF", 10: "#4B0082", 11: "#8B00FF", 12: "#FF00FF",
            13: "#FF1493", 14: "#DC143C"
        }

    def draw_title(self):
        """Draw the lab title with fancy effects"""
        self.pen.penup()
        self.pen.goto(-400, 300)
        self.pen.color("darkblue")
        self.pen.write("⚗️ VIRTUAL CHEMISTRY LAB", font=("Arial", 24, "bold"))
        
        self.pen.goto(-300, 270)
        self.pen.color("purple")
        self.pen.write("Acid-Base Titration Simulator", font=("Arial", 16, "italic"))

    def draw_burette(self):
        """Draw animated burette with liquid"""
       
        self.pen.penup()
        self.pen.goto(self.burette_x - 20, self.burette_y + 100)
        self.pen.pendown()
        self.pen.color("black")
        self.pen.setheading(270)
        self.pen.forward(200)
        self.pen.left(90)
        self.pen.forward(40)
        self.pen.left(90)
        self.pen.forward(200)
        self.pen.left(90)
        self.pen.forward(40)
        
        
        liquid_height = 180 * (1 - self.volume_added / self.max_volume)
        self.pen.penup()
        self.pen.goto(self.burette_x - 18, self.burette_y + 98)
        self.pen.pendown()
        self.pen.color("lightblue")
        self.pen.begin_fill()
        self.pen.setheading(270)
        self.pen.forward(liquid_height)
        self.pen.left(90)
        self.pen.forward(36)
        self.pen.left(90)
        self.pen.forward(liquid_height)
        self.pen.left(90)
        self.pen.forward(36)
        self.pen.end_fill()
        
        
        self.pen.penup()
        self.pen.goto(self.burette_x, self.burette_y - 110)
        self.pen.pendown()
        self.pen.color("black")
        self.pen.circle(5)
        
       
        for i in range(0, 51, 10):
            y_pos = self.burette_y + 80 - (i * 3.2)
            self.pen.penup()
            self.pen.goto(self.burette_x + 25, y_pos)
            self.pen.color("black")
            self.pen.write(f"{i}mL", font=("Arial", 8))

    def draw_beaker(self):
        """Draw beaker with solution"""
       
        self.pen.penup()
        self.pen.goto(self.beaker_x - 60, self.beaker_y + 80)
        self.pen.pendown()
        self.pen.color("black")
        self.pen.width(3)
        
       
        self.pen.setheading(270)
        self.pen.forward(120)
        self.pen.circle(20, 180)
        self.pen.forward(120)
        
       
        self.pen.penup()
        self.pen.goto(self.beaker_x + 60, self.beaker_y + 60)
        self.pen.pendown()
        self.pen.setheading(45)
        self.pen.forward(20)
        
       
        ph_int = max(1, min(14, int(self.current_ph)))
        solution_color = self.ph_colors.get(ph_int, "#FF0000")
        
        self.pen.penup()
        self.pen.goto(self.beaker_x - 55, self.beaker_y + 75)
        self.pen.pendown()
        self.pen.color(solution_color)
        self.pen.begin_fill()
        self.pen.setheading(270)
        self.pen.forward(110)
        self.pen.circle(15, 180)
        self.pen.forward(110)
        self.pen.left(90)
        self.pen.forward(110)
        self.pen.end_fill()
        
       
        if self.volume_added > 0:
            self.draw_bubbles()

    def draw_bubbles(self):
        """Draw animated bubbles in the solution"""
        self.pen.width(1)
        for i in range(5):
            x = self.beaker_x + random.randint(-40, 40)
            y = self.beaker_y + random.randint(-40, 40)
            self.pen.penup()
            self.pen.goto(x, y)
            self.pen.pendown()
            self.pen.color("white")
            self.pen.circle(random.randint(2, 5))

    def draw_ph_meter(self):
        """Draw digital pH meter"""
       
        self.pen.penup()
        self.pen.goto(-400, 100)
        self.pen.pendown()
        self.pen.color("black")
        self.pen.width(2)
        
        
        for _ in range(2):
            self.pen.forward(120)
            self.pen.left(90)
            self.pen.forward(60)
            self.pen.left(90)
        
        
        self.pen.penup()
        self.pen.goto(-390, 120)
        self.pen.color("green")
        self.pen.write("pH METER", font=("Arial", 10, "bold"))
        
        self.pen.goto(-380, 105)
        self.pen.color("red")
        self.pen.write(f"pH: {self.current_ph:.2f}", font=("Arial", 14, "bold"))

    def draw_ph_curve(self):
        """Draw real-time pH curve"""
        if len(self.ph_data) < 2:
            return
            
       
        self.pen.penup()
        self.pen.goto(-400, -50)
        self.pen.pendown()
        self.pen.color("black")
        self.pen.width(2)
        
        
        self.pen.setheading(90)
        self.pen.forward(200)
        
        
        self.pen.penup()
        self.pen.goto(-400, -50)
        self.pen.pendown()
        self.pen.setheading(0)
        self.pen.forward(200)
        
       
        self.pen.penup()
        self.pen.goto(-420, 150)
        self.pen.write("pH", font=("Arial", 10))
        self.pen.goto(-150, -70)
        self.pen.write("Volume (mL)", font=("Arial", 10))
        
        
        if len(self.ph_data) > 1:
            self.pen.penup()
            self.pen.goto(-400, -50 + (self.ph_data[0] * 10))
            self.pen.pendown()
            self.pen.color("blue")
            self.pen.width(2)
            
            for i in range(1, len(self.ph_data)):
                x = -400 + (self.volume_data[i] * 4)
                y = -50 + (self.ph_data[i] * 10)
                self.pen.goto(x, y)

    def calculate_ph(self, volume_titrant):
        """Calculate pH based on titration type and volume"""
        if not self.selected_titration:
            return 7.0
            
        titration = self.titration_types[self.selected_titration]
        
       
        if volume_titrant == 0:
            return 1.0
        
        
        equiv_point = 25.0  
        
        if volume_titrant < equiv_point:
            
            fraction = volume_titrant / equiv_point
            ph = 1.0 + (titration["endpoint"] - 1.0) * (fraction ** 0.5)
        elif volume_titrant == equiv_point:
            
            ph = titration["endpoint"]
        else:
           
            excess = volume_titrant - equiv_point
            ph = titration["endpoint"] + math.log10(1 + excess/10)
        
        return min(14, max(0, ph))

    def animate_drop(self):
        """Animate a drop falling from burette to beaker"""
        
        drop_x = self.burette_x
        drop_y = self.burette_y - 120
        
        for y in range(int(drop_y), self.beaker_y + 60, -5):
            self.pen.penup()
            self.pen.goto(drop_x, y)
            self.pen.pendown()
            self.pen.color("lightblue")
            self.pen.circle(3)
            self.screen.update()
            time.sleep(0.02)
            
          
            self.pen.penup()
            self.pen.goto(drop_x, y)
            self.pen.pendown()
            self.pen.color("lightgray")
            self.pen.circle(3)

    def show_endpoint_effect(self):
        """Show special effects when endpoint is reached"""
        if not self.endpoint_reached:
            return
            
        
        for _ in range(3):
            self.pen.penup()
            self.pen.goto(0, 0)
            self.pen.pendown()
            self.pen.color("yellow")
            self.pen.circle(100)
            self.screen.update()
            time.sleep(0.1)
            
            self.pen.color("lightgray")
            self.pen.circle(100)
            self.screen.update()
            time.sleep(0.1)
        
       
        self.pen.penup()
        self.pen.goto(-100, 0)
        self.pen.color("red")
        self.pen.write("ENDPOINT REACHED!", font=("Arial", 20, "bold"))

    def display_menu(self):
        """Display titration selection menu"""
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(-300, 200)
        self.pen.color("darkblue")
        self.pen.write("🧪 SELECT TITRATION TYPE", font=("Arial", 18, "bold"))
        
        y_pos = 150
        for key, value in self.titration_types.items():
            self.pen.goto(-300, y_pos)
            self.pen.color("black")
            self.pen.write(f"{key}. {value['name']}", font=("Arial", 12))
            self.pen.goto(-280, y_pos - 15)
            self.pen.write(f"   {value['acid']} + {value['base']}", font=("Arial", 10, "italic"))
            y_pos -= 40
        
        self.pen.goto(-300, 0)
        self.pen.color("purple")
        self.pen.write("Enter choice (1-4): ", font=("Arial", 14))

    def display_controls(self):
        """Display control instructions"""
        self.pen.penup()
        self.pen.goto(250, 200)
        self.pen.color("darkgreen")
        self.pen.write("🎛️ CONTROLS", font=("Arial", 14, "bold"))
        
        controls = [
            "SPACE - Add titrant",
            "R - Reset experiment",
            "Q - Quit",
            "↑/↓ - Change titrant rate"
        ]
        
        y_pos = 170
        for control in controls:
            self.pen.goto(250, y_pos)
            self.pen.color("black")
            self.pen.write(control, font=("Arial", 10))
            y_pos -= 20

    def display_info(self):
        """Display current experiment info"""
        if not self.selected_titration:
            return
            
        titration = self.titration_types[self.selected_titration]
        
        self.pen.penup()
        self.pen.goto(250, 50)
        self.pen.color("darkred")
        self.pen.write("📊 EXPERIMENT INFO", font=("Arial", 12, "bold"))
        
        info = [
            f"Titration: {titration['name']}",
            f"Acid: {titration['acid']}",
            f"Base: {titration['base']}",
            f"Volume added: {self.volume_added:.1f} mL",
            f"Rate: {self.titrant_rate:.1f} mL/s",
            f"Expected endpoint: pH {titration['endpoint']}"
        ]
        
        y_pos = 20
        for item in info:
            self.pen.goto(250, y_pos)
            self.pen.color("black")
            self.pen.write(item, font=("Arial", 9))
            y_pos -= 15

    def add_titrant(self):
        """Add titrant and update simulation"""
        if self.volume_added >= self.max_volume:
            return
            
        self.volume_added += self.titrant_rate
        self.current_ph = self.calculate_ph(self.volume_added)
        
        
        self.ph_data.append(self.current_ph)
        self.volume_data.append(self.volume_added)
        
        
        titration = self.titration_types[self.selected_titration]
        if abs(self.current_ph - titration["endpoint"]) < 0.2:
            self.endpoint_reached = True
        
        
        self.animate_drop()

    def reset_experiment(self):
        """Reset the experiment"""
        self.volume_added = 0.0
        self.current_ph = 1.0
        self.ph_data = []
        self.volume_data = []
        self.endpoint_reached = False

    def update_display(self):
        """Update the entire display"""
        self.pen.clear()
        self.draw_title()
        self.draw_burette()
        self.draw_beaker()
        self.draw_ph_meter()
        self.draw_ph_curve()
        self.display_controls()
        self.display_info()
        
        if self.endpoint_reached:
            self.show_endpoint_effect()
        
        self.screen.update()

    def on_key_space(self):
        """Handle spacebar press"""
        if self.selected_titration:
            self.add_titrant()
            self.update_display()

    def on_key_r(self):
        """Handle reset key"""
        self.reset_experiment()
        self.update_display()

    def on_key_up(self):
        """Increase titrant rate"""
        self.titrant_rate = min(2.0, self.titrant_rate + 0.1)
        self.update_display()

    def on_key_down(self):
        """Decrease titrant rate"""
        self.titrant_rate = max(0.1, self.titrant_rate - 0.1)
        self.update_display()

    def on_key_q(self):
        """Quit the program"""
        self.screen.bye()

    def setup_controls(self):
        """Setup keyboard controls"""
        self.screen.onkey(self.on_key_space, "space")
        self.screen.onkey(self.on_key_r, "r")
        self.screen.onkey(self.on_key_up, "Up")
        self.screen.onkey(self.on_key_down, "Down")
        self.screen.onkey(self.on_key_q, "q")
        self.screen.listen()

    def run(self):
        """Main program loop"""
        self.screen.tracer(0)
        
        
        self.display_menu()
        self.screen.update()
        
        choice = self.screen.textinput("Titration Selection", "Enter choice (1-4):")
        
        if choice in self.titration_types:
            self.selected_titration = choice
            self.setup_controls()
            self.update_display()
            
            
            self.pen.penup()
            self.pen.goto(-200, -300)
            self.pen.color("blue")
            self.pen.write("Press SPACE to add titrant, R to reset, Q to quit", 
                         font=("Arial", 12, "bold"))
            self.screen.update()
            
            
            self.screen.mainloop()
        else:
            print("Invalid choice. Please run the program again.")
            self.screen.bye()


if __name__ == "__main__":
    print("🧪 Starting Virtual Chemistry Lab...")
    print("This program simulates acid-base titrations with visual effects!")
    print("Choose your titration type and watch the magic happen!")
    
    lab = ChemistryLab()
    lab.run()
