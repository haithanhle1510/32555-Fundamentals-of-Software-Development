import tkinter as tk


def menu_label(master, title: str):
    return tk.Label(
        master, text=title, padx=20, pady=20, font="Helvetica 16 bold"
    ).pack()


def information_label(master, title: str):
    return tk.Label(master, text=title, font="Helvetica 16 bold", pady=10).pack()


def option_button(master, title, click_function):
    return tk.Button(
        master,
        text=title,
        bg="black",
        fg="white",
        font="Helvetica 14",
        command=click_function,
        height=2,
    ).pack()


def exit_button(master, title, click_function):
    return tk.Button(
        master,
        text=title,
        bg="red",
        fg="white",
        font="Helvetica 14",
        command=click_function,
        height=2,
    ).pack()


def table(master, data, headers, row_existing):
    print_data = headers + data
    for i in range(len(print_data)):
        for j in range(len(print_data[0])):
            width = 15
            if j == 1:
                width = 20
            if j == 2:
                width = 35

            e = tk.Entry(master, width=width, fg="blue", font=("Arial", 12, "bold"))
            e.grid(row=i + row_existing, column=j + 1)
            e.insert(tk.END, print_data[i][j])
