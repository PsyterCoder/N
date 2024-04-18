#print("Hello World")
import streamlit as srt
srt.title("App by PS")
srt.markdown("<style> -appview-container.css-cc9aqqtcatxzadr5pjc9co {background-image:linear-gradient(Azure,RoyalBlue); color:#FFFFFF'}</style>", unsafe_allow_html=True )
a=srt.number_input("Enter number a")
b=srt.number_input("Enter number b")
c=srt.number_input("Enter number c")
srt.write("The biggest number is "+str(max(a,b,c)))
def text(text,col,bgcolor):
  srt.markdown(f"<p style='background-color:#000000; color:#0000FF'>{text}</p>", unsafe_allow_html=True )
text("Thank you for using my APP","#FFFFFF","#000000")
def gradientText(Text):
  srt.markdown(f"<p style='background-image:linear-gradient(Azure,RoyalBlue); color:#FFFFFF'>{Text}</p>", unsafe_allow_html=True )
gradientText("We are glad to help you , visit again ")
