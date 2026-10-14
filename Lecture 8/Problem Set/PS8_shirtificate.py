#Import relevant libraries
from fpdf import FPDF

#Define shirt class
class Shirt:
    def __init__(self, title, text, photo, orientation="portrait", format="a4"):
        self.title = title
        self.text = text
        self.photo = photo
        self.orientation = orientation
        self.format = format

    def generate(self, filename):
        shirt = FPDF(orientation=self.orientation, format=self.format)
        shirt.set_font("helvetica", style="B", size=40)
        shirt.add_page()
        shirt.cell(0, 60, self.title, align="C", new_x="LMARGIN",new_y="NEXT")
        shirt.image(self.photo, x=10, y=60, w=190)
        shirt.set_font("helvetica", style="B", size=24)
        shirt.set_text_color(255, 255, 255)
        shirt.cell(0, 100, self.text, align="C")
        shirt.output(filename)

#Define main function
def main():
    title = "CS50 Shirtificate"
    photo = "shirtificate.png"
    filename = "shirtificate.pdf"
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    text = f"{first_name} {last_name} took CS50"
    new_shirt = Shirt(title, text, photo)
    new_shirt.generate(filename)
    print(f"Your shirt for {first_name} is ready!")

#Call main function when appropriate
if __name__ == "__main__":
    main()

