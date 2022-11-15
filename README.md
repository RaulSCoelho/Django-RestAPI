# First step
create a folder for your project and a virtual environment inside it: **virtualenv venv**

![venv](https://user-images.githubusercontent.com/84609153/189959256-176532f4-4d44-4353-a8d1-413c4bd62cd3.png)

# Second step
activate your venv: **venv\Scripts\activate**

![activate-venv](https://user-images.githubusercontent.com/84609153/189959494-87763a09-c879-455a-a679-bbb5cf3a1edc.png)

# Third step
"**Save Workspace As**"

![Workspace](https://user-images.githubusercontent.com/84609153/189959672-fcd692b4-0de8-440c-8b74-44c8af201f7c.png)

# Fourth step
create a '**requirements.txt**' file with the following packages:
- **django>=4.0.0,<4.1.0**
- **djangorestframework**
- **pyyaml**
- **requests**
- **django-cors-headers**

![requirements](https://user-images.githubusercontent.com/84609153/189959986-4967ce89-0cd1-4451-872c-1a156dcb2290.png)

# Fifth step
install the packages by running: **pip install -r requirements.txt**

![install-requirements](https://user-images.githubusercontent.com/84609153/189960659-a3105e8d-0d5c-4c30-98de-85772951dff3.png)

# Sixth step
update your requirements.txt file: **pip freeze > requirements.txt**

![pip-freeze](https://user-images.githubusercontent.com/84609153/189960891-f45811cd-858a-492a-8c90-2087667ac98b.png)

# Seventh step
create a backend folder and inside it, run the following command: **django-admin startproject {your project} .**

![startproject](https://user-images.githubusercontent.com/84609153/189961716-aff3f88c-323a-481b-8785-2f01b6814061.png)

# Eighth step
still inside the backend folder, create your first app: **python manage.py startapp {your app}**

![startapp](https://user-images.githubusercontent.com/84609153/189961880-bb1c1aa6-7ef5-4ad7-9b71-9d5aab352f26.png)

# Ninth step
Inside your project folder, on settings.py, add your app name on "**INSTALLED_APPS**"

![INSTALLED_APPS](https://user-images.githubusercontent.com/84609153/189962100-1cc5655b-ba28-4994-9a16-17fbfd2446ba.png)
