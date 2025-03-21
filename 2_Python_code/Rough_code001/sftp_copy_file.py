import pysftp

# SFTP server details
sftp_host = "192.168.1.251"
sftp_port = 22  # Default SFTP port
sftp_username = "mainpy"
sftp_password = "1234"

# File details
remote_file_path = "/home/mainpy/Documents/test_file.txt"
local_file_path = "C:/test_folder/test_file.txt"

# Set SFTP options (if needed)
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  # Disable host key checking (not recommended for production)


    # Establish SFTP connection
with pysftp.Connection(sftp_host, username=sftp_username, password=sftp_password, cnopts=cnopts) as sftp:
    print("Connected to SFTP server.")

    # Copy file from remote to local
    sftp.put(localpath=local_file_path,remotepath=remote_file_path,confirm=True)
    # print(f"File copied successfully to {local_file_path}")

