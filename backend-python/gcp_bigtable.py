from google.cloud import bigtable

def get_bigtable_data():
    client = bigtable.Client(project='your-project-id', admin=True)
    instance = client.instance('your-instance-id')
    table = instance.table('your-table-name')

    partial_rows = table.read_rows()
    rows = []
    for row in partial_rows:
        row_data = {}
        for family_name, columns in row.cells.items():
            for column, cells in columns.items():
                row_data[column.decode()] = cells[0].value.decode()
        rows.append(row_data)
    return rows
