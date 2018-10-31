"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and JUSTIN OGASAWARA.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    my_frame = ttk.Frame(window, padding=100)
    my_frame.grid()
    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button = ttk.Button(my_frame, text='CLick')
    button['command'] = (lambda: hello_function())
    button.grid()
    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    type_here = ttk.Entry(my_frame)
    type_here.grid()

    button1 = ttk.Button(my_frame, text='Click after Typing')
    button1['command'] = (lambda: hello_or_goodbye(type_here))
    button1.grid()

    next_frame = ttk.Entry(my_frame)
    next_frame.grid()

    button2 = ttk.Button(my_frame, text='Try clicking me')
    button2['command'] = (lambda: print_N_times(type_here, next_frame))
    button2.grid()
    # ------------------------------------------------------------------
    # DONE 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # ------------------------------------------------------------------
    #DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    window.mainloop()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------

def hello_or_goodbye(parameter):
    contents_of_entry = parameter.get()
    for k in range(len(contents_of_entry)-1):
        if contents_of_entry[k] == 'o' and contents_of_entry[k+1] == 'k':
            print('Hello')
            return
    print('Goodbye')

def hello_function():
    print('Hello')

def print_N_times(entry1, entry2):
    contents_of_entry2 = entry2.get()
    contents_of_entry1 = entry1.get()
    n = int(contents_of_entry2)

    print(n*contents_of_entry1)

main()


