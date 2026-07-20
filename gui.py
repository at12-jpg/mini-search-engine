from search_engine import search, get_all_words
import tkinter as tk

all_words = get_all_words()


from search_engine import search, get_all_words
import tkinter as tk

all_words = get_all_words()


from search_engine import search, get_all_words
import tkinter as tk

all_words = get_all_words()


def update_suggestions(event):

    query = search_box.get().lower()

    suggestion_box.delete(0, tk.END)

    for word in all_words:

        if word.startswith(query):

            suggestion_box.insert(tk.END, word)

def perform_search(event=None):
    query = search_box.get()

    results = search(query)

    results_box.delete("1.0", tk.END)

    if results:

        for result in results:
            results_box.insert(
                tk.END,
                f"{result['filename']}\n"
            )
            for line in result["lines"]:
                results_box.insert(
                    tk.END,
                    f">{line}\n"
                )
            results_box.insert(
                tk.END,
                f"Matches: {result['matches']}\n"
            )
            results_box.insert(
                tk.END,
                "-"*40 + "\n\n"
            )
    else:
        results_box.insert(tk.END, "❌ No results found.")



window = tk.Tk()
window.title("Mini Search Engine")
window.geometry("500x800")



title = tk.Label(
    window,
    text="Mini Search Engine",
    font=("Georgia", 18, "bold")
)
title.pack(pady=20)



search_label = tk.Label(
    window,
    text="Search:"
)
search_label.pack()



search_box = tk.Entry(
    window,
    width=60
)
search_box.pack(pady=10)
search_box.bind("<Return>", perform_search)
search_box.bind("<KeyRelease>", update_suggestions)

suggestion_box = tk.Listbox(
    window, 
    width=60, 
    height=5
)
suggestion_box.pack()

search_button = tk.Button(
    window,
    text="Search",
    command=perform_search
)
search_button.pack(pady=10)



results_box = tk.Text(
    window,
    width=55,
    height=15
)
results_box.pack(pady=10)


window.mainloop()

def perform_search(event=None):
    query = search_box.get()

    results = search(query)

    results_box.delete("1.0", tk.END)

    if results:

        for result in results:
            results_box.insert(
                tk.END,
                f"{result['filename']}\n"
            )
            for line in result["lines"]:
                results_box.insert(
                    tk.END,
                    f">{line}\n"
                )
            results_box.insert(
                tk.END,
                f"Matches: {result['matches']}\n"
            )
            results_box.insert(
                tk.END,
                "-"*40 + "\n\n"
            )
    else:
        results_box.insert(tk.END, "❌ No results found.")



window = tk.Tk()
window.title("Mini Search Engine")
window.geometry("500x800")



title = tk.Label(
    window,
    text="Mini Search Engine",
    font=("Georgia", 18, "bold")
)
title.pack(pady=20)



search_label = tk.Label(
    window,
    text="Search:"
)
search_label.pack()



search_box = tk.Entry(
    window,
    width=60
)
search_box.pack(pady=10)
search_box.bind("<Return>", perform_search)
search_box.bind("<KeyRelease>", update_suggestions)

suggestion_box = tk.Listbox(
    window, 
    width=60, 
    height=5
)
suggestion_box.pack()

search_button = tk.Button(
    window,
    text="Search",
    command=perform_search
)
search_button.pack(pady=10)



results_box = tk.Text(
    window,
    width=55,
    height=15
)
results_box.pack(pady=10)


window.mainloop()

def perform_search(event=None):
    query = search_box.get()

    results = search(query)

    results_box.delete("1.0", tk.END)

    if results:

        for result in results:
            results_box.insert(
                tk.END,
                f"{result['filename']}\n"
            )
            for line in result["lines"]:
                results_box.insert(
                    tk.END,
                    f">{line}\n"
                )
            results_box.insert(
                tk.END,
                f"Matches: {result['matches']}\n"
            )
            results_box.insert(
                tk.END,
                "-"*40 + "\n\n"
            )
    else:
        results_box.insert(tk.END, "❌ No results found.")



window = tk.Tk()
window.title("Mini Search Engine")
window.geometry("500x800")



title = tk.Label(
    window,
    text="Mini Search Engine",
    font=("Georgia", 18, "bold")
)
title.pack(pady=20)



search_label = tk.Label(
    window,
    text="Search:"
)
search_label.pack()



search_box = tk.Entry(
    window,
    width=60
)
search_box.pack(pady=10)
search_box.bind("<Return>", perform_search)
search_box.bind("<KeyRelease>", update_suggestions)

suggestion_box = tk.Listbox(
    window, 
    width=60, 
    height=5
)
suggestion_box.pack()

search_button = tk.Button(
    window,
    text="Search",
    command=perform_search
)
search_button.pack(pady=10)



results_box = tk.Text(
    window,
    width=55,
    height=15
)
results_box.pack(pady=10)


window.mainloop()