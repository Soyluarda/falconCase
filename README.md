# FalconCase

- ### Installation
- create a directory and clone projects in it.
    - create a virtual environment and activate it.
        ```
        - virtualenv -p python3 venv
        - source venv/bin/activate
        ```
    - and after all the changes in models.py files you should run the following commands:
       ```
        pip3 install -r requirements.txt
        Create your secrets file using settings/secrets.py.template file and write your credentials into it.(Add SECRET_KEY first,* if you are using prod.py file configure your postgres settings)
        python3 manage.py makemigrations riot  & python3 manage.py makemigrations user
        python3 manage.py migrate
        python3 manage.py runserver
       ```
- Install redis:
    ``` 
    -sudo apt-get install redis-server (for ubuntu)
    -brew install redis (for macOs)
    ```
- To create an admin user:
    ``` 
    python3 manage.py createsuperuser 
    ```
    
- To run in the localhost:
    ```
    python3 manage.py runserver
    ```
- ## API
    - To list all the characters of user:
        - `user/list/`

    - To get the detail of a plant:
        - `user/char/add/`
            - send parameters as api_key
            - send parameters as region
     
    - To see all others api, documentation:
        - `docs/`
       
- ## Testing on server
  ### All API open for testing.
    - to see documentation 
        -`www.ardaben.com/docs/`
    - send post request to see ranked-data;
        -`https://www.ardaben.com/api/ranked-data/`
            send parameters as: example,{region:tr1,api_key:your_api_key}
    - send post request to see lor-ranked-data;
        -`https://www.ardaben.com/api/lor-ranked-data/`
            send parameters as: example,{region:europe,api_key:your_api_key}    
    - send post request to see shared-data;
        -`https://www.ardaben.com/api/shard-data/`
            send parameters as: example,{region:europe,api_key:your_api_key} 

    - Serving files as download section
        -`https://www.ardaben.com/download/test.json`
        -`https://www.ardaben.com/download/arda_cv.pages`
         
    
    
