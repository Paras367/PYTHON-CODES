import tkinter as tk
from tkinter import ttk, messagebox
import math
import random
import time
import threading
from tkinter import font

class NeuralNetwork3DVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 3D Neural Network Visualizer")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        
        # Network architecture
        self.layers = [4, 6, 4, 2]  # Default architecture
        self.weights = []
        self.biases = []
        self.activations = []
        self.is_animating = False
        
        # 3D visualization parameters
        self.depth_scale = 0.6
        self.rotation_x = 0
        self.rotation_y = 0
        self.zoom = 1.0
        self.center_x = 400
        self.center_y = 300
        
        # Animation parameters
        self.animation_speed = 0.1
        self.pulse_time = 0
        self.current_layer = 0
        
        # Colors and styling
        self.colors = {
            'bg': '#0f0f23',
            'neuron': '#00d4ff',
            'neuron_active': '#ff6b6b',
            'connection': '#16213e',
            'connection_active': '#4ecdc4',
            'text': '#ffffff',
            'panel': '#16213e',
            'button': '#4ecdc4',
            'accent': '#ffd93d'
        }
        
        self.initialize_network()
        self.create_widgets()
        self.start_animation_loop()
        
    def initialize_network(self):
        """Initialize weights and biases for the network"""
        self.weights = []
        self.biases = []
        
        for i in range(len(self.layers) - 1):
            # Xavier initialization
            w = [[random.uniform(-1, 1) for _ in range(self.layers[i])] 
                 for _ in range(self.layers[i + 1])]
            b = [random.uniform(-0.5, 0.5) for _ in range(self.layers[i + 1])]
            self.weights.append(w)
            self.biases.append(b)
            
        # Initialize activations
        self.activations = [[0.0 for _ in range(layer_size)] for layer_size in self.layers]
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_font = font.Font(family="Arial", size=20, weight="bold")
        title_label = tk.Label(main_frame, text="🧠 3D Neural Network Visualizer", 
                              font=title_font, fg=self.colors['accent'], bg=self.colors['bg'])
        title_label.pack(pady=10)
        
        # Control panel
        control_frame = tk.Frame(main_frame, bg=self.colors['panel'], relief=tk.RAISED, bd=2)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Architecture controls
        arch_frame = tk.Frame(control_frame, bg=self.colors['panel'])
        arch_frame.pack(side=tk.LEFT, padx=10, pady=5)
        
        tk.Label(arch_frame, text="Network Architecture:", 
                font=("Arial", 12, "bold"), fg=self.colors['text'], bg=self.colors['panel']).pack()
        
        # Layer input frame
        layer_input_frame = tk.Frame(arch_frame, bg=self.colors['panel'])
        layer_input_frame.pack(pady=5)
        
        tk.Label(layer_input_frame, text="Layers (comma separated):", 
                fg=self.colors['text'], bg=self.colors['panel']).pack(side=tk.LEFT)
        
        self.layer_entry = tk.Entry(layer_input_frame, width=20, font=("Arial", 10))
        self.layer_entry.pack(side=tk.LEFT, padx=5)
        self.layer_entry.insert(0, "4,6,4,2")
        
        tk.Button(layer_input_frame, text="Update Architecture", 
                 command=self.update_architecture, bg=self.colors['button'], 
                 fg='white', font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
        
        # Input controls
        input_frame = tk.Frame(control_frame, bg=self.colors['panel'])
        input_frame.pack(side=tk.LEFT, padx=20, pady=5)
        
        tk.Label(input_frame, text="Input Values:", 
                font=("Arial", 12, "bold"), fg=self.colors['text'], bg=self.colors['panel']).pack()
        
        self.input_entries = []
        input_grid = tk.Frame(input_frame, bg=self.colors['panel'])
        input_grid.pack(pady=5)
        
        for i in range(4):
            tk.Label(input_grid, text=f"Input {i+1}:", 
                    fg=self.colors['text'], bg=self.colors['panel']).grid(row=i, column=0, sticky=tk.W)
            entry = tk.Entry(input_grid, width=8, font=("Arial", 9))
            entry.grid(row=i, column=1, padx=5)
            entry.insert(0, f"{random.uniform(0, 1):.2f}")
            self.input_entries.append(entry)
        
        # Control buttons
        button_frame = tk.Frame(control_frame, bg=self.colors['panel'])
        button_frame.pack(side=tk.RIGHT, padx=10, pady=5)
        
        tk.Button(button_frame, text="🚀 Forward Propagation", 
                 command=self.start_forward_propagation, bg=self.colors['button'], 
                 fg='white', font=("Arial", 11, "bold")).pack(pady=2)
        
        tk.Button(button_frame, text="🎲 Random Inputs", 
                 command=self.randomize_inputs, bg=self.colors['accent'], 
                 fg='black', font=("Arial", 10, "bold")).pack(pady=2)
        
        tk.Button(button_frame, text="🔄 Reset Network", 
                 command=self.reset_network, bg='#ff6b6b', 
                 fg='white', font=("Arial", 10, "bold")).pack(pady=2)
        
        # 3D Canvas
        canvas_frame = tk.Frame(main_frame, bg=self.colors['bg'], relief=tk.SUNKEN, bd=3)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, bg=self.colors['bg'], highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind mouse events for 3D rotation
        self.canvas.bind("<Button-1>", self.start_rotate)
        self.canvas.bind("<B1-Motion>", self.rotate_view)
        self.canvas.bind("<MouseWheel>", self.zoom_view)
        
        # Status and info panel
        info_frame = tk.Frame(main_frame, bg=self.colors['panel'], relief=tk.RAISED, bd=2)
        info_frame.pack(fill=tk.X, pady=5)
        
        self.status_label = tk.Label(info_frame, text="Status: Ready", 
                                   font=("Arial", 11, "bold"), fg=self.colors['text'], 
                                   bg=self.colors['panel'])
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(info_frame, text="Click and drag to rotate • Scroll to zoom", 
                                 font=("Arial", 10), fg=self.colors['accent'], 
                                 bg=self.colors['panel'])
        self.info_label.pack(side=tk.RIGHT, padx=10)
        
        # Legend
        legend_frame = tk.Frame(main_frame, bg=self.colors['panel'])
        legend_frame.pack(fill=tk.X, pady=2)
        
        legend_items = [
            ("🔵 Inactive Neuron", self.colors['neuron']),
            ("🔴 Active Neuron", self.colors['neuron_active']),
            ("— Weak Connection", self.colors['connection']),
            ("━ Strong Connection", self.colors['connection_active'])
        ]
        
        for i, (text, color) in enumerate(legend_items):
            tk.Label(legend_frame, text=text, fg=color, bg=self.colors['panel'], 
                    font=("Arial", 9)).pack(side=tk.LEFT, padx=15)
        
    def update_architecture(self):
        """Update network architecture from user input"""
        try:
            layers_str = self.layer_entry.get().strip()
            new_layers = [int(x.strip()) for x in layers_str.split(',')]
            
            if len(new_layers) < 2:
                raise ValueError("Need at least 2 layers")
            if any(x < 1 or x > 10 for x in new_layers):
                raise ValueError("Layer sizes must be between 1 and 10")
                
            self.layers = new_layers
            self.initialize_network()
            
            # Update input entries
            for entry in self.input_entries:
                entry.destroy()
            self.input_entries.clear()
            
            # Recreate input entries for new input layer size
            input_grid = self.input_entries[0].master if self.input_entries else None
            if input_grid:
                input_grid.destroy()
            
            # Find the input frame and recreate grid
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, tk.Frame):
                            for grandchild in child.winfo_children():
                                if isinstance(grandchild, tk.Frame):
                                    for item in grandchild.winfo_children():
                                        if isinstance(item, tk.Label) and "Input Values:" in str(item.cget("text")):
                                            parent = item.master
                                            input_grid = tk.Frame(parent, bg=self.colors['panel'])
                                            input_grid.pack(pady=5)
                                            
                                            for i in range(self.layers[0]):
                                                tk.Label(input_grid, text=f"Input {i+1}:", 
                                                        fg=self.colors['text'], bg=self.colors['panel']).grid(row=i, column=0, sticky=tk.W)
                                                entry = tk.Entry(input_grid, width=8, font=("Arial", 9))
                                                entry.grid(row=i, column=1, padx=5)
                                                entry.insert(0, f"{random.uniform(0, 1):.2f}")
                                                self.input_entries.append(entry)
                                            break
            
            self.status_label.config(text=f"Architecture updated: {' → '.join(map(str, self.layers))}")
            
        except ValueError as e:
            messagebox.showerror("Invalid Architecture", str(e))
            
    def randomize_inputs(self):
        """Generate random input values"""
        for entry in self.input_entries:
            entry.delete(0, tk.END)
            entry.insert(0, f"{random.uniform(0, 1):.2f}")
    
    def reset_network(self):
        """Reset the network to initial state"""
        self.is_animating = False
        self.current_layer = 0
        self.pulse_time = 0
        self.initialize_network()
        self.status_label.config(text="Network reset")
        
    def start_rotate(self, event):
        self.last_x = event.x
        self.last_y = event.y
        
    def rotate_view(self, event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y
        
        self.rotation_y += dx * 0.01
        self.rotation_x += dy * 0.01
        
        self.last_x = event.x
        self.last_y = event.y
        
    def zoom_view(self, event):
        if event.delta > 0:
            self.zoom *= 1.1
        else:
            self.zoom /= 1.1
        self.zoom = max(0.3, min(3.0, self.zoom))
        
    def project_3d(self, x, y, z):
        """Project 3D coordinates to 2D screen coordinates"""
        # Apply rotation
        cos_x, sin_x = math.cos(self.rotation_x), math.sin(self.rotation_x)
        cos_y, sin_y = math.cos(self.rotation_y), math.sin(self.rotation_y)
        
        # Rotate around Y axis
        x_rot = x * cos_y - z * sin_y
        z_rot = x * sin_y + z * cos_y
        
        # Rotate around X axis
        y_rot = y * cos_x - z_rot * sin_x
        z_final = y * sin_x + z_rot * cos_x
        
        # Apply perspective projection
        perspective = 1 / (1 + z_final * 0.001)
        
        # Scale and translate to screen coordinates
        screen_x = self.center_x + x_rot * self.zoom * perspective
        screen_y = self.center_y + y_rot * self.zoom * perspective
        
        return screen_x, screen_y, z_final
    
    def sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + math.exp(-max(-500, min(500, x))))
    
    def start_forward_propagation(self):
        """Start the forward propagation animation"""
        if self.is_animating:
            return
            
        try:
            # Get input values
            inputs = []
            for i, entry in enumerate(self.input_entries):
                if i < len(self.activations[0]):
                    inputs.append(float(entry.get()))
                    
            # Set input layer activations
            for i, val in enumerate(inputs):
                if i < len(self.activations[0]):
                    self.activations[0][i] = val
                    
            self.is_animating = True
            self.current_layer = 0
            self.status_label.config(text="Forward propagation started...")
            
            # Start animation in separate thread
            threading.Thread(target=self.animate_forward_propagation, daemon=True).start()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for all inputs")
    
    def animate_forward_propagation(self):
        """Animate the forward propagation process"""
        for layer_idx in range(len(self.layers) - 1):
            self.current_layer = layer_idx
            
            # Calculate next layer activations
            next_activations = []
            for j in range(self.layers[layer_idx + 1]):
                weighted_sum = self.biases[layer_idx][j]
                for i in range(self.layers[layer_idx]):
                    weighted_sum += self.activations[layer_idx][i] * self.weights[layer_idx][j][i]
                next_activations.append(self.sigmoid(weighted_sum))
            
            # Update activations
            self.activations[layer_idx + 1] = next_activations
            
            # Animation delay
            time.sleep(1.0)
            
        self.is_animating = False
        self.status_label.config(text="Forward propagation completed!")
        
        # Display final outputs
        output_str = "Outputs: " + ", ".join([f"{val:.3f}" for val in self.activations[-1]])
        self.info_label.config(text=output_str)
    
    def draw_neuron(self, x, y, z, radius, activation, layer_idx, neuron_idx):
        """Draw a 3D neuron with lighting effects"""
        screen_x, screen_y, depth = self.project_3d(x, y, z)
        
        # Calculate size based on depth
        size = radius * (1 + depth * 0.0001)
        
        # Determine color based on activation and animation
        if self.is_animating and layer_idx <= self.current_layer:
            intensity = activation
            if layer_idx == self.current_layer:
                pulse = 0.5 + 0.5 * math.sin(self.pulse_time * 8)
                intensity = max(intensity, pulse)
            
            # Color interpolation
            base_color = self.colors['neuron_active'] if intensity > 0.5 else self.colors['neuron']
            
        else:
            base_color = self.colors['neuron']
            intensity = 0.3
        
        # Draw neuron with gradient effect
        for i in range(int(size), 0, -2):
            alpha = i / size
            shade = int(255 * intensity * alpha)
            
            if base_color == self.colors['neuron_active']:
                color = f"#{min(255, shade):02x}{min(100, shade//2):02x}{min(100, shade//2):02x}"
            else:
                color = f"#{min(100, shade//2):02x}{min(200, shade):02x}{min(255, shade):02x}"
            
            self.canvas.create_oval(screen_x - i, screen_y - i, 
                                  screen_x + i, screen_y + i, 
                                  fill=color, outline="")
        
        # Draw highlight
        highlight_x = screen_x - size * 0.3
        highlight_y = screen_y - size * 0.3
        highlight_size = size * 0.4
        
        self.canvas.create_oval(highlight_x - highlight_size, highlight_y - highlight_size,
                              highlight_x + highlight_size, highlight_y + highlight_size,
                              fill="white", outline="")
        
        # Draw activation value
        if activation > 0.01:
            self.canvas.create_text(screen_x, screen_y + size + 15, 
                                  text=f"{activation:.2f}", 
                                  fill=self.colors['text'], 
                                  font=("Arial", 8))
    
    def draw_connection(self, x1, y1, z1, x2, y2, z2, weight, is_active=False):
        """Draw a 3D connection between neurons"""
        screen_x1, screen_y1, depth1 = self.project_3d(x1, y1, z1)
        screen_x2, screen_y2, depth2 = self.project_3d(x2, y2, z2)
        
        # Determine line properties based on weight and activation
        abs_weight = abs(weight)
        width = max(1, int(abs_weight * 3))
        
        if is_active and self.is_animating:
            color = self.colors['connection_active']
            width = max(width, 2)
        else:
            # Color based on weight (positive = blue, negative = red)
            if weight > 0:
                intensity = min(abs_weight, 1.0)
                color = f"#{int(100 * intensity):02x}{int(150 * intensity):02x}{int(255 * intensity):02x}"
            else:
                intensity = min(abs_weight, 1.0)
                color = f"#{int(255 * intensity):02x}{int(100 * intensity):02x}{int(100 * intensity):02x}"
        
        # Draw connection line
        self.canvas.create_line(screen_x1, screen_y1, screen_x2, screen_y2,
                              fill=color, width=width, capstyle=tk.ROUND)
    
    def draw_network(self):
        """Draw the entire 3D neural network"""
        self.canvas.delete("all")
        
        # Calculate positions for each layer
        layer_positions = []
        total_depth = 400
        
        for layer_idx, layer_size in enumerate(self.layers):
            z = (layer_idx - len(self.layers) / 2) * total_depth / len(self.layers)
            
            neurons = []
            for neuron_idx in range(layer_size):
                y = (neuron_idx - layer_size / 2) * 60
                x = 0
                neurons.append((x, y, z))
            
            layer_positions.append(neurons)
        
        # Draw connections first (so they appear behind neurons)
        for layer_idx in range(len(self.layers) - 1):
            current_layer = layer_positions[layer_idx]
            next_layer = layer_positions[layer_idx + 1]
            
            for i, (x1, y1, z1) in enumerate(current_layer):
                for j, (x2, y2, z2) in enumerate(next_layer):
                    weight = self.weights[layer_idx][j][i]
                    is_active = (self.is_animating and 
                               layer_idx <= self.current_layer and 
                               self.activations[layer_idx][i] > 0.1)
                    
                    self.draw_connection(x1, y1, z1, x2, y2, z2, weight, is_active)
        
        # Draw neurons
        for layer_idx, layer_neurons in enumerate(layer_positions):
            for neuron_idx, (x, y, z) in enumerate(layer_neurons):
                activation = self.activations[layer_idx][neuron_idx]
                self.draw_neuron(x, y, z, 20, activation, layer_idx, neuron_idx)
        
        # Draw layer labels
        for layer_idx, layer_neurons in enumerate(layer_positions):
            if layer_neurons:
                x, y, z = layer_neurons[0]
                screen_x, screen_y, _ = self.project_3d(x, y - 80, z)
                
                if layer_idx == 0:
                    label = "Input Layer"
                elif layer_idx == len(self.layers) - 1:
                    label = "Output Layer"
                else:
                    label = f"Hidden Layer {layer_idx}"
                
                self.canvas.create_text(screen_x, screen_y, text=label,
                                      fill=self.colors['accent'], 
                                      font=("Arial", 12, "bold"))
    
    def start_animation_loop(self):
        """Start the main animation loop"""
        def animate():
            self.pulse_time += self.animation_speed
            
            # Update canvas size
            self.center_x = self.canvas.winfo_width() // 2
            self.center_y = self.canvas.winfo_height() // 2
            
            # Draw the network
            self.draw_network()
            
            # Schedule next frame
            self.root.after(50, animate)
        
        self.root.after(100, animate)

def main():
    root = tk.Tk()
    app = NeuralNetwork3DVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# ©SOFTWARELABS
# BY - PARAS DHIMAN (Co-Founder)
# CONTACT:
#     softwarelabschd@gmail.com
