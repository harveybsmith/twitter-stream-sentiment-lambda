import boto

def lambda_handler(event, context):
	comprehend = boto3.client('comprehend',
			          region_name='us-east-1,
				  aws_access_key_id = AWS_KEY,
				  aws_secret_access_key=AWS_SECRET)

	output = []
	for record in event['records']:
		dict_data = base64.b64decode(record['data']).decode('utf-8').strip()
		dict_data = json.loads(dict_data)
		sentiment_all = comprehend.detect_sentiment(
			Text=dict_data['text'],
			LanguageCode=dict_data['lang'])
		dict_data['sentiment'] = sentiment_all['Sentiment']

		output_record = {
			'recordId': record['recordId'],
			'result': 'Ok',
			'data': base64.b64encode(json.dumps(dict_data).encode('utf-8'))
		}
		output.append(output_record)
	return {'records': output}