import tkinter as tk
from tkinter import ttk, messagebox
import turtle
import math
import random

class WorldLanguagesMap:
    def __init__(self, root):
        self.root = root
        self.root.title("🗺️ 3D World Languages Map")
        self.root.geometry("1400x900")
        
        # 3D projection parameters
        self.rotation_x = 0
        self.rotation_y = 0
        self.zoom = 200
        
        # Language data for different regions
        self.language_data = {
            "North America": {
                "languages": ["English", "Spanish", "French", "Indigenous Languages"],
                "hello_translations": {
                    "English": "Hello",
                    "Spanish": "Hola", 
                    "French": "Bonjour",
                    "Indigenous Languages": "Boozhoo (Ojibwe)"
                },
                "speakers": {
                    "English": "370 million",
                    "Spanish": "50 million",
                    "French": "10 million", 
                    "Indigenous Languages": "2 million"
                },
                "color": "red",
                "3d_pos": (-0.5, 0.3, 0.4)
            },
            "South America": {
                "languages": ["Spanish", "Portuguese", "English", "Indigenous Languages"],
                "hello_translations": {
                    "Spanish": "Hola",
                    "Portuguese": "Olá",
                    "English": "Hello",
                    "Indigenous Languages": "Kamisaraki (Quechua)"
                },
                "speakers": {
                    "Spanish": "210 million",
                    "Portuguese": "220 million",
                    "English": "5 million",
                    "Indigenous Languages": "10 million"
                },
                "color": "green",
                "3d_pos": (-0.3, -0.5, 0.2)
            },
            "Europe": {
                "languages": ["English", "German", "French", "Spanish", "Italian", "Russian"],
                "hello_translations": {
                    "English": "Hello",
                    "German": "Hallo",
                    "French": "Bonjour",
                    "Spanish": "Hola",
                    "Italian": "Ciao",
                    "Russian": "Привет (Privet)"
                },
                "speakers": {
                    "English": "70 million",
                    "German": "100 million",
                    "French": "80 million",
                    "Spanish": "50 million",
                    "Italian": "65 million",
                    "Russian": "150 million"
                },
                "color": "blue",
                "3d_pos": (0.2, 0.6, 0.4)
            },
            "Africa": {
                "languages": ["Arabic", "Swahili", "English", "French", "Portuguese", "Hausa"],
                "hello_translations": {
                    "Arabic": "مرحبا (Marhaba)",
                    "Swahili": "Hujambo",
                    "English": "Hello",
                    "French": "Bonjour",
                    "Portuguese": "Olá",
                    "Hausa": "Sannu"
                },
                "speakers": {
                    "Arabic": "200 million",
                    "Swahili": "100 million",
                    "English": "200 million",
                    "French": "120 million",
                    "Portuguese": "20 million",
                    "Hausa": "70 million"
                },
                "color": "orange",
                "3d_pos": (0.3, 0.1, 0.1)
            },
            "Asia": {
                "languages": ["Chinese", "Hindi", "English", "Arabic", "Japanese", "Korean"],
                "hello_translations": {
                    "Chinese": "你好 (Nǐ hǎo)",
                    "Hindi": "नमस्ते (Namaste)",
                    "English": "Hello",
                    "Arabic": "مرحبا (Marhaba)",
                    "Japanese": "こんにちは (Konnichiwa)",
                    "Korean": "안녕하세요 (Annyeonghaseyo)"
                },
                "speakers": {
                    "Chinese": "1.3 billion",
                    "Hindi": "600 million",
                    "English": "400 million",
                    "Arabic": "400 million",
                    "Japanese": "125 million",
                    "Korean": "77 million"
                },
                "color": "purple",
                "3d_pos": (0.6, 0.4, 0.3)
            },
            "Australia/Oceania": {
                "languages": ["English", "Tok Pisin", "Fijian", "Samoan", "Indigenous Languages"],
                "hello_translations": {
                    "English": "Hello",
                    "Tok Pisin": "Gude",
                    "Fijian": "Bula",
                    "Samoan": "Talofa",
                    "Indigenous Languages": "Palya (Pitjantjatjara)"
                },
                "speakers": {
                    "English": "25 million",
                    "Tok Pisin": "5 million",
                    "Fijian": "350,000",
                    "Samoan": "500,000",
                    "Indigenous Languages": "150,000"
                },
                "color": "brown",
                "3d_pos": (0.7, -0.4, -0.2)
            }
        }
        
        # Test questions for the quiz
        self.test_questions = []
        self.setup_test_questions()
        
        # Projected points for click detection
        self.projected_regions = {}
        
        self.setup_ui()
        
    def setup_test_questions(self):
        """Prepare test questions from all regions"""
        for region, data in self.language_data.items():
            for lang, hello in data["hello_translations"].items():
                self.test_questions.append({
                    "language": lang,
                    "hello": hello,
                    "region": region
                })
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="🗺️ 3D World Languages Map", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=5)
        
        # Instructions
        instructions = ttk.Label(main_frame, 
                                text="Click on any region of the 3D globe to explore languages! Use controls to rotate.",
                                font=("Arial", 10))
        instructions.pack(pady=5)
        
        # Control frame
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Rotation controls
        ttk.Label(control_frame, text="Rotate:").pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="↑", command=self.rotate_up).pack(side=tk.LEFT, padx=2)
        ttk.Button(control_frame, text="↓", command=self.rotate_down).pack(side=tk.LEFT, padx=2)
        ttk.Button(control_frame, text="←", command=self.rotate_left).pack(side=tk.LEFT, padx=2)
        ttk.Button(control_frame, text="→", command=self.rotate_right).pack(side=tk.LEFT, padx=2)
        
        # Zoom controls
        ttk.Label(control_frame, text="Zoom:").pack(side=tk.LEFT, padx=10)
        ttk.Button(control_frame, text="+", command=self.zoom_in).pack(side=tk.LEFT, padx=2)
        ttk.Button(control_frame, text="-", command=self.zoom_out).pack(side=tk.LEFT, padx=2)
        
        # Reset button
        ttk.Button(control_frame, text="Reset View", command=self.reset_view).pack(side=tk.LEFT, padx=10)
        
        # Content frame
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas for turtle graphics
        self.canvas = tk.Canvas(content_frame, bg="black", width=800, height=600)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Setup turtle
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("black")
        self.screen.setworldcoordinates(-400, -300, 400, 300)
        
        # Create turtle for drawing
        self.globe_turtle = turtle.RawTurtle(self.screen)
        self.globe_turtle.speed(0)
        self.globe_turtle.hideturtle()
        
        # Right panel for information
        right_panel = ttk.Frame(content_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=10)
        
        # Language info display
        self.info_frame = ttk.LabelFrame(right_panel, text="Language Information", 
                                        padding=10)
        self.info_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.info_text = tk.Text(self.info_frame, height=20, width=35, wrap=tk.WORD,
                                font=("Arial", 10))
        self.info_text.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar for info text
        scrollbar = ttk.Scrollbar(self.info_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_text.config(yscrollcommand=scrollbar.set)
        
        # Language selector
        selector_frame = ttk.LabelFrame(right_panel, text="Explore Regions", padding=10)
        selector_frame.pack(fill=tk.X, pady=5)
        
        self.region_var = tk.StringVar()
        self.region_combo = ttk.Combobox(selector_frame, textvariable=self.region_var,
                                        values=list(self.language_data.keys()),
                                        state="readonly")
        self.region_combo.pack(fill=tk.X, pady=5)
        self.region_combo.bind('<<ComboboxSelected>>', self.on_region_select)
        
        # Test yourself button
        test_button = ttk.Button(selector_frame, text="🎯 Test Yourself!", 
                                command=self.start_language_test)
        test_button.pack(fill=tk.X, pady=5)
        
        # Auto-rotate button
        self.auto_rotate_var = tk.BooleanVar()
        auto_rotate_check = ttk.Checkbutton(selector_frame, text="Auto Rotate", 
                                           variable=self.auto_rotate_var,
                                           command=self.toggle_auto_rotate)
        auto_rotate_check.pack(fill=tk.X, pady=5)
        
        # Bind click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Show initial information
        self.show_welcome_info()
        
        # Draw initial globe
        self.draw_3d_globe()
        
        # Start auto-rotation if enabled
        self.auto_rotate_job = None
        
    def project_3d_to_2d(self, x, y, z):
        """Convert 3D coordinates to 2D screen coordinates"""
        # Apply rotations
        cos_x, sin_x = math.cos(self.rotation_x), math.sin(self.rotation_x)
        cos_y, sin_y = math.cos(self.rotation_y), math.sin(self.rotation_y)
        
        # Rotate around Y axis
        x_rot = x * cos_y - z * sin_y
        z_rot = x * sin_y + z * cos_y
        
        # Rotate around X axis
        y_rot = y * cos_x - z_rot * sin_x
        z_final = y * sin_x + z_rot * cos_x
        
        # Apply perspective projection
        distance = 3
        if z_final > -distance:
            screen_x = (x_rot * self.zoom) / (distance + z_final)
            screen_y = (y_rot * self.zoom) / (distance + z_final)
        else:
            screen_x = x_rot * self.zoom
            screen_y = y_rot * self.zoom
        
        return screen_x, screen_y, z_final
    
    def draw_3d_globe(self):
        """Draw the 3D globe with regions"""
        self.globe_turtle.clear()
        self.projected_regions.clear()
        
        # Draw wireframe sphere
        self.draw_wireframe_sphere()
        
        # Draw regions
        for region, data in self.language_data.items():
            x, y, z = data["3d_pos"]
            screen_x, screen_y, depth = self.project_3d_to_2d(x, y, z)
            
            # Only draw if facing towards viewer
            if depth > -2:
                self.globe_turtle.penup()
                self.globe_turtle.goto(screen_x, screen_y)
                self.globe_turtle.pendown()
                
                # Draw region marker
                self.globe_turtle.color(data["color"])
                self.globe_turtle.begin_fill()
                self.globe_turtle.circle(15)
                self.globe_turtle.end_fill()
                
                # Add region label
                self.globe_turtle.penup()
                self.globe_turtle.goto(screen_x + 20, screen_y + 10)
                self.globe_turtle.color("white")
                self.globe_turtle.write(region, font=("Arial", 8, "normal"))
                
                # Store projected position for click detection
                self.projected_regions[region] = (screen_x, screen_y, 15)
    
    def draw_wireframe_sphere(self):
        """Draw wireframe lines for the sphere"""
        self.globe_turtle.color("darkgray")
        self.globe_turtle.width(1)
        
        # Draw latitude lines
        for lat in range(-60, 90, 30):
            self.globe_turtle.penup()
            points = []
            for lng in range(0, 360, 10):
                x = math.cos(math.radians(lat)) * math.cos(math.radians(lng))
                y = math.sin(math.radians(lat))
                z = math.cos(math.radians(lat)) * math.sin(math.radians(lng))
                
                screen_x, screen_y, depth = self.project_3d_to_2d(x, y, z)
                points.append((screen_x, screen_y, depth))
            
            # Draw the line
            first_point = True
            for screen_x, screen_y, depth in points:
                if depth > -2:  # Only draw visible parts
                    if first_point:
                        self.globe_turtle.penup()
                        self.globe_turtle.goto(screen_x, screen_y)
                        self.globe_turtle.pendown()
                        first_point = False
                    else:
                        self.globe_turtle.goto(screen_x, screen_y)
                else:
                    first_point = True
        
        # Draw longitude lines
        for lng in range(0, 180, 30):
            self.globe_turtle.penup()
            points = []
            for lat in range(-90, 90, 10):
                x = math.cos(math.radians(lat)) * math.cos(math.radians(lng))
                y = math.sin(math.radians(lat))
                z = math.cos(math.radians(lat)) * math.sin(math.radians(lng))
                
                screen_x, screen_y, depth = self.project_3d_to_2d(x, y, z)
                points.append((screen_x, screen_y, depth))
            
            # Draw the line
            first_point = True
            for screen_x, screen_y, depth in points:
                if depth > -2:  # Only draw visible parts
                    if first_point:
                        self.globe_turtle.penup()
                        self.globe_turtle.goto(screen_x, screen_y)
                        self.globe_turtle.pendown()
                        first_point = False
                    else:
                        self.globe_turtle.goto(screen_x, screen_y)
                else:
                    first_point = True
    
    def on_canvas_click(self, event):
        """Handle clicks on the canvas"""
        # Convert click coordinates to turtle coordinates
        click_x = event.x - self.canvas.winfo_width() / 2
        click_y = self.canvas.winfo_height() / 2 - event.y
        
        # Check if click is near any region
        for region, (x, y, radius) in self.projected_regions.items():
            distance = math.sqrt((click_x - x)**2 + (click_y - y)**2)
            if distance <= radius + 10:  # Add some tolerance
                self.show_region_info(region)
                break
    
    def rotate_up(self):
        self.rotation_x += 0.3
        self.draw_3d_globe()
    
    def rotate_down(self):
        self.rotation_x -= 0.3
        self.draw_3d_globe()
    
    def rotate_left(self):
        self.rotation_y -= 0.3
        self.draw_3d_globe()
    
    def rotate_right(self):
        self.rotation_y += 0.3
        self.draw_3d_globe()
    
    def zoom_in(self):
        self.zoom += 20
        self.draw_3d_globe()
    
    def zoom_out(self):
        self.zoom = max(50, self.zoom - 20)
        self.draw_3d_globe()
    
    def reset_view(self):
        self.rotation_x = 0
        self.rotation_y = 0
        self.zoom = 200
        self.draw_3d_globe()
    
    def toggle_auto_rotate(self):
        if self.auto_rotate_var.get():
            self.start_auto_rotate()
        else:
            self.stop_auto_rotate()
    
    def start_auto_rotate(self):
        def auto_rotate():
            if self.auto_rotate_var.get():
                self.rotation_y += 0.1
                self.draw_3d_globe()
                self.auto_rotate_job = self.root.after(100, auto_rotate)
        
        self.auto_rotate_job = self.root.after(100, auto_rotate)
    
    def stop_auto_rotate(self):
        if self.auto_rotate_job:
            self.root.after_cancel(self.auto_rotate_job)
            self.auto_rotate_job = None
    
    def on_region_select(self, event):
        """Handle region selection from dropdown"""
        region = self.region_var.get()
        if region:
            self.show_region_info(region)
    
    def show_region_info(self, region):
        """Display information about selected region"""
        self.info_text.delete(1.0, tk.END)
        
        if region in self.language_data:
            data = self.language_data[region]
            
            info = f"🌍 {region}\n"
            info += "="*40 + "\n\n"
            
            info += "🗣️ LANGUAGES SPOKEN:\n"
            for i, lang in enumerate(data["languages"], 1):
                info += f"{i}. {lang}\n"
            
            info += "\n👋 HOW TO SAY 'HELLO':\n"
            for lang, hello in data["hello_translations"].items():
                info += f"• {lang}: {hello}\n"
            
            info += "\n📊 NATIVE SPEAKERS:\n"
            for lang, count in data["speakers"].items():
                info += f"• {lang}: {count} speakers\n"
            
            info += f"\n🎨 Region Color: {data['color'].title()}\n"
            info += f"📍 3D Position: {data['3d_pos']}\n"
            
            self.info_text.insert(tk.END, info)
    
    def show_welcome_info(self):
        """Show welcome information"""
        welcome = """🌍 Welcome to the 3D World Languages Map!

This interactive globe shows languages spoken around the world using Python's turtle graphics.

🎮 HOW TO USE:
• Click on colored regions on the 3D globe
• Use rotation buttons (↑↓←→) to rotate the globe
• Use zoom buttons (+/-) to zoom in/out
• Use the dropdown to select regions directly
• Enable "Auto Rotate" for continuous rotation
• Click 'Test Yourself' for a fun language quiz!

✨ FEATURES:
• Real 3D wireframe globe with perspective
• Interactive rotation and zoom controls
• Languages from all 6 continents
• "Hello" translations in native scripts
• Native speaker statistics
• 10-question language learning quiz
• Auto-rotation mode

🗺️ REGIONS COVERED:
• North America (Red)
• South America (Green)  
• Europe (Blue)
• Africa (Orange)
• Asia (Purple)
• Australia/Oceania (Brown)

Click on any colored region dot to start exploring languages from that part of the world!

🎯 Try the quiz to test your knowledge of world greetings!"""
        
        self.info_text.insert(tk.END, welcome)
    
    def start_language_test(self):
        """Start the language learning test"""
        if not self.test_questions:
            messagebox.showwarning("No Data", "No test questions available!")
            return
        
        # Create test window
        test_window = tk.Toplevel(self.root)
        test_window.title("🎯 Language Test - Say Hello Around the World!")
        test_window.geometry("600x500")
        test_window.configure(bg="#f0f0f0")
        
        # Test variables
        self.current_question = 0
        self.score = 0
        self.selected_questions = random.sample(self.test_questions, 
                                               min(10, len(self.test_questions)))
        
        # Test UI
        test_frame = ttk.Frame(test_window, padding=20)
        test_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(test_frame, text="🎯 World Languages Quiz", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Question counter
        self.question_label = ttk.Label(test_frame, text="", font=("Arial", 12, "bold"))
        self.question_label.pack(pady=5)
        
        # Question text
        self.question_text = ttk.Label(test_frame, text="", font=("Arial", 14),
                                      wraplength=500)
        self.question_text.pack(pady=15)
        
        # Answer frame
        answer_frame = ttk.Frame(test_frame)
        answer_frame.pack(pady=10)
        
        ttk.Label(answer_frame, text="Your answer:", font=("Arial", 12)).pack(pady=5)
        self.answer_var = tk.StringVar()
        self.answer_entry = ttk.Entry(answer_frame, textvariable=self.answer_var, 
                                     font=("Arial", 12), width=30)
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # Buttons
        button_frame = ttk.Frame(test_frame)
        button_frame.pack(pady=20)
        
        self.check_button = ttk.Button(button_frame, text="✓ Check Answer", 
                                      command=self.check_answer)
        self.check_button.pack(side=tk.LEFT, padx=10)
        
        self.next_button = ttk.Button(button_frame, text="Next Question →", 
                                     command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        # Result label
        self.result_label = ttk.Label(test_frame, text="", font=("Arial", 12),
                                     wraplength=500)
        self.result_label.pack(pady=15)
        
        # Score label
        self.score_label = ttk.Label(test_frame, text=f"Score: {self.score}/10", 
                                    font=("Arial", 14, "bold"))
        self.score_label.pack(pady=10)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(test_frame, variable=self.progress_var,
                                           maximum=10, length=400)
        self.progress_bar.pack(pady=10)
        
        # Store test window reference
        self.test_window = test_window
        
        # Start first question
        self.show_question()
    
    def show_question(self):
        """Show current test question"""
        if self.current_question >= len(self.selected_questions):
            self.show_final_score()
            return
        
        question = self.selected_questions[self.current_question]
        
        self.question_label.config(text=f"Question {self.current_question + 1} of 10")
        self.question_text.config(text=f"How do you say 'Hello' in {question['language']}?\n"
                                      f"(From {question['region']})")
        
        self.answer_var.set("")
        self.answer_entry.focus()
        self.result_label.config(text="", foreground="black")
        
        self.check_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        
        # Update progress bar
        self.progress_var.set(self.current_question)
    
    def check_answer(self):
        """Check the user's answer"""
        question = self.selected_questions[self.current_question]
        user_answer = self.answer_var.get().strip().lower()
        correct_answer = question['hello'].lower()
        
        # Extract main word from parentheses for better matching
        correct_main = correct_answer.split('(')[0].strip()
        
        # Check if answer is correct (flexible matching)
        is_correct = (user_answer in correct_answer or 
                     correct_main in user_answer or
                     user_answer in correct_main)
        
        if is_correct:
            self.result_label.config(text="✅ Correct! Well done!", foreground="green")
            self.score += 1
        else:
            self.result_label.config(text=f"❌ Incorrect.\n"
                                         f"Correct answer: {question['hello']}\n"
                                         f"Region: {question['region']}", 
                                   foreground="red")
        
        self.score_label.config(text=f"Score: {self.score}/10")
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.next_button.focus()
    
    def next_question(self):
        """Move to next question"""
        self.current_question += 1
        self.show_question()
    
    def show_final_score(self):
        """Show final test results"""
        percentage = (self.score / 10) * 100
        
        if percentage >= 80:
            grade = "🏆 Outstanding! You're a world languages expert!"
        elif percentage >= 60:
            grade = "👍 Great job! You know your way around the world!"
        elif percentage >= 40:
            grade = "📚 Good effort! Keep exploring to learn more!"
        else:
            grade = "🌍 Keep practicing! There's a whole world to discover!"
        
        result_text = f"""🎯 QUIZ COMPLETE!

Final Score: {self.score}/10 ({percentage:.0f}%)

{grade}

You've explored greetings from across the globe!
Each language represents the rich culture and 
history of its people.

Continue exploring the 3D map to discover 
more fascinating languages and cultures!"""
        
        self.question_label.config(text="Quiz Complete!")
        self.question_text.config(text="")
        self.result_label.config(text=result_text, foreground="blue")
        self.answer_entry.config(state=tk.DISABLED)
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.progress_var.set(10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WorldLanguagesMap(root)
    root.mainloop()
