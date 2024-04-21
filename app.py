import streamlit as st

def Largestamong3(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("TDS Graded Assignment week8")
    st.write("Enter three numbers.")

    num1 = st.number_input("First number:", step=1.0)
    num2 = st.number_input("Second number:", step=1.0)
    num3 = st.number_input("Third number:", step=1.0)

    if st.button("Find Largest"):
        largest = Largestamong3(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()