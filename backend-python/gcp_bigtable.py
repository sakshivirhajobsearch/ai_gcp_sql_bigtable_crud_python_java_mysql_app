# gcp_bigtable.py
from google.cloud import bigtable
from config import PROJECT_ID, BIGTABLE_INSTANCE_ID, BIGTABLE_TABLE_ID

def get_bigtable_data():
    client = bigtable.Client(project=PROJECT_ID, admin=True)
    instance = client.instance(BIGTABLE_INSTANCE_ID)
    table = instance.table(BIGTABLE_TABLE_ID)

    rows = []
    partial_rows = table.read_rows()
    partial_rows.consume_all()

    for row_key, row_data in partial_rows.rows.items():
        row_dict = {"row_key": row_key.decode("utf-8")}
        for family_name, columns in row_data.cells.items():
            row_dict[family_name] = {}
            for col_name, cell_list in columns.items():
                # latest cell value
                row_dict[family_name][col_name.decode("utf-8")] = cell_list[-1].value.decode("utf-8")
        rows.append(row_dict)
    return rows
