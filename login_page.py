import streamlit as sl
import time
import subprocess
# import pandas as pd
import openpyxl

# if use MySQL as database
# from userDatabase import get_user


def get_user_from_excel():

   # save = [('Alex', '123456'),
   #         ('Bob', 'iambob'),
   #         ('Swing', 'swing')]

   path = 'user_database.xlsx'
   book = openpyxl.load_workbook(path)
   sheet = book['Sheet1']
   rows = sheet.iter_rows(values_only=True)
   print(rows)

   save = []
   for r in rows:
      save.append(r)

   save = save[1:]
   print(save)
   
   return save


def user_account(username, password):

   # use local python file as database
   # save = [('Alex', '123456'),
   #         ('Bob', 'iambob'),
   #         ('Swing', 'swing')]

   # use MySQL as database
   # save = get_user()

   # use Excel as database
   save = get_user_from_excel()
   
   if (username, password) in save:
      return True
   else:
      return False


def title_section():

   sl.markdown('''
   <style>
   .title {
      text-align: center;
   }
   
   .direction {
      text-align: center;
   }
   <style>
   ''', unsafe_allow_html=True)

   sl.markdown('<h1 class="title">Log in</h1>',
               unsafe_allow_html=True)
   
   sl.markdown('<p class="direction">Find your amazing photos in amazing speed</p>',
               unsafe_allow_html=True)


def login_section():

   with sl.form('login'):
      username = sl.text_input('Username')
      password = sl.text_input('Password',
                               type='password')

      if sl.form_submit_button('Login'):
         if user_account(username, password):
            sl.success('Login successfully')
            time.sleep(2)
            return True, username
         else:
            sl.warning('Wrong username or password')
   
   return False, None


def goto_sign_up_section():

   # st-emotion-cache-1umgz6k ef3psqc12

   sl.markdown('''
   <style>
   .st-emotion-cache-1umgz6k.ef3psqc12 {
      border-color: transparent;
      color: gray;
   }
   </style>''', unsafe_allow_html=True)

   col1, col2, col3 = sl.columns([1, 2, 1])
   with col2:
      sign_up_button = sl.button('Do not have a account ?  Sign up now', use_container_width=100)

   if sign_up_button:
      sl.warning('ready to sign up...')
      time.sleep(0.5)

      subprocess.Popen(["streamlit", 
                     "run", 
                     "sign_up_page.py", 
                     "none", 
                     f"{404}"])



# Skiing Time
      
if __name__ == '__main__':

   title_section()

   if_goto_upload_page, username = login_section()

   goto_sign_up_section()

   if if_goto_upload_page == True:

      subprocess.Popen(["streamlit", 
                        "run", 
                        "gallery_page.py", 
                        "username", 
                        f"{username}"])

      # subprocess.Popen(["streamlit", 
      #                   "run", 
      #                   "upload_page.py", 
      #                   "username", 
      #                   f"{username}"])

      # pass
