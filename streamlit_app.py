#print("Hello World")
import streamlit as srt
srt.title("App by PS")
a=srt.number_input("Enter number a")
b=srt.number_input("Enter number b")
c=srt.number_input("Enter number c")
srt.write("The biggest number is "+str(max(a,b,c)))
def text(text,col,bgcolor):
  srt.markdown(f"<p style='background-color:{bgcolor}; color:{col}'>{text}</p>" unsafe_html_allow=True )
text("Thank you for using my APP","#FFFFFF","#000000")
