from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession

import asyncio
import shutil
import os

async def create_tdata():
    try:

        session_folder = "MySession"

        session_files = [f for f in os.listdir(session_folder) if f.endswith(".session")]


        tdata_folder = f"{os.getcwd()}/tdatas"
        os.makedirs(tdata_folder, exist_ok=True)

        for session_file in session_files:
            try:
                client = TelegramClient(os.path.join(session_folder, session_file))

                tdesk = await client.ToTDesktop(flag=UseCurrentSession)
                if tdesk:
                    tdata_name = os.path.splitext(session_file)[0]
                    tdesk.SaveTData(f'{tdata_folder}/{tdata_name}')
                    shutil.make_archive(f'{tdata_folder}/{tdata_name}', 'zip', f'{tdata_folder}/{tdata_name}')
                    print(f"TData для сессии {session_file} создан и сохранен успешно.")
                else:
                    print(f"Ошибка при получении TDesktop объекта для сессии {session_file}.")
            except Exception as e:
                print(f"An error occurred for session {session_file}: {e}")
            finally:
                await client.disconnect()

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


asyncio.run(create_tdata())
