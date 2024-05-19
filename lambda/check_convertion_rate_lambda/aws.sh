

aws sns create-topic --name sgd-myr-rate-update-topic

awslocal lambda create-function \
    --function-name check-currency-convertion-rate-function \
    --runtime python3.12 \
    --zip-file fileb://currency_tracking_app_packages.zip \
    --handler index.handler \
    --role arn:aws:iam::000000000000:role/lambda-role