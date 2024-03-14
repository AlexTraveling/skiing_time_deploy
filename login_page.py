import streamlit as sl
import time
import openpyxl

# if use MySQL as database
# from userDatabase import get_user


def get_user_from_excel():

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

   # use MySQL as database
   # save = get_user()

   # use Excel as database
   save = get_user_from_excel()
   
   if (username, password) in save:
      return True
   else:
      return False


# Title Section
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

   sl.markdown('<h1 class="title">Log in</h1>', unsafe_allow_html=True)
   sl.markdown('<p class="direction">Username and password are required to log in Skiing Time</p>', unsafe_allow_html=True)


# Information Input Section
def login_section():

   with sl.form('login'):
      username = sl.text_input('Username')
      password = sl.text_input('Password',
                               type='password')

      if sl.form_submit_button('Login'):
         
         if user_account(username, password):
            sl.success('Login successfully')
            time.sleep(0.5)
            gallery_page_url = 'https://skiing-time-gallery.streamlit.app/'
            sl.markdown(f'[Hello {username}, you may click here to use Skiing Time now]({gallery_page_url})')
            return True, username
         
         else:
            sl.warning('Wrong username or password')
   
   return False, None


# Go to Sign up Section
def goto_sign_up_section():

   sl.markdown('<br>', unsafe_allow_html=True)
   sign_up_page_url = 'https://skiing-time-sign-up.streamlit.app/'
   sl.markdown(f'Do not have a account ? [Sign up now]({sign_up_page_url})')
   

# Log in Page
def login_page():

   page_name = 'Log in · Skiing Time'
   page_icon = '❄️'
   sl.set_page_config(page_name, page_icon)

   title_section()
   if_goto_gallery_page, username = login_section()

   goto_sign_up_section()
      

if __name__ == '__main__':

   login_page()