import streamlit as st

#Points
a=0

st.title("Modern Swayam-War")

#Name
name=st.text_input("Name")
name=name.lower()
if (name.startswith('a') or name.startswith('c') or name.startswith('d') or name.startswith('e') or name.startswith('f') or name.startswith('g')):
    a-=1
else:
    a+=1

#Religion
Religion=st.selectbox('Religion',('Hindu','Muslim','Christian','Others'))
if Religion == "Hindu":
    a+=1
else:
    a-=1

#Height
height=st.number_input("Height")
if height>=173:
    a+=1
else:
    a-=1

#Mother Toungue
mt=st.selectbox('Mother Toungue',('Hindi','Kannada','Telugu','Tamil','Malayalam','Urdu','Tulu','Konkani','Marati','Bengali','Bihari','Punjabi','Gujurati','Assamese'))
if mt == "Kannada":
    a+=1
else:
    a-=1

#Favourite Pet
f=st.selectbox('Favourite Pet',('Dog','Cat','Birds','Rabbit','Hamster','Others'))
if f == "Dog":
    a+=1
else:
    a-=1

#Food Habitat
food=st.selectbox("Food Habitat",('Vegetarian','Non-Vegetarian','Eggitarian'))
if food=="Non-Vegetarian":
    a+=1
else:
    a-=1


#Validation
if st.button('Submit'):
    st.write(a)

    if a>=4:
        st.balloons()
        st.header("It's a Match")
        st.write("Contact her:+919481804500")
    else:
        st.write("Thank You")