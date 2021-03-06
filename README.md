# 3-Legged-OAuth-WorkFlow
If you are trying to create a Twitter bot, and your Twitter developer account is different from the account you are trying to run your bot on, this Python code should help you.

I recommend that you run this code in Visual Studio Code and that you also set up a virtual environment. In the README.md file, I have instructions on how to do this in your terminal. You also need to have a Twitter developer account before running this code. You will need to put your app_secret and app_key in the YAML file in this repo before runnning this code.

This code is part of a project I have coined the Herzl Bot Project. 

## Step 1: Create a Virtual Environment
Creating a Virtual Environment in Visual Studio Code
Lets say that the name of the virtual environment that you want to create is:
		
		herzlbot-env

1. Create the virtual environment by opening the folder where you want the virtual environment in the terminal. 
   Execute the following code:
		
		python3 -m venv herzlbot-env

2. Now it is time to install packages.
   Update the terminal with this code to make sure you are working in the context of the virtual environment:
		
		source herzlbot-env/bin/activate

3. Make sure that the interpreter is updated to the virtual environment.
   
4. Make sure to update pip as well, using the command:
		
		pip install --upgrade pip


## Step 2: Install the Packages in the Virtual Environment
Run this command in the terminal in the virtual environment:
		
		pip install -r requirements.txt


## Step 3: Run the Authentication File
The authentication file only needs to be run once.

Follow the command prompt. When prompted, you will authenticate your application and confirm the permissions on your Twitter account. Make sure you are signed into the Twitter account that you want your bot to be before running this code. After you authorize your app in the browser, you are going to then copy and paste the URL in your browser into your terminal.

This file when run will store all the needed tokens in the confg.yaml file.
Variables can then be pulled from this file by calling these functions:

		from authentication import process_yaml, app_key, app_secret, oauth_token, oauth_token_secret

			data =  process_yaml()
			CONSUMER_KEY = app_key(data)
			CONSUMER_SECRET = app_secret(data) 
			ACCESS_KEY = oauth_token(data)  
			ACCESS_SECRET = oauth_token_secret(data)

We can now use the HerzlBot Twitter application.
Note that the test_tweet.py file is for testing if the API is connected properly. If you run this file, your app should Tweet out a "Shalom."
This file uses the tweepy module to Tweet out a sample Tweet.
