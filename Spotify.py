import requests


def get_token() -> str:
    return requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "client_credentials"
        },
        headers={
            "Authorization": "Basic ZDMyNDBkYzllMjUwNDcwYjk4NjZlODJlMDkwZDVhN2M6NGE3MmQ4YzQwNTRkNGM4MDk5M2E5OGEyMWRiMzE5NzU="
        }
    ).json()["access_token"]


if __name__ == "__main__":
    print(get_token())