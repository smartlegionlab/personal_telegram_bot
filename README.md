# Personal Telegram Bot

---

### Personal telegram bot for you or your company:

> Universal, asynchronous telegram bot for your company or personal use.

- Displays information about you or your company. 
- Adds a button to go to your website. 
- Forward sent messages to you.
- You can deploy and run it even on a phone with Termux installed.

---

## Help:

- Create a bot using [Bot Father](https://t.me/botfather).
- Get bot token.
- Get the chat id of the account to which the bot will send user messages. [Get telegram ID](https://t.me/my_id_bot).


- Clone the project.
- Go to the project folder.
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

- In the project folder, create a file `.env`

Contents of the .env file:

```env
PERSONAL_API_TOKEN="Your telegram bot token"
ADMIN_CHAT_ID="Your telegram chat id"
```


- Create a `config.json` file in the project folder, copy the data from the `config_example.json` file to the `.config.json` file.
- Replace the "Name" and "Description" lines in the `.config.json` file with the ones you need.

Example `.config.json`:

```json
{
    "name": "Smart Legion Lab",
    "description": "I am a developer specializing in creating web applications, libraries, console and graphical applications, as well as bots for Telegram and VK using Python.",
    "url": "https://smartlegionlab.github.io"
}
```

- Launching the bot: `python bot.py`

### Termux:

- Install Termux
- Run Termux app
- `termux-wake-lock`
- `pkg update`
- `pkg upgrade`
- `pkg install termux-tools`
- `pkg install python`
- `pkg install python-pip`
- `pkg install python-pip`
- `pkg install git`
- `pkg install vim`
- The problem with installing aiogram is solved by installing rust: `pkg install rust`
- Clone repo.
- Create a `.env` file.
- Create a `config.json` file.
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python bot.py`

> Now you don't need a server! Your Telegram bot is hosted and running right on your phone.

---

![LOGO](https://github.com/smartlegionlab/personal_telegram_bot/raw/master/data/images/personal_telegram_bot.png)

---

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------