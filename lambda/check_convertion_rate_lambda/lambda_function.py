import os
import decimal
import logging
import boto3
import yfinance as yf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sns_client = boto3.client("sns")


def lambda_handler(event, context):
    try:
        logger.info("Event received: %s", event)

        currency_pair = "SGDMYR=X"

        live_data = yf.download(currency_pair, period="1d", interval="1m")

        if live_data.empty:
            logger.error("No data received for %s", currency_pair)
            return

        logger.info("Live data: %s", live_data.tail())

        sgd_myr = live_data["Close"].iloc[-1]

        logger.info("SGD to MYR rate: %.4f", sgd_myr)

        threshold_rate = decimal.Decimal("3.40")
        if decimal.Decimal(sgd_myr) > threshold_rate:
            logger.info("SGD to MYR rate exceeds the threshold: %.4f", threshold_rate)

            response = sns_client.publish(
                TopicArn=os.getenv("SGD_MYR_RATE_UPDATE_SNS_TOPIC_ARN"),
                Message=f"{currency_pair} conversion rate is {sgd_myr:.4f}.",
                Subject="Action Now",
            )
            logger.info("SNS response: %s", response)
        else:
            logger.info("SGD to MYR rate does not exceed the threshold.")

    except Exception as e:
        logger.error("Error processing the event: %s", e, exc_info=True)