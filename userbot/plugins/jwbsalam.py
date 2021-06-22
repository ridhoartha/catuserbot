import random

from . import ALIVE_NAME, catmemes

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@bot.on(admin_cmd(pattern="l$"))
@bot.on(sudo_cmd(pattern="l$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Waalaikumsalam**"
    await event.edit(mentions)


CMD_HELP.update(
    {
        "memestext": "**Plugin : **`SALAM`\
        \n\n  •  **Syntax :** `.congo`\
        \n  •  **Function : **Congratulate the people.\
        \n\n  •  **Syntax :** `.shg`\
        \n  •  **Function : **Shrug at it !!\
        \n\n  •  **Syntax :** `.runs`\
        \n  •  **Function : **Run, run, RUNNN!\
        \n\n  •  **Syntax :** `.noob`\
        \n  •  **Function : **Whadya want to know? Are you a NOOB?\
        \n\n  •  **Syntax :** `.insult`\
        \n  •  **Function : **insult someone\
        \n\n  •  **Syntax :** `.hey`\
        \n  •  **Function : **start a conversation with people\
        \n\n  •  **Syntax :** `.pro`\
        \n  •  **Function : **If you think you're pro, try this.\
        \n\n  •  **Syntax :** `.react` <type>\
        \n  •  **Function : **Make your userbot react. types are <happy ,think ,wave ,wtf ,love ,confused,dead, sad,dog>\
        \n\n  •  **Syntax :** `.10iq`\
        \n  •  **Function : **You retard !!\
        \n\n  •  **Syntax :** `.fp`\
        \n  •  **Function : **send you face pam emoji!\
        \n\n  •  **Syntax :** `.bt`\
        \n  •  **Function : **Believe me, you will find this useful.\
        \n\n  •  **Syntax :** `.session`\
        \n  •  **Function : **telethon session error code(fun)\
        "
    }
)