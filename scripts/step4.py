import boto3
import json

# Cliente Kinesis
kinesis_client = boto3.client('kinesis', region_name='us-west-2')

# Obter a lista de fragmentos do stream
response = kinesis_client.describe_stream(StreamName='info-stream')
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

# Obter o iterador de fragmento
iterator_response = kinesis_client.get_shard_iterator(
    StreamName='info-stream',
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)

shard_iterator = iterator_response['ShardIterator']

found = False
found2 = False

records = []
i = 0
# Ler os registros do stream
for _ in range(1):
    records_response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=1000)

    # Exibir os registros lidos
    for record in records_response['Records']:
        print(record)
        data = json.loads(record['Data'])
        if found2:
            break
        if found:
            records.append(record['Data'])
            print(f"{data['x']},{data['y']},#00FF00,circle,\"{i}\"")
            i+=1
        if data["type"] == "<":
            if found:
                found2 = True
            found = True



