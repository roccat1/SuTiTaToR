import tkinter as tk, webbrowser, os

window = None
nick_entry = None
ip_entry = None
port_entry = None
label_file_explorer = None
button_run = None

def connectToServer() -> None:
    """Connects to the server"""
    global nick_entry, ip_entry, port_entry, label_file_explorer, button_run

    nick = nick_entry.get()
    ip = ip_entry.get()
    port = int(port_entry.get())

    import scripts.client.createConnection as createConnection
    createConnection.create_connection(ip, port, nick)

    label_file_explorer.configure(text=f"Connected to {ip}:{port} as {nick}")
    button_run.configure(state="normal")

def exit() -> None:
    """exit"""
    global window
    window.destroy()
    os._exit(0)

def hostServer() -> None:
    # check if SuTiTaToRServer.exe exists
    if not os.path.isfile("SuTiTaToRServer.exe"):
        os.system("start cmd /k python SuTiTaToRServer.py")
    else:
        os.system("start cmd /k SuTiTaToRServer.exe")

def runProgram() -> None:
    import scripts.UI.boardUI as boardUI
    window.destroy()
    boardUI.UI(True)

def returnToMainMenu() -> None:
    window.destroy()

def UI():
    """main window UI"""
    global window, nick_entry, ip_entry, port_entry, label_file_explorer, button_run

    window = tk.Tk()
    window.title('SuTiTaToR')
    window.geometry("700x380")
    window.config(background = "turquoise2")
    window.quit = exit
    window.resizable(False, False)

    label_file_explorer = tk.Label(window, 
							text = "Connect to the server to run the game",
							width = 44, height = 2, 
							fg = "black",
                            background="pale green",
                            font=("Arial", 20)
        )

    button_run = tk.Button(window, 
						text = "Run program (Takes a while to load))",
						command = runProgram,
                        width = 40, height = 2, state="disabled")
    
    button_connect_to_server = tk.Button(window, 
					text = "Connect to server",
					command = connectToServer,
                    width = 40, height = 2) 
    
    button_host_server = tk.Button(window,
                    text = "Host server",
                    command = hostServer,
                    width = 40, height = 2)
    
    button_exit = tk.Button(window, 
					text = "Exit",
					command = exit,
                    width = 40, height = 2) 
    
    #text input for nick, ip, port
    nick = tk.StringVar()
    ip = tk.StringVar()
    port = tk.StringVar()

    nick_label = tk.Label(window, text="Nick", width=20, font=("Arial", 19))
    ip_label = tk.Label(window, text="IP", width=20, font=("Arial", 19))
    port_label = tk.Label(window, text="Port", width=20, font=("Arial", 19))

    nick_entry = tk.Entry(window, textvariable=nick, width=20, font=("Arial", 20))
    ip_entry = tk.Entry(window, textvariable=ip, width=20, font=("Arial", 20))
    port_entry = tk.Entry(window, textvariable=port, width=20, font=("Arial", 20))

    #change default text
    port_entry.insert(0, "5050")

    nick_label.grid(column=1, row=2, sticky="e")
    ip_label.grid(column=1, row=3, sticky="e")
    port_label.grid(column=1, row=4, sticky="e")

    nick_entry.grid(column=2, row=2, sticky="w")
    ip_entry.grid(column=2, row=3, sticky="w")
    port_entry.grid(column=2, row=4, sticky="w")

    
    label_file_explorer.grid(column = 1, row = 1, columnspan=2)

    button_run.grid(column = 1, row = 5, columnspan=2)

    button_exit.grid(column = 1,row = 9, columnspan=2)

    button_connect_to_server.grid(column = 1,row = 6, columnspan=2)

    button_host_server.grid(column = 1,row = 7, columnspan=2)

    
    #footer
    footerLabel = tk.Label(window, 
                            text = "Author: github.com/roccat1",
                            width = 87, height = 2, 
                            fg = "black",
                            background="pale green",
                            font=("Arial", 10)
        )
    
    footerLabel.bind("<Button-1>", lambda e:webbrowser.open_new_tab("https://github.com/roccat1"))
    
    footerLabel.grid(column = 1, row = 10, columnspan=2, sticky="w")
    
    # Let the window wait for any events
    window.mainloop()
