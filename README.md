# upload_file
Server to upload files

# requirements - Libs 
python 2:
pip install requests  
pip install flask  
pip install -U Werkzeug  

python 3:  
pip3 install requests   
pip3 install flask    
pip3 install -U Werkzeug   


Download Libs from https://pypi.org


**Installation from local:**

1. Created folder:  
mkdir libs_upload  
cd libs_upload  

2. Download libs in folder:  
Flask,
Werkzeug,  
Jinja2,  
itsdangerous,  
click,  

3. Install libs:  
pip install *.whl  
or  
pip3 install *.whl    

4. Start Server    
cd upload_file   
sudo python3 server.py    
  
References:
https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
