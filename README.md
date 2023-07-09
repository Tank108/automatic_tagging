# automatic_tagging

The project is about generating tags from the video ,audio , and text files.

-Prerequisites
  To run the programs in this repo, do the following:

  create a virtual environment using the command:
  python -m venv venv
  activate the virtual environment
  cd ./venv/Scripts/activate (windows users)
  source ./venv/bin/activate (mac and linux users)
  install the requirements
  pip install --upgrade pip (to upgrade pip)
  pip install -r requirements.txt
  or you may create a conda environemnt  

- Once the requirements have been installed, The programs will run successfully. 

- # Tag generation from text
- For Text Parsing Apache tika python library is being used,which is verstaile parser.
   -Obatained text from file is given to Keybert library which is used to generate the tags.

 - # Tag generation from Audio
   - First  speech to text conversion is done using huggigface pipeline using pretrained open-ai whisper tiny model.
   - Then obatained text is further processed using KeyBert library to generate tags.  

 - # Tag generation from Video
   - First Video is converted into audio using moviepy library.
   - Then audio is converted to text using speech to text using huggigface pipeline using pretrained open-ai whisper tiny model.
   - Then this converted audio to speech to further processed using KeyBert library to generate tags.  


