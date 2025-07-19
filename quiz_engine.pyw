import tkinter as tk
from tkinter import ttk, messagebox
import turtle
import random
import time
import math

class QuizEngine:
    def __init__(self):
        # Initialize main window
        self.root = tk.Tk()
        self.root.title("🎮 Adventure Quiz Engine")
        self.root.geometry("800x600")
        self.root.configure(bg='#1a1a2e')
        
        # Game state
        self.current_question = "start"
        self.score = 0
        self.path_history = []
        self.player_name = ""
        
        # Colors
        self.colors = {
            'bg': '#1a1a2e',
            'secondary': '#16213e',
            'accent': '#0f3460',
            'primary': '#e94560',
            'success': '#00ff88',
            'warning': '#ffd700',
            'text': '#ffffff'
        }
        
        # Quiz questions with branching logic
        self.questions = {
            "start": {
                "question": "🚀 Welcome to the Space Adventure Quiz! What's your exploration style?",
                "options": [
                    ("🛡️ Cautious Explorer", "safety_first"),
                    ("⚡ Bold Adventurer", "risk_taker"),
                    ("🧠 Scientific Researcher", "knowledge_seeker")
                ],
                "visual": "rocket"
            },
            "safety_first": {
                "question": "🛡️ You discover a strange alien artifact. What do you do?",
                "options": [
                    ("📊 Scan it thoroughly first", "science_path"),
                    ("🤝 Try to communicate with it", "diplomacy_path"),
                    ("🏃 Keep safe distance and observe", "observer_path")
                ],
                "visual": "artifact"
            },
            "risk_taker": {
                "question": "⚡ You encounter a black hole! Your ship can handle it, but it's dangerous. What's your move?",
                "options": [
                    ("🌀 Dive in for the ultimate adventure!", "black_hole_dive"),
                    ("🔬 Study it from a safe distance", "science_path"),
                    ("🚀 Use it as a gravity slingshot", "slingshot_path")
                ],
                "visual": "black_hole"
            },
            "knowledge_seeker": {
                "question": "🧠 You find an ancient alien library. How do you approach it?",
                "options": [
                    ("📚 Systematically catalog everything", "scholar_ending"),
                    ("🔍 Focus on the most mysterious texts", "mystery_path"),
                    ("🤖 Use AI to translate everything", "tech_path")
                ],
                "visual": "library"
            },
            "science_path": {
                "question": "🔬 Your scientific analysis reveals the artifact is a key to an ancient civilization. What next?",
                "options": [
                    ("🏛️ Seek out the civilization", "ancient_civ"),
                    ("🔑 Try to activate the key", "activation_path"),
                    ("📡 Share discovery with Earth", "fame_ending")
                ],
                "visual": "key"
            },
            "diplomacy_path": {
                "question": "🤝 The artifact responds to your peaceful intentions! It's actually a communication device. What do you say?",
                "options": [
                    ("👋 'Greetings, we come in peace'", "peace_ending"),
                    ("🤔 'We seek knowledge and friendship'", "alliance_ending"),
                    ("🌍 'We represent Earth'", "ambassador_ending")
                ],
                "visual": "communication"
            },
            "mystery_path": {
                "question": "🔍 The mysterious texts reveal a prophecy about a chosen explorer. You realize it describes you! What's your response?",
                "options": [
                    ("👑 Embrace your destiny", "destiny_ending"),
                    ("🤔 Question the prophecy's validity", "skeptic_ending"),
                    ("🏃 Run from the responsibility", "escape_ending")
                ],
                "visual": "prophecy"
            }
        }
        
        # Initialize turtle graphics
        self.setup_turtle()
        
        # Start the game
        self.create_main_interface()
        
    def setup_turtle(self):
        """Set up turtle graphics for visual effects"""
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg='#0a0a1a')
        self.canvas.pack(pady=10)
        
        # Create turtle screen
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor('#0a0a1a')
       
        
        # Create turtle
        self.artist = turtle.RawTurtle(self.screen)
        self.artist.speed(0)
        self.artist.pensize(3)
        
    def create_main_interface(self):
        """Create the main quiz interface"""
        # Title
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="🎮 Adventure Quiz Engine",
            font=('Arial', 24, 'bold'),
            fg=self.colors['primary'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        # Player name input
        name_frame = tk.Frame(self.root, bg=self.colors['bg'])
        name_frame.pack(pady=5)
        
        tk.Label(
            name_frame,
            text="Enter your name, brave explorer:",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack()
        
        self.name_entry = tk.Entry(
            name_frame,
            font=('Arial', 12),
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        self.name_entry.pack(pady=5)
        
        # Start button
        start_btn = tk.Button(
            self.root,
            text="🚀 Begin Adventure",
            font=('Arial', 14, 'bold'),
            bg=self.colors['primary'],
            fg=self.colors['text'],
            command=self.start_quiz,
            padx=20,
            pady=10
        )
        start_btn.pack(pady=10)
        
        # Score display
        self.score_label = tk.Label(
            self.root,
            text="Score: 0 ⭐",
            font=('Arial', 12, 'bold'),
            fg=self.colors['success'],
            bg=self.colors['bg']
        )
        self.score_label.pack()
        
        # Question area
        self.question_frame = tk.Frame(self.root, bg=self.colors['secondary'])
        self.question_frame.pack(pady=10, padx=20, fill='x')
        
        # Options frame
        self.options_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.options_frame.pack(pady=10)
        
        # Draw initial visual
        self.draw_visual("start_screen")
        
    def start_quiz(self):
        """Start the quiz game"""
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Name Required", "Please enter your name first!")
            return
        
        self.player_name = name
        self.show_question("start")
        
    def show_question(self, question_id):
        """Display a question with its options"""
        if question_id not in self.questions:
            self.show_ending(question_id)
            return
            
        question_data = self.questions[question_id]
        self.current_question = question_id
        
        # Clear previous question
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Display question
        question_label = tk.Label(
            self.question_frame,
            text=question_data["question"],
            font=('Arial', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['secondary'],
            wraplength=600,
            justify='center'
        )
        question_label.pack(pady=20)
        
        # Display options
        for i, (option_text, next_question) in enumerate(question_data["options"]):
            btn = tk.Button(
                self.options_frame,
                text=option_text,
                font=('Arial', 12),
                bg=self.colors['accent'],
                fg=self.colors['text'],
                command=lambda nq=next_question: self.select_option(nq),
                padx=15,
                pady=8,
                width=30
            )
            btn.pack(pady=5)
            
            # Add hover effects
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.colors['primary']))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.colors['accent']))
        
        # Draw visual for this question
        self.draw_visual(question_data["visual"])
        
    def select_option(self, next_question):
        """Handle option selection"""
        self.score += 10
        self.score_label.config(text=f"Score: {self.score} ⭐")
        self.path_history.append(self.current_question)
        
        # Add some visual feedback
        self.create_particle_effect()
        
        # Move to next question after a brief delay
        self.root.after(500, lambda: self.show_question(next_question))
        
    def show_ending(self, ending_id):
        """Show the ending based on the path taken"""
        endings = {
            "peace_ending": {
                "title": "🕊️ Peaceful Ambassador",
                "message": f"Congratulations {self.player_name}! You've established peaceful contact with an alien civilization. Your diplomatic approach has opened doors to interstellar friendship!",
                "visual": "peace"
            },
            "alliance_ending": {
                "title": "🤝 Galactic Alliance",
                "message": f"Amazing work, {self.player_name}! You've formed a powerful alliance with an advanced civilization. Together, you'll explore the universe!",
                "visual": "alliance"
            },
            "scholar_ending": {
                "title": "📚 Master Scholar",
                "message": f"Incredible, {self.player_name}! You've become the greatest xenoarchaeologist in history. Your systematic approach has unlocked ancient secrets!",
                "visual": "scholar"
            },
            "destiny_ending": {
                "title": "👑 Chosen One",
                "message": f"Extraordinary, {self.player_name}! You've fulfilled an ancient prophecy and become the bridge between worlds. Your destiny awaits!",
                "visual": "destiny"
            },
            "fame_ending": {
                "title": "🌟 Famous Explorer",
                "message": f"Well done, {self.player_name}! Your discoveries have made you the most famous explorer in human history!",
                "visual": "fame"
            }
        }
        
        # Default ending if not found
        if ending_id not in endings:
            ending_id = "peace_ending"
        
        ending_data = endings[ending_id]
        
        # Clear interface
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Show ending
        ending_label = tk.Label(
            self.question_frame,
            text=ending_data["title"],
            font=('Arial', 18, 'bold'),
            fg=self.colors['success'],
            bg=self.colors['secondary']
        )
        ending_label.pack(pady=10)
        
        message_label = tk.Label(
            self.question_frame,
            text=ending_data["message"],
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['secondary'],
            wraplength=600,
            justify='center'
        )
        message_label.pack(pady=20)
        
        # Final score
        final_score_label = tk.Label(
            self.question_frame,
            text=f"Final Score: {self.score} ⭐",
            font=('Arial', 16, 'bold'),
            fg=self.colors['warning'],
            bg=self.colors['secondary']
        )
        final_score_label.pack(pady=10)
        
        # Restart button
        restart_btn = tk.Button(
            self.options_frame,
            text="🔄 New Adventure",
            font=('Arial', 14, 'bold'),
            bg=self.colors['primary'],
            fg=self.colors['text'],
            command=self.restart_game,
            padx=20,
            pady=10
        )
        restart_btn.pack(pady=20)
        
        # Draw ending visual
        self.draw_visual(ending_data["visual"])
        
    def draw_visual(self, visual_type):
        """Draw different visuals based on the current scene"""
        self.artist.clear()
        
        if visual_type == "start_screen":
            self.draw_start_screen()
        elif visual_type == "rocket":
            self.draw_rocket()
        elif visual_type == "artifact":
            self.draw_artifact()
        elif visual_type == "black_hole":
            self.draw_black_hole()
        elif visual_type == "library":
            self.draw_library()
        elif visual_type == "key":
            self.draw_key()
        elif visual_type == "communication":
            self.draw_communication()
        elif visual_type == "prophecy":
            self.draw_prophecy()
        elif visual_type == "peace":
            self.draw_peace()
        elif visual_type == "alliance":
            self.draw_alliance()
        elif visual_type == "scholar":
            self.draw_scholar()
        elif visual_type == "destiny":
            self.draw_destiny()
        elif visual_type == "fame":
            self.draw_fame()
        
    def draw_start_screen(self):
        """Draw the start screen"""
        # Draw stars
        for _ in range(20):
            self.artist.penup()
            self.artist.goto(random.randint(-180, 180), random.randint(-120, 120))
            self.artist.pendown()
            self.artist.color('white')
            self.artist.dot(random.randint(1, 3))
        
        # Draw title decoration
        self.artist.penup()
        self.artist.goto(0, 50)
        self.artist.pendown()
        self.artist.color('#e94560')
        self.artist.write("ADVENTURE AWAITS!", align="center", font=("Arial", 16, "bold"))
        
    def draw_rocket(self):
        """Draw a rocket ship"""
        self.artist.penup()
        self.artist.goto(0, -50)
        self.artist.pendown()
        self.artist.color('#ff6b6b')
        self.artist.begin_fill()
        self.artist.setheading(90)
        self.artist.forward(80)
        self.artist.right(45)
        self.artist.forward(20)
        self.artist.right(90)
        self.artist.forward(20)
        self.artist.right(45)
        self.artist.forward(80)
        self.artist.right(90)
        self.artist.forward(40)
        self.artist.end_fill()
        
        # Rocket flames
        self.artist.penup()
        self.artist.goto(-15, -50)
        self.artist.pendown()
        self.artist.color('#ffd700')
        self.artist.begin_fill()
        for _ in range(3):
            self.artist.forward(10)
            self.artist.right(120)
        self.artist.end_fill()
        
    def draw_artifact(self):
        """Draw an alien artifact"""
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()
        self.artist.color('#00ff88')
        
        # Draw glowing crystal
        for size in [30, 25, 20, 15]:
            self.artist.penup()
            self.artist.goto(0, 0)
            self.artist.pendown()
            self.artist.begin_fill()
            for _ in range(6):
                self.artist.forward(size)
                self.artist.right(60)
            self.artist.end_fill()
            
    def draw_black_hole(self):
        """Draw a black hole"""
        # Draw event horizon
        self.artist.penup()
        self.artist.goto(0, -40)
        self.artist.pendown()
        self.artist.color('#000000')
        self.artist.begin_fill()
        self.artist.circle(40)
        self.artist.end_fill()
        
        # Draw accretion disk
        for radius in [60, 50, 45]:
            self.artist.penup()
            self.artist.goto(0, -radius)
            self.artist.pendown()
            self.artist.color('#ff6b6b' if radius == 60 else '#ffd700')
            self.artist.circle(radius)
            
    def draw_library(self):
        """Draw an ancient library"""
        self.artist.penup()
        self.artist.goto(-80, -40)
        self.artist.pendown()
        self.artist.color('#8b4513')
        
        # Draw bookshelves
        for x in range(-80, 81, 40):
            self.artist.penup()
            self.artist.goto(x, -40)
            self.artist.pendown()
            self.artist.setheading(90)
            self.artist.forward(80)
            
        # Draw books
        colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffd93d']
        for i, x in enumerate(range(-70, 71, 20)):
            self.artist.penup()
            self.artist.goto(x, -30)
            self.artist.pendown()
            self.artist.color(colors[i % len(colors)])
            self.artist.begin_fill()
            for _ in range(4):
                self.artist.forward(15)
                self.artist.right(90)
            self.artist.end_fill()
            
    def draw_key(self):
        """Draw a glowing key"""
        self.artist.penup()
        self.artist.goto(-30, 0)
        self.artist.pendown()
        self.artist.color('#ffd700')
        self.artist.pensize(5)
        
        # Key shaft
        self.artist.forward(50)
        
        # Key head
        self.artist.penup()
        self.artist.goto(-30, 0)
        self.artist.pendown()
        self.artist.circle(15)
        
        # Key teeth
        self.artist.penup()
        self.artist.goto(20, 0)
        self.artist.pendown()
        self.artist.right(90)
        self.artist.forward(10)
        self.artist.backward(10)
        self.artist.forward(5)
        self.artist.left(90)
        self.artist.forward(10)
        
    def draw_communication(self):
        """Draw communication waves"""
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()
        self.artist.color('#00ff88')
        
        # Draw expanding circles
        for radius in [20, 30, 40, 50]:
            self.artist.penup()
            self.artist.goto(0, -radius)
            self.artist.pendown()
            self.artist.circle(radius)
            
    def draw_prophecy(self):
        """Draw ancient prophecy symbols"""
        self.artist.penup()
        self.artist.goto(0, 30)
        self.artist.pendown()
        self.artist.color('#9b59b6')
        
        # Draw mystical symbols
        symbols = ['☆', '◊', '▲', '●', '◈']
        for i, symbol in enumerate(symbols):
            angle = i * 72
            x = 40 * math.cos(math.radians(angle))
            y = 40 * math.sin(math.radians(angle))
            self.artist.penup()
            self.artist.goto(x, y)
            self.artist.pendown()
            self.artist.write(symbol, align="center", font=("Arial", 16, "bold"))
            
    def draw_peace(self):
        """Draw peace symbol"""
        self.artist.penup()
        self.artist.goto(0, 30)
        self.artist.pendown()
        self.artist.color('#00ff88')
        self.artist.write("☮", align="center", font=("Arial", 48, "bold"))
        
    def draw_alliance(self):
        """Draw alliance symbol"""
        self.artist.penup()
        self.artist.goto(0, 30)
        self.artist.pendown()
        self.artist.color('#4ecdc4')
        self.artist.write("🤝", align="center", font=("Arial", 48, "bold"))
        
    def draw_scholar(self):
        """Draw scholar symbol"""
        self.artist.penup()
        self.artist.goto(0, 30)
        self.artist.pendown()
        self.artist.color('#45b7d1')
        self.artist.write("📚", align="center", font=("Arial", 48, "bold"))
        
    def draw_destiny(self):
        """Draw destiny symbol"""
        self.artist.penup()
        self.artist.goto(0, 30)
        self.artist.pendown()
        self.artist.color('#ffd700')
        self.artist.write("👑", align="center", font=("Arial", 48, "bold"))
        
    def draw_fame(self):
        """Draw fame symbol"""
        self.artist.penup()
        self.artist.goto(0, 30)
        self.artist.pendown()
        self.artist.color('#ff6b6b')
        self.artist.write("🌟", align="center", font=("Arial", 48, "bold"))
        
    def create_particle_effect(self):
        """Create a particle effect for correct answers"""
        for _ in range(10):
            self.artist.penup()
            self.artist.goto(random.randint(-100, 100), random.randint(-50, 50))
            self.artist.pendown()
            self.artist.color(random.choice(['#ffd700', '#00ff88', '#ff6b6b', '#4ecdc4']))
            self.artist.dot(random.randint(3, 8))
            
    def restart_game(self):
        """Restart the game"""
        self.current_question = "start"
        self.score = 0
        self.path_history = []
        self.score_label.config(text="Score: 0 ⭐")
        self.show_question("start")
        
    def run(self):
        """Start the game"""
        self.root.mainloop()

# Create and run the quiz game
if __name__ == "__main__":
    game = QuizEngine()
    game.run()


# ©SOFTWARELABS
# BY - PARAS DHIMAN (Co-Founder)
# CONTACT:
#     softwarelabschd@gmail.com
