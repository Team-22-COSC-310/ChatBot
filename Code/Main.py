from tkinter import *
from Code.preprocess import parse_string as ps
from Code.category import find_category as fc
from Code.subject import find_subject as fs
from Code.response import generate_response as gs

"""
This is the core class for the ChatBot. This is a general purpose ChatBot about retail clothing and accessories. The 
ChatBot is able to discuss reviews, compliant, and product satisfaction.
"""


class ChatApplication:

    BG_COLOR: str = "#202531"
    FG_COLOR: str = "#CBCDD1"
    FONT: str = "Helvetica 14"
    FONT_BOLD: str = "helvetica 12 bold"

    def __init__(self) -> None:
        """
        This is the core class for the ChatBot GUI. It is responsible for the GUI and returning a response to the user
        :return None:
        """
        # create main window
        self.root = Tk()
        self.root.title("Customer Service ChatBot")
        self.root.configure(
            width=180,
            height=320,
            bg=self.BG_COLOR,
        )
        self.root.minsize(
            width=470,
            height=550,
        )

        # create title label
        self.header_label = Label(
            self.root,
            bg=self.BG_COLOR,
            fg=self.FG_COLOR,
            text="ChatBot",
            font=self.FONT_BOLD,
        )
        self.header_label.place(
            relwidth=1,
            relheight=0.1,
        )

        # create main text body for conversation
        self.chat_log = Text(
            self.root,
            bg=self.BG_COLOR,
            fg=self.FG_COLOR,
            height=10,
            font=self.FONT,
            padx=5,
            pady=5,
            wrap=WORD,
        )
        self.chat_log.place(
            relwidth=0.94,
            relheight=0.8,
            relx=0.01,
            rely=0.1,
        )
        self.chat_log.configure(
            cursor="arrow",
            state=DISABLED,
            highlightbackground=self.FG_COLOR,
        )
        self.scrollbar = Scrollbar(
            self.root,
        )
        self.scrollbar.place(
            relheight=0.8,
            relx=0.95,
            rely=0.1,
        )
        self.scrollbar.configure(
            command=self.chat_log.yview,
        )

        # create entry for user input
        self.message_entry = Entry(
            self.root,
            bg=self.BG_COLOR,
            fg=self.FG_COLOR,
            font=self.FONT,
        )
        self.message_entry.place(
            relwidth=0.82,
            relheight=0.065,
            relx=0.01,
            rely=0.92,
        )
        self.message_entry.focus()
        self.message_entry.bind("<Return>", self._on_receive)

        # create send button for user input
        self.send_button_Frame = Frame(
            self.root,
            bg=self.BG_COLOR,
        )
        self.send_button_Frame.place(
            relwidth=0.15,
            relheight=0.065,
            relx=0.84,
            rely=0.92,
        )
        self.send_button = Button(
            self.send_button_Frame,
            bg=self.BG_COLOR,
            fg=self.FG_COLOR,
            text="Send",
            font=self.FONT_BOLD,
            command=lambda: self._on_receive(None),
        )
        self.send_button.pack(
            expand=True,
            fill="both",
        )

    def _on_receive(self, _event: Event or None) -> None:
        """
        inserts user message and bots reply to textbox
        :param _event: Event type that triggered function
        :type _event: Event or None
        :return None:
        """
        if self.message_entry.get():
            self.chat_log.configure(state=NORMAL)

            # insert user message
            msg: str = self.message_entry.get()
            self.message_entry.delete(0, END)
            self.chat_log.insert(END, "User: " + msg + "\n\n")

            # generate and insert bot message
            msg = ps(msg)
            category: str = fc(msg)
            subject: str = fs(msg)
            response: str = gs(category, subject)
            self.chat_log.insert(END, "Customer Service: " + response + "\n\n")

            self.chat_log.configure(state=DISABLED)
            self.chat_log.see(END)

    def run(self) -> None:
        """
        Calls mainloop for main GUI window
        :return None:
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
