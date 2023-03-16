from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import red, black, blue, slategrey, orangered
import argparse
import pandas as pd
import configparser
import webbrowser

#The dimensions of A4 paper size in points are 595.27 x 841.89 points. These #dimensions correspond to a width of approximately 8.27 inches (595.27/72) and a #height of approximately 11.69 inches (841.89/72).
# calcs horizontal is the same as libre
# vert goes from bottom of page for some reason so it is
# height of page 595.27 - from top and height in libre
# want to do half a page for the pic so (595.27/2)/ 9 = 33.070 X 16 =  529.13

parser = argparse.ArgumentParser(description='Process selected rows')
parser.add_argument('rows', nargs='+', help='Selected rows')

args = parser.parse_args()
selected_rows = args.rows

print(selected_rows)

file_path = selected_rows[0]

# Get the index of the first occurrence of "shot"
start_index = file_path.index("shot")

# Get the substring starting from "shot" and ending at the next occurrence of "/"
substring = file_path[start_index:file_path.index("/", start_index)]

# Extract the shot number from the substring
shot_number = substring.split("_")[0]

print(shot_number)  # Output: shot11

actual_shot_number = shot_number.replace('shot', '')
print(actual_shot_number) # prints '11'


config = configparser.ConfigParser()
config.read('settings.ini')

shot_list_file = config.get('FileLocations', 'ShotListFile')

df = pd.read_csv(shot_list_file, header=0)

print(df)

# Convert 'Shot Number' column to string
df['Shot Number'] = df['Shot Number'].astype(str)

# Convert values to string

df_filtered = df[df['Shot Number'] == actual_shot_number]




# Create a new PDF document with A4 landscape orientation
pdf = canvas.Canvas(shot_number + ".pdf", pagesize=landscape(A4))

page_height = 595.27
outerborder = 40
myborder = 20

# Set the dimensions and position of the image
image_width = 529.13
image_height = page_height/2
center_x = 156.38 
center_y = image_height - myborder 

fs =14

# Define a ParagraphStyle with bold font
bold_style = ParagraphStyle(name='Bold', fontName='Helvetica-Bold', fontSize=fs, alignment=TA_CENTER, wordWrap=1.5)

norm_style = ParagraphStyle(name='norm', fontName='Helvetica', fontSize=fs)

# Set the font to bold using the ParagraphStyle
pdf.setFont(bold_style.fontName, bold_style.fontSize, bold_style.wordWrap)

word_spacing = 1.5

# Set the position to start putting in text
x, y = myborder, page_height - outerborder

# how much width do I have on the left
available_width = center_x - (x)

#how much height do I have on the left
available_height = image_height



#print(available_width)

def draw_text_with_word_wrap(pdf, text, fontsize, available_width, available_height, x, y, center_x):
    words = text.split()
    fs = fontsize
    myborder = x
    fully_printed = True
    
    for word in words:
        print(word)
        word_width = pdf.stringWidth(word + '  ', "Helvetica", fs)
        word_height = fs
        print(word_width)
        print(available_width)
        if word_width > available_width:
            x = myborder
            y -= word_height
            available_height -= word_height
            pdf.drawString(x, y, word + '  ')
            available_width = (center_x - (x) - word_width) 
            x += word_width
        elif word_height > available_height:
            if fully_printed:
                text = ' '.join(words[words.index(word):])
            else:
                text += ' ' + word
            fully_printed = False
            break
        else:
            pdf.drawString(x, y, word + '  ')
            available_width -= word_width
            x += word_width
    return x, y, fully_printed, text

def draw_text_for_description(pdf, text, fontsize, available_width, available_height, x, y, center_x):
    words = text.split()
    fs = fontsize
    myborder = x
    fully_printed = True
    
    for word in words:
        print(word)
        word_width = pdf.stringWidth(word + '  ', "Helvetica", fs)
        word_height = fs
        print(word_width)
        print(available_width)
        if word_width > available_width:
            x = myborder
            y -= word_height
            available_height -= word_height
            pdf.drawString(x, y, word + '  ')
            available_width = (x - word_width) 
            x += word_width
        elif word_height > available_height:
            if fully_printed:
                text = ' '.join(words[words.index(word):])
            else:
                text += ' ' + word
            fully_printed = False
            break
        else:
            pdf.drawString(x, y, word + '  ')
            available_width -= word_width
            x += word_width
    return x, y, fully_printed, text

def resetxy (x,y):
    x= myborder
    print(fs)
    y = y - (fs*2)
    return x, y

#SCENE measurements 

scenetext = 'SCENE NUMBER: '


x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, scenetext, fs, available_width, available_height, x, y, center_x)

#fs = 10


pdf.setFillColor(orangered)


scenetext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['Scene Number']].iloc[0,0])



x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, scenetext, fs, available_width, available_height, x, y, center_x)

scenetext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['Scene Name']].iloc[0,0])

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, scenetext, fs, available_width, available_height, x, y, center_x)

#Shot Measurements

#fs = 12

pdf.setFillColor(black)

shottext = 'SHOT NUMBER:'

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, shottext, fs, available_width, available_height, x, y, center_x)



#fs = 10

pdf.setFillColor(orangered)

shottext =  actual_shot_number

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, shottext, fs, available_width, available_height, x, y, center_x)



#Shot Size Measurements

#fs = 12

pdf.setFillColor(black)

shotsizetext = 'SHOT SIZE:'

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, shotsizetext, fs, available_width, available_height, x, y, center_x)

#fs = 10

pdf.setFillColor(orangered)
shotsizetext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['Shot Size']].iloc[0,0])

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, shotsizetext, fs, available_width, available_height, x, y, center_x)

#Lens Size Measurements

#fs = 12

pdf.setFillColor(black)
lenstext = 'LENS SIZE:'

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, lenstext, fs, available_width, available_height, x, y, center_x)

#fs = 10 

pdf.setFillColor(orangered)
lenstext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['lens']].iloc[0,0])

x,y = resetxy(x,y)

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, lenstext, fs, available_width, available_height, x, y, center_x)

#Angle Measurements

#fs = 12
pdf.setFillColor(black)
angletext = 'ANGLE ORIGIN:'

#685.51
newx = 685.51 + myborder

x,y = resetxy(x,y)
x = newx
y = page_height - outerborder

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, angletext, fs, available_width, available_height, x, y, center_x)

#fs = 10
pdf.setFillColor(orangered)
angletext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['AngleOrigin']].iloc[0,0])

x,y = resetxy(x,y)

x = newx

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, angletext, fs, available_width, available_height, x, y, center_x)


#Movement Measurements

#fs = 12
pdf.setFillColor(black)
movementtext = 'MOVEMENT:' 

x,y = resetxy(x,y)
x = newx

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, movementtext , fs, available_width, available_height, x, y, center_x)

#fs = 10

pdf.setFillColor(orangered)
movementtext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['MoveMent']].iloc[0,0])

x,y = resetxy(x,y)
x = newx

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, movementtext , fs, available_width, available_height, x, y, center_x)

#Sound Measurements

#fs = 12

pdf.setFillColor(black)
soundtext = 'SOUND:'

x,y = resetxy(x,y)
x = newx

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, soundtext, fs, available_width, available_height, x, y, center_x)

#fs = 10

pdf.setFillColor(orangered)
soundtext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['Sound']].iloc[0,0])

x,y = resetxy(x,y)
x = newx

x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, soundtext, fs, available_width, available_height, x, y, center_x)

#Description Measurements

#fs = 12
pdf.setFillColor(black)
descriptiontext = 'DESCRIPTION' 

x,y = resetxy(x,y)
x = 156.38
y = 257 #image_height
print(y)
available_height = image_height
available_width = image_width


x, y, fully_printed_text, remainingtext = draw_text_with_word_wrap(pdf, descriptiontext , fs, available_width, available_height, x, y, center_x)

#fs = 10
pdf.setFillColor(slategrey)
descriptiontext = str(df_filtered.loc[df_filtered['Shot Number'] == actual_shot_number, ['Description']].iloc[0,0])

#x,y = resetxy(x,y)
x = 156.38
y = y - (fs*2)
print(y)
available_height = image_height
available_width = image_width

x, y, fully_printed_text, remainingtext = draw_text_for_description(pdf, descriptiontext , fs, available_width, available_height, x, y, center_x)

# Draw the image at the center of the page
pdf.drawImage(file_path, center_x, center_y, width=image_width, height=image_height)

# Save the PDF document
pdf.save()

file_path = shot_number + ".pdf"
webbrowser.open_new_tab(file_path)









