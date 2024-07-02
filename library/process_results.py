import json
import csv

# Load the JSON file
with open('/tmp/device_versions.json') as f:
    data = f.read().splitlines()
    data = [json.loads(line) for line in data]

# Define CSV headers
csv_headers = ['hostname', 'device_ip', 'current_version', 'target_version', 'model', 'target_version_satisfied', 'target_image_presence', 'md5_checksum_success']

# Write to CSV
with open('/tmp/device_versions.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()
    for item in data:
        writer.writerow(item)
