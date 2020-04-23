import os
import shutil
import uuid
import datetime
from json.encoder import JSONEncoder

from commons.constants import PAGE_NUMBER, PAGE_SIZE, DEFAULT_PAGE_NUMBER, DEFAULT_PAGE_SIZE, EXACTLY_ONCE, \
    ATLEAST_ONCE, ALMOST_ONCE
from commons.exceptions import ClientError
from commons.schema import ResponseSchema, ResponseSchemaModel


def extract_query_params(args, query_param_keys):
    query_params = {k: v for k, v in args.items() if k in query_param_keys}
    page_number = {k: v for k, v in args.items() if k == PAGE_NUMBER}
    page_size = {k: v for k, v in args.items() if k == PAGE_SIZE}

    if not page_number:
        page_number = DEFAULT_PAGE_NUMBER

    if not page_size:
        page_size = DEFAULT_PAGE_SIZE

    return query_params, (page_number, page_size)


def create_uuid():
    return str(uuid.uuid4())


def apply_filter(query, tables, params, op="eq"):
    for table in tables:
        for attr, value in params.items():
            if hasattr(table, attr):
                if op == "like":
                    query = query.filter(str(getattr(table, attr)).like(str(value) + "%"))
                else:
                    query = query.filter(getattr(table, attr) == value)

    return query


def get_error(status_code, message):
    raise ClientError(message, status_code)


def create_folders(path):
    if not os.path.exists(path):
        os.makedirs(path)


def delete_folder(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory, ignore_errors=True)


class PayloadEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
