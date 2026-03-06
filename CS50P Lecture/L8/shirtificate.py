from fpdf import FPDF
class Shirtificate(FPDF):
    #提示用户输入他们的名字（比如 "John Harvard"）。
    #生成一个名为 shirtificate.pdf 的文件。
    #PDF 顶部要有一行居中的大字："CS50 Shirtificate"。
    #下面要贴上那张 T 恤的图片。
    #用户的名字必须印在 T 恤的正中间（文字颜色最好是白色的，方便看清）。
    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(w=0, h=30, txt="CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    pdf = Shirtificate()
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=60,w=210 )
    pdf.set_text_color(r = 255, g = 255, b = 255)
    pdf.set_y(140)
    pdf.cell(w=0, h=10, txt=f'{name} took CS50', border=0, ln=0, align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()