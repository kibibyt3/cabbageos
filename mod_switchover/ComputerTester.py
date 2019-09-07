#!/usr/bin/python3.6
import Computer
import Tools

def main():
	newComputer = Computer.Computer(True, "dreamscape", Tools.Tools.ipGen(), [], [], False, False)
	newComputer.loginScreen()

main()
