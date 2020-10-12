# Benjamin Kruskamp
# Created some functions to test and check whether the state of the engine,
# radio and window were changing, as well as a function to check if the
# text file is being created with the correct values.

class car:
    def __init__(self):
        self._engine = 0
        self._radio = 0
        self._window = 0

    def get_engine(self, a):
        # a = int(input("Enter: "))
        if a == 1:
            self._engine == 1
            print("\nThe engine is purring.")
            return a
        elif a == 0:
            self._engine == 0
            print("\nThe engine is off.")
            return a

    def get_radio(self, b):
        # b = int(input("Enter: "))
        if b == 1:
            self._radio == 1
            print("\nSome tunes are playing.")
            return b
        elif b == 0:
            self._radio == 0
            print("\nThe radio is off.")
            return b

    def get_window(self, c):
        # c = int(input("Enter: "))
        if c == 1:
            self._window == 1
            print("\nFresh air is filling the car.\n")
            return c
        elif c == 0:
            self._window == 0
            print("\nThe window is closed.\n")
            return c

    def get_menu(self):
        with open("test.txt", "w") as f:
            f.write("engine:0")
            f.write("\n")
            f.write("radio:0")
            f.write("\n")
            f.write("window:0")
            f.write("\n")
        while True:
            print("1: Interact with car.")
            print("2: Check state of car.")
            print("3: Quit.")
            x = int(input("\n"))
            while x != 1 and x != 2 and x != 3:
                x = int(input("\nPlease enter 1, 2, or 3: "))
            else:
                if x == 1:
                    usrinput()
                elif x == 2:
                    current_state()
                elif x == 3:
                    print("\nGoodbye.")
                    break


def usrinput():
    searchfor1 = "engine:"
    searchfor2 = "radio:"
    searchfor3 = "window"
    engine = input("\nEnter 1 to turn on the engine or 0 to turn it off. ")
    radio = input("\nEnter 1 to turn on the radio or 0 to turn it off. ")
    window = input("\nEnter 1 to roll down the window or 0 to close it. ")

    with open("test.txt", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        # file_to_write.truncate()
        for line in lines:
            if line.startswith(searchfor1):
                line = line[:7] + engine + "\n"

            elif line.startswith(searchfor2):
                line = line[:6] + radio + "\n"

            elif line.startswith(searchfor3):
                line = line[:7] + window + "\n"

            file_to_write.write(line)
    print("\n")


def current_state():
    searchfor1 = "engine:"
    searchfor2 = "radio:"
    searchfor3 = "window"
    with open("test.txt", 'r') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        # file_to_write.truncate()
        for line in lines:
            if line.startswith(searchfor1):
                a = int(line[7])
                newcar.get_engine(a)

            elif line.startswith(searchfor2):
                b = int(line[6])
                newcar.get_radio(b)

            elif line.startswith(searchfor3):
                c = int(line[7])
                newcar.get_window(c)


newcar = car()


def main():
    newcar.get_menu()


def test_if_running():
    print(newcar.get_engine(0))


def test_read():
    with open("test.txt", 'r') as file_to_write:
        lines = file_to_write.readlines()
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()

# test_read()
# test_if_running()