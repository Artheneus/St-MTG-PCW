import streamlit as st

# st.header("Card Price Comparison Magic the Gathering")

def main():

    navbar_top = """
            <nav class="navbar">
            <a href="" class="logo">Professor Suhu</a>
            <div class="menu">
                <a href=#>Oke</a>
                <a href=#>Oke</a>
                <a href=#>Oke</a>
                <a href=#>Oke</a>
            </div>
        </nav>
        """


    # title of the web
    st.title("Magic the Gathering Price Comparison Website")
    st.write("the fastest way to compare your Magic the Gathering cards through 3 biggest marketplace")

    
    st.markdown(navbar_top, unsafe_allow_html=True)
    # adding css
    with open('style/style.css') as f :
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#     hide_st_style = """
#                 <style>
#                 #Mainmenu {visibility: hidden;}
#                 footer {visibility: hidden;}
#                 </style>
#     """
   
    
if __name__ == '__main__':
     main()