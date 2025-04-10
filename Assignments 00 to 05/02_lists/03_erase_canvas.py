import tkinter as tk

# Canvas size and grid configuration
canvas_width = 600
canvas_height = 400
rows = 10
cols = 15
cell_width = canvas_width // cols
cell_height = canvas_height // rows

# Create the Tkinter window and canvas
root = tk.Tk()
root.title("Canvas Eraser")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Draw the grid of blue cells directly on the canvas
def draw_grid():
    for r in range(rows):
        for c in range(cols):
            x1 = c * cell_width
            y1 = r * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            canvas.create_rectangle(x1, y1, x2, y2, fill='red', outline='brown')

# Eraser properties
eraser_width = 60
eraser_height = 40
eraser = canvas.create_rectangle(0, 0, eraser_width, eraser_height, fill='grey', outline='brown')

# Function to update the grid when the eraser moves
def erase_cells(event):
    # Calculate the position where the eraser is
    start_x = event.x - eraser_width // 2
    start_y = event.y - eraser_height // 2
    
    # Loop through the grid and erase cells
    for r in range(rows):
        for c in range(cols):
            # Calculate the bounds of the current cell
            cell_x1 = c * cell_width
            cell_y1 = r * cell_height
            cell_x2 = cell_x1 + cell_width
            cell_y2 = cell_y1 + cell_height

            # Check if the eraser overlaps with the cell
            if (start_x + eraser_width > cell_x1 and start_x < cell_x2) and (start_y + eraser_height > cell_y1 and start_y < cell_y2):
                # Erase the cell by changing its color to white
                canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2, fill='pink', outline='black')

    # Move the eraser to the new position
    canvas.coords(eraser, start_x, start_y, start_x + eraser_width, start_y + eraser_height)

# Function to start dragging the eraser
def start_drag(event):
    erase_cells(event)  # Erase cells while dragging the mouse

# Bind mouse motion event to the eraser dragging
canvas.bind("<B1-Motion>", start_drag)

# Draw the initial grid of blue cells
draw_grid()

# Start the Tkinter event loop
root.mainloop()
