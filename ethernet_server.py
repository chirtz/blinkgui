#!/usr/bin/env python3.4

import socket
import sys
import threading
import blinkconfig
from avrconnector import AVRConnector, ConnectionType

HOST = blinkconfig.getstring("ethernet_host")
PORT = blinkconfig.getint("ethernet_port")


class EthernetConnector:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((HOST, PORT))
            self.socket.listen(10)
            while True:
                conn, addr = self.socket.accept()
                t = threading.Thread(target=self.client_thread, args=(conn,))
                t.start()
            self.socket.close()
        except socket.error as msg:
            print("Bind failed. Error Code : " + str(msg))
            sys.exit()

    def client_thread(self, conn):
        while True:
            data = conn.recv(39)
            avr_connector.write(data)
            if not data:
                break
        conn.close()


if __name__ == "__main__":
    avr_connector = AVRConnector()
    avr_connector.connect(ConnectionType.usb)
    connector = EthernetConnector()

