import os


class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):
        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        os.system(command)


# Example usage:
gcloud_sync = GCloudSync()
gcloud_sync.sync_folder_from_gcloud("hate00332211", "Data.zip", "Download/data.zip")
