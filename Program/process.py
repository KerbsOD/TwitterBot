from Program import dolarAPI
from Program import meme_generator

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



