import pysftp
import os

# SFTP Server Details
sftp_host = "192.168.1.251"
sftp_username = "mainpy"
sftp_password = "1234"

# Corrected Local and Remote Folder Paths
local_folder = "C:/test_folder"  # Ensure this path is correct
remote_folder = "/home/mainpy/Documents/test_folder"  # Ensure this path does NOT contain '\'

# SFTP options
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  # Disable host key checking (not recommended for production)

def upload_directory(sftp, local_dir, remote_dir):
    """Uploads a local directory to the remote SFTP server."""
    for root, dirs, files in os.walk(local_dir):
        # Compute relative path
        rel_path = os.path.relpath(root, local_dir)
        remote_path = os.path.join(remote_dir, rel_path).replace("\\", "/")

        # Create directories on the remote server
        if not sftp.exists(remote_path):
            sftp.makedirs(remote_path)

        # Upload files
        for file in files:
            local_file = os.path.join(root, file)
            remote_file = os.path.join(remote_path, file).replace("\\", "/")
            sftp.put(local_file, remote_file)
            print(f"Uploaded {local_file} → {remote_file}")

try:
    # Establish SFTP connection
    with pysftp.Connection(sftp_host, username=sftp_username, password=sftp_password, cnopts=cnopts) as sftp:
        print("Connected to SFTP server.")

        # Ensure remote folder does not contain incorrect characters
        if "\\" in remote_folder or "." in remote_folder:
            raise ValueError("Invalid remote folder path. Use forward slashes ('/') instead.")

        # Upload the directory correctly
        upload_directory(sftp, local_folder, remote_folder)
        print(f"Folder '{local_folder}' uploaded successfully to '{remote_folder}'.")

except Exception as e:
    print(f"Error: {e}")
