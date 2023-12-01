import tkinter as tk
from fantasydata import *

# ... (your existing code)

def on_fantasy_button_click():
    # ... (your existing code)

    # Add a Label to display data
    data_label = tk.Label(window, text="Data imported from Fantasy API", font=button_font, bg="light gray", width=30, height=2)
    data_label.place(x=300, y=200)

    # You can customize this part to display actual data from your Fantasy API
    # For example, if you have a function to get data from the API
    fantasy_data = get_fantasy_data()  # Replace with your actual function
    data_text = "\n".join([f"{key}: {value}" for key, value in fantasy_data.items()])
    
    data_text_label = tk.Label(window, text=data_text, font=button_font, bg="light gray", width=30, height=5)
    data_text_label.place(x=300, y=300)

    label.after(3000, reset_label_text2)

# ... (your existing code)

# Start the main event loop
window.mainloop()