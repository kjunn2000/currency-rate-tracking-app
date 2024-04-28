import aws_cdk as core
import aws_cdk.assertions as assertions

from currency_tracking_app.currency_tracking_app_stack import CurrencyTrackingAppStack


def test_sqs_queue_created():
    app = core.App()
    stack = CurrencyTrackingAppStack(app, "currency-tracking-app")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SQS::Queue", 1)
    template.has_resource_properties("AWS::SQS::Queue", {"VisibilityTimeout": 300})


def test_lambda_created():

    app = core.App()
    stack = CurrencyTrackingAppStack(app, "currency-tracking-app")
    template = assertions.Template.from_stack(stack)

    # Assert that the Lambda function is created
    template.resource_count_is("AWS::Lambda::Function", 1)
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Runtime": "python3.12",
            "Handler": "lambda_function.handler",
        },
    )


def test_event_source_mapping_created():

    app = core.App()
    stack = CurrencyTrackingAppStack(app, "currency-tracking-app")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::EventSourceMapping", 1)
    template.has_resource_properties(
        "AWS::Lambda::EventSourceMapping",
        {
            "BatchSize": 1,
            "EventSourceArn": {
                "Fn::GetAtt": ["CurrencyConvertionTrackingQueue15F4561C", "Arn"]
            },
            "FunctionName": {"Ref": "CheckCurrencyConvertionRateLambda62A4DEB9"},
        },
    )

    template.resource_count_is("AWS::Lambda::EventSourceMapping", 1)
