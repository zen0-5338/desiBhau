from botCredentials import TOKEN
from botClass import DesiBhauClient


runningInstance = DesiBhauClient()
runningInstance.run(token=TOKEN,reconnect=True)