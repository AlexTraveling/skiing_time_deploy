import streamlit as sl
import time
import torch
from PIL import Image
from transformers import AutoProcessor, CLIPModel
import torch.nn as nn
import openpyxl


# @sl.cache_resource
# @sl.cache_data()
@sl.cache(suppress_st_warning=True)
def CLIP(a, b):

   # device = torch.device('cuda' if torch.cuda.is_available else "cpu")
   device = 'cpu'

   processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")
   model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
   
   image1 = a
   with torch.no_grad():
      inputs1 = processor(images=image1, return_tensors="pt").to(device)
      image_features1 = model.get_image_features(**inputs1)
   
   image2 = b
   with torch.no_grad():
      inputs2 = processor(images=image2, return_tensors="pt").to(device)
      image_features2 = model.get_image_features(**inputs2)
   
   # Compute their cosine similarity and convert it into a score between 0 and 1
   cos = nn.CosineSimilarity(dim=0)
   sim = cos(image_features1[0],image_features2[0]).item()
   sim = (sim+1)/2

   print('done.')

   return sim


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

   image_catalog_list = []
   for single in full_list:
      if single[1] == date and single[2] == resort_short_name:
         image_catalog_list.append(single[0])

   image_sum = len(image_catalog_list)

   return image_catalog_list


def sidebar_section(full_list):

   # header
   sl.sidebar.header('Information')

   # date
   date = sl.sidebar.date_input('Date')

   # resort
   resort_list = ['Wanlong Holiday Paradise',
                  'Genting Yunding Garden',
                  'Thaiwood Ski Resort']
   resort = sl.sidebar.radio('Resort', resort_list)

   # select
   image_catalog_list = select_section(date, resort, full_list)
   if len(image_catalog_list) == 0:
      sl.sidebar.warning('No photo found')
   else:
      sl.sidebar.success(f'Amount to {len(image_catalog_list)} photos.')

   # upload photo
   upload_file = sl.sidebar.file_uploader('Upload old skiing photo', type=['jpg', 'png'])
   if upload_file is not None:
      sl.sidebar.success('Upload successfully')
      time.sleep(0.5)
      sl.sidebar.image(upload_file)

   # button
      # if sl.sidebar.button('Next'):
      # if sl.button('Next'):
      if len(image_catalog_list) == 0:
         sl.sidebar.error('You may change a date or resort')
      else:
         upload_image = Image.open(upload_file)
         return upload_image, image_catalog_list
   
   return None, None


# AI Section

def id_to_PIL(image_catalog_list):

   PIL_list = []

   for image_index in image_catalog_list:
      image_path = f'image_catalog/image_{image_index}.jpg'
      image = Image.open(image_path)
      PIL_list.append(image)

   return PIL_list


# @sl.cache_resource
def get_sim(list, single):

   sim_list = []

   with sl.spinner('Ai searching'):
      for l in list:
         sim = CLIP(l, single)
         sim_list.append(sim)
   
   sl.success('Got it')
   
   return sim_list


# Show Section
def show_section(image_catalog_list, sim_list):

   PIL_list = id_to_PIL(image_catalog_list)
   # PIL_list = small_PIL(PIL_list)

   if len(PIL_list) != 0:

      column_quantity = 2

      col1, col2 = sl.columns(column_quantity)
      column = 1
      number = 0

      for PIL in PIL_list:

         if column == 1:
            with col1:
               sl.image(PIL)
               image_number = image_catalog_list[number]
               sim = round(sim_list[number], 3)
               sl.markdown(f'> Photo {image_number} ({sim})')

         elif column == 2:
            with col2:
               sl.image(PIL)
               image_number = image_catalog_list[number]
               sim = round(sim_list[number], 3)
               sl.markdown(f'> Photo {image_number} ({sim})')

         number += 1

         column += 1
         if column == (column_quantity + 1):
            column = 1


def list_str_to_int(before):

   after = []

   for single in before:
      after.append(int(single))
   
   return after


def download_section(image_catalog_list):
   # options = sl.multiselect('What are your favorite colors', 
   #    options= ['Green', 'Yellow', 'Red', 'Blue'],
   #    ['Yellow', 'Red'])
   # st.write('You selected:', options)

   # download_list = sl.text_input('Wanna download')
   # sl.success(download_list)

   # PIL_list = id_to_PIL(image_catalog_list)

   with sl.form('download'):

      download_str = sl.text_input('Which ones do you like?')
      download_list = download_str.split(',')
      download_list = list_str_to_int(download_list)
      sl.success(download_list)
      download_PIL_list = id_to_PIL(image_catalog_list)

      if sl.form_submit_button('Download'):

         for number in download_list:
            with sl.spinner(f'Photo {number} is being downloaded'):
               download_PIL_list[number].save(f'download_image/save_photo_{number}.png')



def ai_search_page():

   full_list = open_excel()
   upload_image, image_catalog_list = sidebar_section(full_list)
   if upload_image != None:
      sl.success(image_catalog_list)
      sl.image(upload_image)
      image_catalog_list = [0, 1, 2, 3]
      sl.success(image_catalog_list)
      PIL_list = id_to_PIL(image_catalog_list)
      # i = 2
      # sl.image(image_catalog_list[i])
      # get_sim(image_catalog_list[i], upload_image)
      sim_list = get_sim(PIL_list, upload_image)
      sl.success(sim_list)
      show_section(image_catalog_list, sim_list)
      download_section(image_catalog_list)

   
if __name__ == '__main__':

   ai_search_page()