import mysql.connector
import streamlit as st


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="PythonCrud"
)
mycursor=mydb.cursor()
print("Connection ok")

def main():
    st.title("CRUD ok")
    option=st.sidebar.selectbox("Select an Option",("Create","Read","Update","Delete"))

    if option=="Create":
        st.subheader("Create record")
        name=st.text_input("Enter Name");
        email=st.text_input("Enter Email");
        if st.button("Create"):
            sql="insert into users(name,email) values(%s,%s)"
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully")
    elif option=="Read":
        st.subheader("Read Record")
        mycursor.execute("select * from users")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option=="Update":
        st.subheader("Update Record")
        id=st.text_input("Enter Id");
        name=st.text_input("Enter New Name");
        email=st.text_input("Enter New Email");
        if st.button("Update"):
            sql="update users set name=%s,email=%s where id=%s"
            val=(name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully")


    elif option=="Delete":
        st.subheader("Delete Record")
        id=st.text_input("Enter Id");
        if st.button("Delete"):
            sql="Delete from users where id=%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Delete Successfully")



if __name__ =="__main__":
    main()