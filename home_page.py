import streamlit as sl
# import subprocess


# Top Section
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

   # col = sl.columns([1.6, 0.4, 0.8, 0.8, 2, 1])

   # with col[0]:
   #    # sl.text('SKIING TIME')
   #    logo_path = 'home_page_material/skiing_time_logo.png'
   #    sl.image(logo_path)

   # with col[2]:
   #    help_page_url = 'https://skiing-time-assist.streamlit.app/'
   #    sl.markdown(f'[Help]({help_page_url})')
   
   # with col[3]:
   #    about_us_page_url = 'https://skiing-time-about-us.streamlit.app/'
   #    sl.markdown(f'[About us]({about_us_page_url})')

   # with col[5]:
   #    login_page_url = 'https://skiing-time-log-in.streamlit.app/'
   #    sl.markdown(f'[Log in]({login_page_url})')

   column = sl.columns([1, 1, 1, 2, 2])

   with column[0]:
      login_page_url = 'https://skiing-time-log-in.streamlit.app/'
      sl.markdown(f'[Log in]({login_page_url})')

   with column[1]:
      help_page_url = 'https://skiing-time-assist.streamlit.app/'
      sl.markdown(f'[Help]({help_page_url})')
   
   with column[2]:
      about_us_page_url = 'https://skiing-time-about-us.streamlit.app/'
      sl.markdown(f'[About us]({about_us_page_url})')
   
   with column[4]:
      # sl.text('SKIING TIME')
      logo_path = 'home_page_material/skiing_time_logo.png'
      sl.image(logo_path)



# Title Section
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


# Goto Use Section
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

   # if_goto_login = sl.button('Try Skiing Time Now')

   # if if_goto_login:

   #    information = f'nothing'

   #    subprocess.Popen(["streamlit", 
   #                      "run", 
   #                      "login_page.py", 
   #                      "information", 
   #                      f"{information}"])

   login_page_url = 'https://skiing-time-log-in.streamlit.app/'
   sl.markdown(f'[Log in]({login_page_url})')


# Demonstration Section
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

   demonstration_video_path = 'home_page_material/small_demo_vlog.m4v'
   sl.video(demonstration_video_path)


# Help Section
def help_section_title():

   sl.markdown('''

   <br>

   <h1 class="title">
      Easier than Easier to Use
   </h1>

   <br>

   <p class="describe">
      Just three steps to use Ai Searching of Skiing Time
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
   

# Help 1: Time and resort
def help_section_1():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.title('Choose Date and Resort')
      sl.write('Enjoy all photos after choosing specific date and resort in Gallery Page. Then you may click button of Go Ai Searching to use it.')

   with column[1]:
      sl.image('home_page_material/gallery.png')


# Help 2: Upload one photo
def help_section_2():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.title('Upload One Old Photo')
      sl.write('System can analyze which part of photos belong to you automatically by the marvelous CLIP deep learning model.')
      # sl.caption('System can analyze which part of photos belong to you automatically by the CLIP deep learning model.')


   with column[1]:
      sl.image('home_page_material/upload.png')


# Help 3: Select and download photo after AI searching
def help_section_3():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.title('Download Your Checked Photos')
      sl.write('Take the further selection after AI searching and download all photos.')
      sl.write('You may also use the Threshold Slider to adjust threshold inside CLIP deep learning model. Upper brings better accuracy and lower brings better completness.')

   with column[1]:
      sl.image('home_page_material/download.png')


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


# Page Structure
def home_page():

   page_name = 'Home · Skiing Time'
   sl.set_page_config(page_name)

   top_section()

   title_section()
   # goto_use_section()
   demonstration_section()

   sl.markdown('---')

   help_section_title()
   help_section_1()
   help_section_2()
   help_section_3()

   information()

   bottom_section()


if __name__ == '__main__':

   home_page()