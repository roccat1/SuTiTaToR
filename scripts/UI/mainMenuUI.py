import tkinter as tk
import webbrowser, os

onlineMode = True
window = None

def runProgram() -> None:
    """run program"""
    global onlineMode, window
    window.destroy()

    if onlineMode.get():
        import scripts.UI.onlineModeUI as onlineModeUI
        onlineModeUI.UI()
    else:
        import scripts.UI.boardUI as boardUI
        boardUI.UI(False)

def exit() -> None:
    """exit"""
    global window
    window.destroy()
    os._exit(0)

def mainWindowUI() -> None:
    """main window UI"""
    global onlineMode, window

    window = tk.Tk()
    window.title('SuTiTaToR')
    window.geometry("700x230")
    window.config(background = "turquoise2")
    window.quit = exit
    window.resizable(False, False)

    label_file_explorer = tk.Label(window, 
							text = "SuTiTaToR",
							width = 44, height = 2, 
							fg = "black",
                            background="pale green",
                            font=("Arial", 20)
        )

    button_run = tk.Button(window, 
						text = "Run program",
						command = runProgram,
                        width = 40, height = 2)
    
    button_exit = tk.Button(window, 
					text = "Exit",
					command = exit,
                    width = 40, height = 2) 

    onlineMode = tk.BooleanVar(value=onlineMode)
    onlineTrue_button = tk.Radiobutton(window, text="Online", variable=onlineMode,
                                indicatoron=False, value=True, width=19, height = 2)
    onlineFalse_button = tk.Radiobutton(window, text="Offline", variable=onlineMode,
                                indicatoron=False, value=False, width=19, height = 2)
    
    label_file_explorer.grid(column = 1, row = 1, columnspan=2)

    button_run.grid(column = 1, row = 4, columnspan=2)

    button_exit.grid(column = 1,row = 6, columnspan=2)

    onlineTrue_button.grid(column = 1,row = 2, sticky="e")
    onlineFalse_button.grid(column = 2,row = 2, sticky="w")
    
    #footer
    footerLabel = tk.Label(window, 
                            text = "Author: github.com/roccat1",
                            width = 87, height = 2, 
                            fg = "black",
                            background="pale green",
                            font=("Arial", 10)
        )
    
    footerLabel.bind("<Button-1>", lambda e:webbrowser.open_new_tab("https://github.com/roccat1"))
    
    footerLabel.grid(column = 1, row = 7, columnspan=2, sticky="w")
    
    # Let the window wait for any events
    window.mainloop()
