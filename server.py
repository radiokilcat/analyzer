from app import app_run, app
import os

# if not os.path.exists("databases"):
#     os.mkdir("databases")
#
# if not os.path.exists("files"):
#     os.mkdir("files")

if __name__ == '__main__':
    app_run(host='0.0.0.0',
            port='5000',
           )
