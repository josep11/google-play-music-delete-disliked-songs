#Google Play Music Delete Disliked Songs

###This project deletes all your disliked songs from your Google Music account, so that you no longer have to do that tedious process

Tested on python version: 3.5.1

####Install
* python 3.5.1
* pip install gmusicapi

####Configuration
* Edit email, password and/or device MAC Address
* Execute
```
copy config_example.ini config.ini
```
And add your credentials there
* [Optional] clone https://josep_a11@bitbucket.org/josep_a11/sendgrid (.git) and put the parent folder on a environment variable called SENDGRID_DIR. Also, set the SENDGRID_API_KEY.


####Usage
> python main.py


## NOT WORKING AS OF 04/09/2017 because Google Play Music changed API
