import time
import socket
import threading
from tkinter import *
from preprocess import parse_string as ps
from category import find_category as fc
from subject import find_subject as fs
from response import generate_response as gs
from typing import Optional

"""
This is the core class for the ChatBot. This is a general purpose ChatBot about retail clothing and accessories. The 
ChatBot is able to discuss reviews, compliant, and product satisfaction.
"""


class Socket(threading.Thread):
    def __init__(self, conn_type: str, ip: str, port: int) -> None:
        """
        Socket is responsible for creating a socket and linking a host and client together for back and forth
        communication
        :param str conn_type: type of connection user wants to make
        :param str ip: host ip address
        :param int port: access port number
        :return None:
        """
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_type: str = conn_type
        self.ip: str = ip
        self.port: int = port
        self.mainloop: bool = False
        self.start()

    def _host(self) -> None:
        """
        Creates a socket for a host
        :return None:
        """
        self.socket.bind((self.ip, self.port))
        self.socket.listen(1)
        app.log("[System]: Socket created. Waiting for other bot...\n\n")
        self.socket = self.socket.accept()[0]
        app.log("[System]: Client has joined!\n\n")
        self._send(gs("greeting", ""))

    def _client(self) -> None:
        """
        Creates a socket for a client
        :return None:
        """
        app.log("[System]: Connecting to host...\n\n")
        self.socket.connect((self.ip, self.port))
        app.log("[System]: Connected to host!\n\n")

    def _send(self, msg: str) -> None:
        """
        Sends a message through the connected socket
        :param msg:
        :return:
        """
        try:
            app.log("LOCAL BOT: {msg}\n\n".format(msg=msg))
            self.socket.send(msg.encode())

        except ConnectionAbortedError:
            self.mainloop = False
            return

    def _receive(self) -> str:
        """
        Receives a message through the connected socket
        :return str: returns the message received
        """
        try:
            msg: str = self.socket.recv(1024).decode()
            app.log("OTHER BOT: {msg}\n\n".format(msg=msg))
            return msg

        except ConnectionAbortedError as error:
            self.mainloop = False
            return str(error)

    def run(self) -> None:
        """
        threaded function for the retrieval and sending of messages through the socket
        :return None:
        """
        if self.conn_type == "HOST":
            self._host()

        elif self.conn_type == "CLIENT":
            self._client()

        self.mainloop = True
        while self.mainloop is True:
            msg: str = self._receive()
            time.sleep(1.5)
            msg = ps(msg)
            category: str = fc(msg)
            subject: str = fs(msg)
            response: str = gs(category, subject)
            self._send(response)

        app.log("[System]: Closing Socket...\n\n")
        app.socket = None
        self.socket.close()
        app.log("[System]: Socket closed.\n\n")


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
        self.socket: Optional[Socket] = None
        self.COMMANDS: dict["str", callable] = {
            "--help": self._help,
            "--local": self._local,
            "--host": self._host,
            "--join": self._join,
            "--quit": self._quit,
        }

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

        msg: str = self.message_entry.get()
        self.message_entry.delete(0, END)

        if msg:

            for command, method in self.COMMANDS.items():
                if msg.startswith(command):
                    method(msg)
                    return

            if self.socket is None:
                # insert user message
                self.log("User: {msg}\n\n".format(msg=msg))

                # generate and insert bot message
                msg = ps(msg)
                category: str = fc(msg)
                subject: str = fs(msg)
                response: str = gs(category, subject)
                self.log("Customer Service: {response}\n\n".format(response=response))

    def log(self, msg: str) -> None:
        """
        logs a message to the text box
        :param msg: message that the user wants on the text box
        :return None:
        """
        self.chat_log.configure(state=NORMAL)
        self.chat_log.insert(END, "{msg}".format(msg=msg))
        self.chat_log.configure(state=DISABLED)
        self.chat_log.see(END)

    def _help(self, _command: str) -> None:
        """
        Displays user commands
        :param str _command: command pass through for command specific functionality
        :return None:
        """
        self.log(
            "Commands\n    --help\n    --local\n    --host <ip> <port>\n    --join <ip> "
            "<port>\n    --quit\n\n"
        )

    def _local(self, _command: str) -> None:
        """
        Converts chatbot into local process (user and computer)
        :param str _command: command pass through for command specific functionality
        :return None:
        """
        self._close_socket()

    def _host(self, _command: str) -> None:
        """
        Converts chatbot into socket process (computer and computer)
        :param str _command: command pass through for command specific functionality
        :return None:
        """
        self._close_socket()
        address = _command.split(" ")
        ip: str = (
            socket.gethostbyname(socket.gethostname())
            if address[1] == "local"
            else address[1]
        )
        port: int = int(address[2])
        self.socket = Socket("HOST", ip, port)

    def _join(self, _command: str) -> None:
        """
        Converts chatbot into socket process (computer and computer)
        :param str _command: command pass through for command specific functionality
        :return None:
        """
        self._close_socket()
        address = _command.split(" ")
        ip: str = (
            socket.gethostbyname(socket.gethostname())
            if address[1] == "local"
            else address[1]
        )
        port: int = int(address[2])
        self.socket = Socket("CLIENT", ip, port)

    def _close_socket(self) -> None:
        """
        closes socket if connection is still up
        :return None:
        """
        if self.socket:
            self.socket.mainloop = False

    def _quit(self, _command: str) -> None:
        """
        Exits application
        :param str _command: is not used for function
        :return None:
        """
        self.root.destroy()


if __name__ == "__main__":
    app = ChatApplication()
    app.root.mainloop()
