# Refactored lambdaFunction

## What I did

In order to leave the main file more readable and efficient, I refactored it dividing the responsibilities into 3 files:

* `static.py`: here is any type of variable that won't change during the code execution, like URLs, long/repeating parameters, etc.

* `headers_and_params.py`: as the name implies, all headers, parameters and others that will be passed to requests.

* `helper.py`: all the auxiliary functions go here. This way it's much simplier to add unitary tests to test each part of the code.


In the main file, I used the Panda's `apply` function to, literally, apply a python lambda function to the DF column.

I also added a `try/except` in each vessel function. This way it's easier to implement some kind of validation if one of these functions doesn't run. I didn't fully implement this validation because, in my point of view, it's part of the business rules how to handle with it. At this time, if the request or validation fails, the function returns None and doesn't enter in the last DF concatenation.

I removed a lot of unused import packages which make slow down the code.

## How I tried to run the code

1. I created a RDS (MySQL) in the **AWS**, and passed the path to the `connect_to_database` function.

2. With the `serverless` framework, I created a Python template and deployed the code.

3. In the **AWS**, I added the necessary layers (I had some issues here and couldn't add the layers directly in the `serverless.yml` file).

4. I don't know if the layers didn't intall correctly, but the code into AWS didn't run properly. To validate, I ran each function (except those that depends of the PROXY or CAPTCHA) separately, in a python file, and could to validate them.

