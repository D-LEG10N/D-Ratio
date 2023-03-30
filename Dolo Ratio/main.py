import zamba
from zamba.models.model_manager import predict_model
from zamba.models.config import PredictConfig
import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.filechooser import FileChooser
from kivy.properties import StringProperty


file =' '
class AnchorLayoutExample(AnchorLayout):
    from zamba.models.model_manager import predict_model
    from zamba.models.config import PredictConfig
    my_text=StringProperty('Video Selected: ')

    def on_file_select(self,instance,value):
        print(f"Selected file: {value[0]}")
        file=value[0]
        print(file)
        self.my_text="Video selected : " + file

    def video_predictor(self,video,model):
        
        self.predict_config = PredictConfig(data_dir='Videos/')

        self.predict_model(predict_config=self.predict_config)
   

class AnimalDetector(App):

   pass

        
if __name__=="__main__":
    AnimalDetector().run()
