rm -Rf function.zip
cp lib.zip function.zip
zip -g function.zip lambda_function.py
aws lambda update-function-code --function-name berryface-flask --publish  --zip-file fileb://function.zip