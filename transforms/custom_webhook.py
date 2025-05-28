from infrahub_sdk.transforms import InfrahubTransform


class CustomWebhook(InfrahubTransform):
    query = "webhook_artifact"

    async def transform(self, data):
        # Test comment
        print(data)
        return {"datas": data}
