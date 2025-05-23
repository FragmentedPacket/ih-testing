from infrahub_sdk.transforms import InfrahubTransform


class CustomWebhook(InfrahubTransform):
    query = "webhook_artifact"

    async def transform(self, data):
        print(data)
        return data
