#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import json
import csv

def generate_csv(input_json_file, output_csv_file):
    try:
        with open(input_json_file) as f:
            data = json.load(f)

        csv_headers = ['hostname', 'device_ip', 'current_version', 'target_version', 'model', 'target_version_satisfied', 'target_image_presence', 'md5_checksum_success']

        with open(output_csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
            writer.writeheader()
            
            for hostname, records in data.items():
                for record in records:
                    writer.writerow(record)

        return True, None
    except Exception as e:
        return False, str(e)

def main():
    module = AnsibleModule(
        argument_spec=dict(
            input_json_file=dict(type='str', required=True),
            output_csv_file=dict(type='str', required=True)
        )
    )

    input_json_file = module.params['input_json_file']
    output_csv_file = module.params['output_csv_file']

    success, msg = generate_csv(input_json_file, output_csv_file)

    if success:
        module.exit_json(changed=True, msg="CSV file generated successfully.")
    else:
        module.fail_json(msg="Failed to generate CSV file: {}".format(msg))

if __name__ == '__main__':
    main()
