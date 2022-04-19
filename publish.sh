rm lambda_function.zip 
cd lambda 
zip -X -r ../lambda_function.zip  *.py
cd .. 
aws lambda update-function-code --function-name pyFristExperiment --zip-file fileb://lambda_function.zip
