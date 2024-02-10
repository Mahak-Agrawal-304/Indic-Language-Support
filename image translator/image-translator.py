import pandas as pd
import easyocr
import cv2
root = Tk()
root.withdraw()  

# Prompt the user to select an image file using a file dialog
file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
image_file_path = file_path
img1=image_file_path
filename=os.path.basename(img1)
upld(filename)

img = cv2.imread(img1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#noise = cv2.medianBlur(gray,3)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
#thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

reader = easyocr.Reader(['en'])
result = reader.readtext(img,paragraph=False)
text_lines = [entry[1] for entry in result[0::]]  # Exclude the last line
text = ' '.join(text_lines)
df = pd.DataFrame({"":text_lines})

sou_txt.delete(1.0,tk.END)
sou_txt.insert(tk.END,df.to_string(index=False,header=False))
comb_sou_option=comb_sou.get()
comb_des_option=comb_des.get()
txt = sou_txt.get(1.0,tk.END)
try:
    trans = Translator()
    trans1 = trans.translate(text=txt,src=comb_sou_option,dest=comb_des_option)
    
    des_txt.delete(1.0, tk.END)
    des_txt.insert(tk.END,trans1.text)
    return None
except Exception as e:
    messagebox.showerror("Error","Please enter text to be translated")
    return None
