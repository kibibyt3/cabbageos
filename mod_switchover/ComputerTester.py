#!/usr/bin/python
import Computer

def main():
	newComputer = Computer.Computer(True, "dreamscape", "192.168.0.1", [], [], False, False)
	newComputer.loginScreen()

main()
