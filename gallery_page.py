import streamlit as sl
from PIL import Image
# import sys
# import subprocess
import openpyxl


# Sidebar Section
def sidebar_section(username):

   sl.sidebar.header('Information')
   date = sl.sidebar.date_input('Date')
   resort_list = ['Wanlong Holiday Paradise',
                     'Genting Yunding Garden',
                     'Thaiwood Ski Resort']
   resort = sl.sidebar.radio('Resort', resort_list)

   sl.markdown('''
   <style>
               
   .st-emotion-cache-13ejsyy.ef3psqc12 {
      width: 100%;
   }
               
   </style>
   ''', unsafe_allow_html=True)

   sl.sidebar.markdown('<br><br>', unsafe_allow_html=True)

   # Goto AI Searching button
   sl.sidebar.header('Find my photos')
   # if_goto_next = sl.sidebar.button('Go AI Searching')
   ai_search_page_url = 'https://skiing-time-ai-search.streamlit.app/' 
   sl.sidebar.markdown(f'[AI Search]({ai_search_page_url})')
   
   # if if_goto_next:
   #    information = f'{username}∆{date}∆{resort}'
   #    subprocess.Popen(["streamlit", 
   #                      "run", 
   #                      "upload_page.py", 
   #                      "information", 
   #                      f"{information}"])
   
   sl.sidebar.markdown('<br><br>', unsafe_allow_html=True)
   
   # Goto Help Page button
   sl.sidebar.header('How to use')
   # if_goto_help_page = sl.sidebar.button('Help')
   help_page_url = 'https://skiing-time-assist.streamlit.app/' 
   sl.sidebar.markdown(f'[Help]({help_page_url})')

   # if if_goto_help_page:
   #    information = f'nothing'
   #    subprocess.Popen(["streamlit", 
   #                      "run", 
   #                      "help_page.py", 
   #                      "information", 
   #                      f"{information}"])

   # Goto About Us button
   # if_goto_about_us_page = sl.sidebar.button('About Us')
   about_us_page_url = 'https://skiing-time-about-us.streamlit.app/'
   sl.sidebar.markdown(f'[About us]({about_us_page_url})')
   
   # if if_goto_about_us_page:
   #    information = f'nothing'
   #    subprocess.Popen(["streamlit", 
   #                      "run", 
   #                      "about_us_page.py", 
   #                      "information", 
   #                      f"{information}"])
   
   return date, resort


# Title Section
def title_section(date, resort):

   sl.markdown('<h1>Gallery of Skiing Photos</h1>', unsafe_allow_html=True)

   pass


# Full List
def open_excel():

   path = 'image_catalog_database.xlsx'
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


# Select Section
def resort_adjust(resort):

   resort_list = [('Wanlong Holiday Paradise', 'wanlong'),
                  ('Genting Yunding Garden', 'yunding'),
                  ('Thaiwood Ski Resort', 'thaiwood')]
   
   for single in resort_list:
      if single[0] == resort:
         return single[1]
   
   return None


def select_section(date, resort, full_list):

   date = str(date)
   resort_short_name = resort_adjust(resort)

   # if use MySQL as database
   # image_catalog_list = select_image_catalog(date, resort_short_name, only_id=True)

   # if use Excel as database
   image_catalog_list = []
   for single in full_list:
      if single[1] == date and single[2] == resort_short_name:
         image_catalog_list.append(single[0])

   image_sum = len(image_catalog_list)

   if image_sum == 0:
      sl.warning(f'Amount to {image_sum} photos ｜ {date} ｜ {resort}')
   else:
      sl.success(f'Amount to {image_sum} photos ｜ {date} ｜ {resort}')

   return image_catalog_list


# Show Section
def id_to_PIL(image_catalog_list):

   PIL_list = []

   for image_index in image_catalog_list:
      image_path = f'image_catalog/image_{image_index}.jpg'
      image = Image.open(image_path)
      PIL_list.append(image)

   return PIL_list


def small_PIL(before):

   after = []
   limit_width = 600.0
   
   for single in before:
      
      width, height = single.size

      if width >= limit_width:

         height = (limit_width / width) * height
         width = limit_width
         height = int(height)
         width = int(width)
         after.append(single.resize((width, height)))
      
      else:

         after.append(single)
   
   return after


def show_section(image_catalog_list):

   PIL_list = id_to_PIL(image_catalog_list)
   PIL_list = small_PIL(PIL_list)

   if len(PIL_list) != 0:

      col1, col2, col3 = sl.columns(3)
      column = 1

      for PIL in PIL_list:

         if column == 1:
            with col1:
               sl.image(PIL)

         elif column == 2:
            with col2:
               sl.image(PIL)
         
         elif column == 3:
            with col3:
               sl.image(PIL)

         column += 1
         if column == 4:
            column = 1


def gallery_page():

   page_name = 'Gallery · Skiing Time'
   page_icon = '❄️'
   sl.set_page_config(page_name, page_icon)

   # username = user_information_section()
   username = 'unknown'

   date, resort = sidebar_section(username)
   title_section(date, resort)
   full_list = open_excel()
   image_catalog_list = select_section(date, resort, full_list)
   show_section(image_catalog_list)


if __name__ == '__main__':

   gallery_page()