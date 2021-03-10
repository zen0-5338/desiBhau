from botCredentials import TOKEN
from botClass import DesiBhauClient

runningInstance = DesiBhauClient()

try:
    runningInstance.run(TOKEN)

except Exception as runtimeException:
    print(runtimeException)
