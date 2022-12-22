from app.config import CONFIG
from app.factory.redis import redis_client
from app.fdk.exntension_handlers import ExtensionHandlers

from fdk_extension import setup_fdk
from fdk_extension.extension import FdkExtensionClient
from fdk_extension.storage.redis_storage import RedisStorage

def get_extension_client() -> FdkExtensionClient:
    print(f'dealing with extension client @ {CONFIG.EXTENSION_API_KEY}')

    # extension handlers for callbacks
    extension_handlers = ExtensionHandlers()

    # setting up the fdk client
    fdk_extension_client = setup_fdk({
        "api_key": CONFIG.EXTENSION_API_KEY,
        "api_secret": CONFIG.EXTENSION_API_SECRET,
        "base_url": CONFIG.EXTENSION_BASE_URL,
        "callbacks": {
            "auth": extension_handlers.auth,
            "uninstall": extension_handlers.uninstall
        },
        "storage": RedisStorage(redis_client, prefix_key="example-extension"), # Add you prefix
        "access_mode": "offline", # Configure Access Mode: 'online' or 'offline'
        "cluster": CONFIG.EXTENSION_CLUSTER_URL # This is optional by default it will point to prod
    })

    print("Extension Initiated..!")

    return fdk_extension_client
