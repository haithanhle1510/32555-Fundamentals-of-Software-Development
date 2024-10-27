def clear_window(master):
    for widget in master.winfo_children():
        widget.destroy()
