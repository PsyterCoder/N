#print("Hello World")
import streamlit as srt
srt.title("App by PS")
a=srt.number_input("Enter number a")
b=srt.number_input("Enter number b")
c=srt.number_input("Enter number c")
srt.write("The biggest number is "+str(max(a,b,c)))

