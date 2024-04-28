import aws_cdk as core
import aws_cdk.assertions as assertions

from currency_tracking_app.currency_tracking_app_stack import CurrencyTrackingAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in currency_tracking_app/currency_tracking_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CurrencyTrackingAppStack(app, "currency-tracking-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
