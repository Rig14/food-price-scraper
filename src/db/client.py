"""Supabase client module."""

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Set up Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def get_supabase() -> Client:
    """Get Supabase client."""
    return supabase
