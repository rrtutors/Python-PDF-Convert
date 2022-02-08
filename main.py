
from fpdf import FPDF
from tkinter import*
from tkinter import filedialog

def convert():
 pdf = FPDF()
 pdf.add_page()
 pdf.set_font("Arial", size=12)
 f = open(fname, "r")
 for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='L')
 pdf.output("Text_to_Python.pdf")
 msgForGenerate.set("Text converted to PDF successfully!!!")

def UploadAction():
    filename = filedialog.askopenfilename(filetypes =[('Text Files', '*.txt')])
    msgForUpload.set("Uploaded:"+filename)
    global fname
    fname=filename
root =Tk()
root.geometry("600x200")
root.title("Convert Text to PDF")
global msgForUpload
global msgForGenerate
msgForUpload=StringVar()
msgForGenerate=StringVar()
Label(root,text="Hello",textvariable=msgForUpload,font="Arial 12",fg="green").place(x=80,y=30)
Button(root, text='Select Txt file', command=UploadAction,font="Arial 12 bold",width="12", bg="gray").place(x=80,y=70)
Button(root,text="Convert to PDF",font="Arial 12 bold",width="12",command=convert,bg="gray").place(x=350,y=70)
Label(root,text="Hello",textvariable=msgForGenerate,font="Arial 12",fg="green").place(x=80,y=120)
root.mainloop()
