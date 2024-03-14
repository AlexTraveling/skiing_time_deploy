import streamlit as sl


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

   sl.markdown('<h1 class="title">Sign Up</h1>',
               unsafe_allow_html=True)
   
   sl.markdown('<p class="direction">Username and password are required for a new account</p>',
               unsafe_allow_html=True)


def account_section():

   with sl.form('sign_up'):
      username = sl.text_input('New username')
      password = sl.text_input('New password', type='password', key='first_password')
      check_password = sl.text_input('Confirm password', type='password', key='second_password')

      if sl.form_submit_button('Sign up'):

         if username == '':
            sl.warning('Username empty')
         elif password == '':
            sl.warning('Password empty')
         elif check_password == '':
            sl.warning('Please confirm password')

         else:
            if password != check_password:
               sl.warning('Passwords are not same')

            else:
               sl.success('Sign up successfully')
               return True, username, password
   
   return False, None, None


def goto_login_section():

   sl.markdown('<br>', unsafe_allow_html=True)
   login_page_url = 'https://skiing-time-log-in.streamlit.app/'
   sl.markdown(f'[Back to log in]({login_page_url})')
   

# Sign up Page
def sign_up_page():

   page_name = 'Sign up · Skiing Time'
   page_icon = '❄️'
   sl.set_page_config(page_name, page_icon)

   title_section()
   account_section()
   goto_login_section()
   

if __name__ == "__main__":

   sign_up_page()