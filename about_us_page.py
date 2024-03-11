import streamlit as sl

# from home_page import top_section, bottom_section


def title_section():

   sl.markdown('''
   <style>
   .title {
      text-align: center;
   }
   
   .direction {
      text-align: center;
   }
   </style>
   ''', unsafe_allow_html=True)

   sl.markdown('<h1 class="title">About Us</h1>',
               unsafe_allow_html=True)
   
   sl.markdown('<h4 class="direction">Who we are and what makes Skiing Time so marvelous</h4>',
               unsafe_allow_html=True)


def new_title_section():

   # st-emotion-cache-1n76uvr e1f1d6gn2

   sl.markdown('''
   <style>
   .box {
      border: 20px;
      background: lightblue;
      border-radius: 20px;
   }
   .title {
      # border: 20px;
      # background: gray;
      color: white;
   }
   .direction {
      text-align: center;
      color: white;
   }

   </style>
   ''', unsafe_allow_html=True)

   sl.markdown('<div class="box"><h1 class="title">About Us</h1><p class="direction">Who we are and what makes Skiing Time so marvelous in AI searching</p></div>',
               unsafe_allow_html=True)
   
   # sl.markdown('<p class="direction">Who we are and what makes Skiing Time so marvelous in AI searching</p>', unsafe_allow_html=True)

   


# Team section
def team_section():

   sl.title('Who We Are')
   sl.write('We are the Skiing Time team majoring in Computer Science from China Agricultural University, dedicated to the majority of ski enthusiasts to provide more convenient image search function.')
   sl.image('about_us_page_material/who_we_are.png')


# Member section
def member(name, job, work_list, portrait):

   column = sl.columns([50, 5, 45])
   
   with column[0]:
      sl.image(f'about_us_page_material/{portrait}.png')
   
   with column[2]:
      sl.header(name)
      sl.caption(job)
      sl.markdown('<br>', unsafe_allow_html=True)
      
      for work in work_list:
         sl.markdown(work, unsafe_allow_html=True)
      

def member_section():

   sl.title('Members of Skiing Time Team')
   sl.write('The team consists of four members from China Agricultral University.')
   # sl.image('about_us_page_material/who_we_are.png')

   sl.markdown('<br>',unsafe_allow_html=True)

   work_list = ['Overall management', 'Front-end development', 'Establishment of innovative project']
   member('Alex Zhao', 'Project Manager', work_list, 'zxb')

   work_list = ['Designing of software prototype', 'Interactive designing']
   member('Zhengyi Guo', 'Product Manager', work_list, 'gzy')

   work_list = ['Backend development', 'Deep learning model', 'Construction of Database']
   member('Zirui Chen', 'Technological Manager', work_list, 'czr')

   work_list = ['Software testing', 'Label of data for deep learning model']
   member('Wenhao Zhang', 'Project Manager', work_list, 'zwh')


# Technology section
def streamlit_part():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.header('Streamlit')
      sl.caption('Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.')
      sl.caption('Run a streamlit app by :')
      sl.code('streamlit run home_page.py')
      sl.markdown('[learn more about Streamlit](https://streamlit.io/)')

   with column[1]:
      sl.image('about_us_page_material/Streamlit.png')


def CLIP_part():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.header('CLIP')
      sl.caption('CLIP is a marvelous deep learning model developed by Open AI, providing the function of comparing the degree of similarity between two images.')
      sl.markdown('[learn more about CLIP](https://openai.com/research/clip)')

   with column[1]:
      sl.image('about_us_page_material/CLIP.png')


def MySQL_part():

   column = sl.columns([2, 3])
   
   with column[0]:
      sl.header('MySQL')
      sl.caption('MySQL is an open-source relational database management system. A relational database organizes data into one or more data tables in which data may be related to each other; these relations help structure the data.')
      sl.markdown('[learn more about MySQL](https://www.mysql.com/)')
      
   with column[1]:
      sl.image('about_us_page_material/MySQL.png')


def technology_section():

   sl.title('What Makes Skiing Time Marvelous')
   sl.write('Stack of advanced technology make Skiing Time the best app for AI searching of skiing photos.')
   # sl.image('about_us_page_material/who_we_are.png')
   
   sl.markdown('<br>', unsafe_allow_html=True)
   streamlit_part()

   sl.markdown('<br>', unsafe_allow_html=True)
   CLIP_part()

   sl.markdown('<br>', unsafe_allow_html=True)
   MySQL_part()


# About Us page
def about_us_page():

   # top_section()

   title_section()
   # new_title_section()
   sl.markdown('---')
   team_section()
   sl.markdown('---')
   member_section()
   sl.markdown('---')
   technology_section()

   # bottom_section()


if __name__ == '__main__':

   about_us_page()