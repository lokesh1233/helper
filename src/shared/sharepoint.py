def parse_results(result_list):
    processed_results = []
    for result in result_list:
        processed_item = dict()
        for cell in result['Cells']:
            key = cell['Key']
            value = cell['Value']
            processed_item[key] = value
        processed_results.append(processed_item)
    return processed_results
        
         