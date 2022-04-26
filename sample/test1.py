# -*- coding: utf-8 -*-
# Author: Shinsuke Ogata
 
import sys
import traceback
import time
import bluetooth
import threading

class SocketThread(threading.Thread):
    '''
    @param client_socket accept の結果返ってきたクライアントソケット.
    @param notify_receive シリアル通信で受信したデータを処理する関数・メソッド.
    @param notify_error エラー時の処理を実行する関数・メソッド
    '''
    def __init__(self, server_socket, client_socket, notify_receive, notify_error, debug):
        super(SocketThread, self).__init__()
        self._server_socket = server_socket
        self._client_socket = client_socket
        self._receive = notify_receive
        self._error = notify_error
        self._debug = debug

    def run(self):
        while True:
            try:
                data = self._client_socket.recv(1024)
                if self._receive != None:
                    self._receive(data)
            except KeyboardInterrupt:
                self._client_socket.close()
                self._server_socket.close()
                break
            except bluetooth.btcommon.BluetoothError:
                self._client_socket.close()
                self._server_socket.close()
                if self._debug:
                    print('>>>> bluetooth.btcommon.BluetoothError >>>>')
                    traceback.print_exc()
                    print('<<<< bluetooth.btcommon.BluetoothError <<<<')
                break
            except:
                self._client_socket.close()
                self._server_socket.close()
                if self._debug:
                    print('>>>> Unknown Error >>>>')
                    traceback.print_exc()
                    print('<<<< Unknown Error <<<<')
                break

class BluetoothServer(threading.Thread):

    '''
    @param notify_receive シリアル通信で受信したデータを処理する関数・メソッド.
    @param notify_error エラー時の処理を実行する関数・メソッド
    @param debug デバッグメッセージを出すときTrue をセット
    '''
    def __init__(self, notify_receive, notify_error=None, debug=False):
        super(BluetoothServer, self).__init__()
        self._port =1
        self._receive = notify_receive
        self._error = notify_error
        self._server_socket = None
        self._debug = debug

    def run(self):
        try:
            self._server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

            if self._debug:
                print("BluetoothServer: binding...")

            self._server_socket.bind( ("",self._port ))

            if self._debug:
                print("BluetoothServer: listening...")

            self._server_socket.listen(1)

            client_socket,address = self._server_socket.accept()

            if self._debug:
                print("BluetoothServer: accept!!")
            task = SocketThread(self._server_socket, client_socket, self._receive, self._error, self._debug)
            task.start()
        except KeyboardInterrupt:
            if self._debug:
                print("BluetoothServer: KeyboardInterrupt")
        except:
            if self._debug:
                print('>>>> Unknown Error >>>>')
                traceback.print_exc()
                print('<<<< Unknown Error <<<<')
 
 
def receive(data):
   print("receive [%s]" % data)
 
def error(data):
    print("error")

if __name__ == '__main__':
    task = BluetoothServer(receive, error, True)
    task.start()
