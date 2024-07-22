'''Must add the 1PasswordCLI and setup before this will function
follow 1Password documentation
https://developer.1password.com/docs/cli/get-started/?utm_medium=organic&utm_source=oph&utm_campaign=macos
be sure to import the class
'''
import subprocess
import json

class CredentialManager:
    def __init__(self):
        pass

    def get_1password_credentials(self, item_name):
        """
        Get credentials from 1Password.
        """
        try:
            result = subprocess.run(
                ["op", "item", "get", item_name, "--format", "json"],
                capture_output=True, text=True, check=True
            )
            item = json.loads(result.stdout)
            username = next(field['value'] for field in item['fields'] if field['id'] == 'username')
            password = next(field['value'] for field in item['fields'] if field['id'] == 'password')
            return username, password
        except subprocess.CalledProcessError as e:
            print(f"Error fetching credentials from 1Password: {e}")
            return None, None
        except (KeyError, StopIteration) as e:
            print(f"Error parsing 1Password item: {e}")
            return None, None
        
# # How to call in code 
# # Fetch credentials from 1Password
# op_username, op_password = cm.get_1password_credentials("NameOfCredHere")
# if op_username and op_password:
#     print(f"1Password - Username: {op_username}, Password: {op_password}")
# else:
#     print("Failed to fetch 1Password credentials.")