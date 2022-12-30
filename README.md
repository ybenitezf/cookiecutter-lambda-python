# Python boilerplate code to use with AWS Lambda

This is a cookiecutter to fast setup a Python project to use witch lambda. The idea behind is that the lambda handler will be keeping it the must simple posible while all the logic will go to the package.

I recommend to use this in conjugation with AWS CDK and this form of code bundling:

```python
self.func = lambda_.Function(
    self,
    f"{id}-lambda",

    ...

    runtime=lambda_.Runtime.PYTHON_3_9,
    handler="main.handler",
    code=lambda_.Code.from_asset(
        'lambda',
        bundling=BundlingOptions(
            image=lambda_.Runtime.PYTHON_3_9.bundling_image,
            command=[
                "bash", "-c",
                "pip install -r requirements.txt -t"
                " /asset-output && cp -au . /asset-output"
            ]
        )
    ),

    ...

)
```

Adding the package builded from the boilerplate to the `requirements.txt` in the prior code.
