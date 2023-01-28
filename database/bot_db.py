from config import bot
import random
import sqlite3
def sqlcreate():
    global db, cursor
    db = sqlite3.connect(
        "bot.sqllite3"
    )
    cursor = db.cursor()
    if db:
        print ("База данных подключено")
    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors"
        "(id INTEGER PRIMARY KEY , name text,"
        "nap TEXT, age INTEGER, group INTEGER)"
    )
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors "
                       "(id, name, nap, age,group ) VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()
async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    await bot.seng_message(
        message.from_user.id,
        random_user[-1],
        caption=f"{random_user[0]} {random_user[1]} {random_user[2]} "
                f"{random_user[3]}\n\n{random_user[4]}"
    )

async def sql_command_all():
        return cursor.execute("SELECT * FROM mentors").fetchall()

async def sql_command_delete(user_id):
        cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
        db.commit()

async def sql_command_all_id():
    return cursor.execute("SELECT * id FROM mentors").fetchall()
