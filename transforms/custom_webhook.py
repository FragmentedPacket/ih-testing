from infrahub_sdk.transforms import InfrahubTransform


class CustomWebhook(InfrahubTransform):
    query = ""

    async def transform(self, data):
        print(data)
        return {"branch_thang": data}
