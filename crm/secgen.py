from django.core.management.utils import get_random_secret_key

"""
#include this code for quick development secret_key gen
if DEBUG:  
    try:
        from .secret_keys import SECRET_KEY
    except ModuleNotFoundError:
        SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
        generate_secret_key(os.path.join(SETTINGS_DIR,"secret_keys.py"))
        from .secret_keys import SECRET_KEY

"""

def generate_secret_key(path):
    secret_file= open(path,"w")
    secret="SECRET_KEY="+"\""+get_random_secret_key()+"\"" + "\n"
    secret_file.write(secret)
    secret_file.close()