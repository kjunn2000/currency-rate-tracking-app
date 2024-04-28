from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
)
from constructs import Construct

class CurrencyTrackingAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "CurrencyConvertionTrackingQueue",
            visibility_timeout=Duration.seconds(300),
        )
        
        lambda_function = _lambda.Function(self, "CheckCurrencyConvertionRateLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda/check_convertion_rate_lambda"),
        )

        lambda_event_source = lambda_event_sources.SqsEventSource(queue, batch_size=1)
        lambda_function.add_event_source(lambda_event_source)
        