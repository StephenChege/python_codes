"""A python program to Find and Print Hostname or Device Name using
socket module."""

#Import socket library
import socket

#Function to find and print the Hostname or Device name
def HostName():
  try:
    host_name = socket.gethostname()
    print("Hostname or Device Name: ", host_name)
  except:
    print('Unable to get Hostname and IP')

#Calling the function
HostName()
