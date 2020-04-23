from marshmallow import Schema, fields, post_load


class ResponseSchema(Schema):
    status = fields.String(data_key="status", nullable=False)
    data = fields.Field(data_key="data")
    response_to = fields.String(data_key="responseTo", nullable=False)

    @post_load
    def make_response(self, data, **kwargs):
        return ResponseSchemaModel(**data)


class ResponseSchemaModel:

    def __init__(self, status, data, response_to):
        self.status = status
        self.data = data
        self.response_to = response_to
