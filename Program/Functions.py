import dolarAPI
import meme_generator

# UpdateImage
def updateImage():
    
    # Price Update
    dolarAPI.update_price()

    # Open Json 
    Data = open('./Program/Resources/Precio.json')
    Data_Load = meme_generator.json.load(Data)
    Dolar_Blue_Half = (Data_Load['blue']["value_sell"]) / 2

    # Generate Image    
    top_text = ""
    bottom_text = str(Dolar_Blue_Half) + " pesos"
    meme_generator.generate_meme('./Program/Resources/50.jpg', top_text=top_text, bottom_text=bottom_text)

# Read and save last response ID

FILE_NAME = './Program/Resources/last.txt'

def read(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


