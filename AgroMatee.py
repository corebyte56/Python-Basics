# AgroMate - A simple crop disease info system (Python version)
# File handling + User authentication + Menu system

class User:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    # Registration function
    def register_user(self):
        print("Register a new user.")
        new_user = input("Enter new username: ")
        new_pass = input("Enter new password: ")

        self.username = new_user
        self.password = new_pass

        with open("AgroMate.txt", "a") as file:
            file.write(f"{self.username} {self.password}\n")

        print("Registration successful! You can now log in with your new credentials.\n")

    # Login function
    def login_user(self):
        input_user = input("Enter username: ")
        input_pass = input("Enter password: ")

        try:
            with open("AgroMate.txt", "r") as file:
                for line in file:
                    file_user, file_pass = line.strip().split()
                    if file_user == input_user and file_pass == input_pass:
                        print("Login successful!\n")
                        return True
        except FileNotFoundError:
            print("No registered users found. Please register first.\n")
            return False

        print("Invalid username or password. Please try again.\n")
        return False

    # Harvest menu function
    def harvest_menu(self):
        print("Harvest Menu:")
        print("""
1. Rice
2. Wheat
3. Sugarcane
4. Corn
5. Jute
6. Potato
7. Tomato
8. Watermelon
""")

        choice1 = int(input("Enter your choice: "))

        if choice1 == 1:
            print("\nYou selected Rice:")
            print("1. Bacterial Leaf Blight\n2. Blast")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nWater-soaked yellow-brown lesions on leaves.")
                print("Solution:\nUse resistant varieties and disease-free seeds.")
            elif choice2 == 2:
                print("\nSymptoms:\nDiamond-shaped lesions with gray centers.")
                print("Solution:\nUse fungicide and resistant varieties.")
            else:
                print("Invalid choice.")

        elif choice1 == 2:
            print("\nYou selected Wheat:")
            print("1. Rust\n2. Powdery Mildew")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nOrange-red pustules on leaves.")
                print("Solution:\nUse resistant varieties and fungicide.")
            elif choice2 == 2:
                print("\nSymptoms:\nWhite powdery fungal growth.")
                print("Solution:\nProper spacing and timely fungicide.")
            else:
                print("Invalid choice.")

        elif choice1 == 3:
            print("\nYou selected Sugarcane:")
            print("1. Red Rot\n2. Smut")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nReddening and rotting of stalk.")
                print("Solution:\nUse disease-free material and crop rotation.")
            elif choice2 == 2:
                print("\nSymptoms:\nBlack whip-like structures on top.")
                print("Solution:\nUse disease-free seeds and fungicide.")
            else:
                print("Invalid choice.")

        elif choice1 == 4:
            print("\nYou selected Corn:")
            print("1. Northern Leaf Blight\n2. Anthracnose")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nOblong lesions on leaves.")
                print("Solution:\nResistant hybrids and fungicide.")
            elif choice2 == 2:
                print("\nSymptoms:\nBrown lesions and stalk rot.")
                print("Solution:\nCrop rotation and residue management.")
            else:
                print("Invalid choice.")

        elif choice1 == 5:
            print("\nYou selected Jute:")
            print("1. Jute Mosaic\n2. Root-Knot")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nYellow patches and stunted growth.")
                print("Solution:\nUse clean seeds and control whiteflies.")
            elif choice2 == 2:
                print("\nSymptoms:\nRoot galls and wilting.")
                print("Solution:\nCrop rotation and biological control.")
            else:
                print("Invalid choice.")

        elif choice1 == 6:
            print("\nYou selected Potato:")
            print("1. Black Scurf\n2. Bacterial Wilt")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nBlack patches on tubers.")
                print("Solution:\nTreat seeds before planting.")
            elif choice2 == 2:
                print("\nSymptoms:\nSudden wilting and brown stem tissue.")
                print("Solution:\nUse resistant varieties and crop rotation.")
            else:
                print("Invalid choice.")

        elif choice1 == 7:
            print("\nYou selected Tomato:")
            print("1. Leaf Curl Virus\n2. Damping Off")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nUpward curling leaves and stunted plants.")
                print("Solution:\nControl whiteflies and remove infected plants.")
            elif choice2 == 2:
                print("\nSymptoms:\nSeedlings collapse after emergence.")
                print("Solution:\nUse sterilized soil and good drainage.")
            else:
                print("Invalid choice.")

        elif choice1 == 8:
            print("\nYou selected Watermelon:")
            print("1. Fusarium Wilt\n2. Gummy Stem Blight")
            choice2 = int(input("Choose disease: "))

            if choice2 == 1:
                print("\nSymptoms:\nYellowing and wilting of leaves.")
                print("Solution:\nCrop rotation and treat soil before planting.")
            elif choice2 == 2:
                print("\nSymptoms:\nBrown spots with gummy ooze.")
                print("Solution:\nUse disease-free seeds and fungicide.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid crop choice.")

        print("\nThank you for using AgroMate!\n")

    # Feedback function
    def feedback(self):
        print("Please provide your feedback about AgroMate:")
        print("1. Excellent\n2. Good\n3. Average\n4. Poor")
        fb = int(input("Enter your choice: "))

        if fb == 1:
            print("Thank you for your excellent feedback!")
        elif fb == 2:
            print("Thank you for your good feedback!")
        elif fb == 3:
            print("Thank you for your average feedback!")
        elif fb == 4:
            print("Thank you! We will strive to improve.")
        else:
            print("Invalid choice.")


# Main program
def main():
    print("Welcome to AgroMate!")
    print("Please log in to continue.")
    farmer = User()

    print("1. Register\n2. Log in")
    choice = int(input("Enter choice: "))

    if choice == 1:
        farmer.register_user()
        print("Please log in to continue.")
        if farmer.login_user():
            farmer.harvest_menu()
            farmer.feedback()

    elif choice == 2:
        if farmer.login_user():
            farmer.harvest_menu()
            farmer.feedback()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
