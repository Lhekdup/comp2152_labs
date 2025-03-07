import platform
import socket
import os
import sys

print("Machine Type")
print(platform.machine())

print("Processor Type")
print(platform.architecture())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout in seconds")
print(socket.getdefaulttimeout())

print("OS Type:")
print(os.name)
print("OS Name:")
print(platform.system())

print("Current PID")
print(os.getpid())

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] Opened file_handle: {file_handle}")

file_object_TextI0 = os.fdopen(file_handle, "w+")
file_object_TextI0.write("Some string to write to the file")
file_object_TextI0.flush()

pid = os.fork()

if pid == 0:
    print(f"\n[Child Process {os.getpid()}], [Parent Process {os.getpid()}]")
    os.lseek(file_handle, 0, 0)

    print(f"[ File Content: {os.read(file_handle, 100).decode()}]")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\n[Parent Process {os.getppid()}], [Child Process {pid}]")
    print("Wait for the child process to finish it's task")
    os.wait()
    print("The child process were able to finish it's task")
    file_object_TextI0.close()

print(f"\n[Process {os.getpid()}], File Closed. Exiting now..")
sys.exit(0)


