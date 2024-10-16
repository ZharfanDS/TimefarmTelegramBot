import os
import asyncio
from telethon import TelegramClient

async def create_session(api_id, api_hash, session_name='default'):
    """Membuat file session .session menggunakan API ID dan API HASH"""
    # Buat instance TelegramClient
    client = TelegramClient(f'sessions/{session_name}', api_id, api_hash)
    
    # Hubungkan dan lakukan autentikasi
    async with client:
        # Jika belum pernah login, ini akan meminta nomor dan kode Telegram
        await client.start()
        print(f"Session '{session_name}.session' berhasil dibuat!")

async def main():
    # API ID dan API HASH didapatkan dari Telegram Developer
    api_id = int(input("Masukkan API ID: "))  # Misal: 123456
    api_hash = input("Masukkan API HASH: ")  # Misal: 'abc123def456ghi789'

    # Path untuk folder sesi
    session_folder = 'sessions/'
    
    # Cek apakah folder sesi sudah ada
    if not os.path.exists(session_folder):
        os.makedirs(session_folder)
    
    # Cek apakah file .session sudah ada, jika tidak, buat file session baru
    sessions = [file for file in os.listdir(session_folder) if file.endswith('.session')]
    if not sessions:
        print("Tidak ada file .session ditemukan. Membuat file session baru...")
        await create_session(api_id, api_hash)
    else:
        print(f"File .session sudah ditemukan: {sessions}")

if __name__ == '__main__':
    asyncio.run(main())
