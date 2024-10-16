import os
import json
import asyncio
from telethon import TelegramClient

async def create_session(api_id, api_hash, session_name):
    """Membuat file session .session menggunakan API ID dan API HASH"""
    # Buat instance TelegramClient
    client = TelegramClient(f'sessions/{session_name}', api_id, api_hash)
    
    # Hubungkan dan lakukan autentikasi
    async with client:
        # Jika belum pernah login, ini akan meminta nomor dan kode Telegram
        await client.start()
        print(f"Session '{session_name}.session' berhasil dibuat!")

async def main():
    # Membaca API ID dan API HASH dari config.json
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
        api_id = config_data.get('api_id')
        api_hash = config_data.get('api_hash')

    # Menanyakan session_name kepada user
    session_name = input("Masukkan nama session: ")  # Tanya session_name ke user

    # Path untuk folder sesi
    session_folder = 'sessions/'
    
    # Cek apakah folder sesi sudah ada
    if not os.path.exists(session_folder):
        os.makedirs(session_folder)
    
    # Cek apakah file .session sudah ada, jika tidak, buat file session baru
    sessions = [file for file in os.listdir(session_folder) if file.endswith('.session')]
    if not sessions:
        print("Tidak ada file .session ditemukan. Membuat file session baru...")
        await create_session(api_id, api_hash, session_name)
    else:
        print(f"File .session sudah ditemukan: {sessions}")

if __name__ == '__main__':
    asyncio.run(main())
