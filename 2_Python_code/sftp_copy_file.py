import pysftp

# SFTP server details
sftp_host = "your.sftp.server.com"
sftp_port = 22  # Default SFTP port
sftp_username = "your_username"
sftp_password = "your_password"

# File details
remote_file_path = "/remote/path/to/file.txt"
local_file_path = "local_copy.txt"

# Set SFTP options (if needed)
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  # Disable host key checking (not recommended for production)

try:
    # Establish SFTP connection
    with pysftp.Connection(sftp_host, username=sftp_username, password=sftp_password, cnopts=cnopts) as sftp:
        print("Connected to SFTP server.")

        # Copy file from remote to local
        sftp.get(remote_file_path, local_file_path)
        print(f"File copied successfully to {local_file_path}")

except Exception as e:
    print(f"Error: {e}")
