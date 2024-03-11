import streamlit as sl
import subprocess


# Top section
def top_section():

   sl.markdown('''     
   <style>

   .title {
      text-align: center;
   }
   .describe {
      text-align: center;
      color: grey;
   }

   </style>

   ''', unsafe_allow_html=True)

   col = sl.columns([1.6, 0.4, 0.8, 0.8, 2, 1])

   with col[0]:
      # sl.text('SKIING TIME')
      logo_path = 'home_page_material/skiing_time_logo.png'
      sl.image(logo_path)

   with col[2]:
      sl.text('Help')
      # sl.button('Help')
   
   with col[3]:
      sl.text('About us')
      # sl.button('Aboud us')

   with col[5]:
      sl.text('Log in')
   
   pass

# Title section
def title_section():

   sl.markdown('''

   <br>

   <h1 class="title">
      A Faster Way to Search Your Amazing Skiing Photos
   </h1>

   <br>

   <p class="describe">
      Skiing Time app offers AI Searching to make photo selecting more convenient
   </p>

   <br>
               
   <style>

   .title {
      text-align: center;
   }
   .describe {
      text-align: center;
      color: grey;
   }

   </style>

   ''', unsafe_allow_html=True)


# Goto use section
def goto_use_section():

   sl.markdown('''
               
   <style>

   .st-emotion-cache-7ym5gk.ef3psqc12 {
      width: 80%;
      margin-left: 10%;
      # background: rgb(255, 75, 75);
      # border: 0px;
      # color: white;
   }

   </style>

   ''', unsafe_allow_html=True)

   if_goto_login = sl.button('Try Skiing Time Now')

   if if_goto_login:

      information = f'nothing'

      subprocess.Popen(["streamlit", 
                        "run", 
                        "login_page.py", 
                        "information", 
                        f"{information}"])
   



# Demonstration section
def demonstration_section():

   sl.markdown('''
               
   <br>
               
   <style>

   .stVideo {
      border-radius: 10px;
      autoplay: true;
   }

   </style>

   ''', unsafe_allow_html=True)

   demonstration_video_path = 'home_page_material/demonstration_video.mov'
   sl.video(demonstration_video_path)


def information():

   sl.markdown('---')

   column = sl.columns([0.2, 1, 1, 1, 1])

   with column[1]:
      sl.subheader('SITE')
      sl.caption('Home')
      sl.caption('Sign up')
      sl.caption('Log in')
      sl.caption('Gallery of photos')
      sl.caption('AI searching')
      sl.caption('Download')
      
   with column[2]:
      sl.subheader('TECH')
      sl.caption('Streamlit')
      sl.caption('Python 3')
      sl.caption('My SQL')
      sl.caption('CLIP model')
   
   with column[3]:
      sl.subheader('TEAM')
      sl.caption('ZXB · project manager')
      sl.caption('GZY · product manager')
      sl.caption('CZR · technical manager')
      sl.caption('ZWH · test manager')

   with column[4]:
      sl.subheader('SOCIAL')
      sl.caption('GitHub')
      sl.caption('CAU')
      sl.caption('Easthome')
      sl.caption('滑呗')
      sl.caption('GOSKI')
   

def bottom_section():

   sl.markdown('---')

   column = sl.columns([3, 2, 3])
   with column[1]:
      logo_path = 'home_page_material/skiing_time_logo.png'
      sl.image(logo_path)

   # sl.text('a web app for AI searching')
   sl.markdown('''

   <p class="bottom">
      a web app for AI searching of skiing photos developed by team Skiing Time of CAU
   </p>
   <p class="bottom">
      March 2024, Peking City
   </p>
      

   <br>
               
   <style>

   .title {
      text-align: center;
   }
   .bottom {
      text-align: center;
      color: lightgrey;
   }

   </style>

   ''', unsafe_allow_html=True)

   pass


# Page structure
def home_page():

   top_section()
   title_section()
   goto_use_section()
   demonstration_section()
   information()
   bottom_section()


if __name__ == '__main__':

   home_page()