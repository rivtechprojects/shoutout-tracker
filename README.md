**Shoutout Tracker**

Shoutout Tracker is a Discord bot I created as a fun way for teams to manage shoutouts to individual players for their contributions. It tracks how many days have passed since someone last had a shoutout, logs the reasons, and keeps a history of all the shoutouts for each player. What started as a simple tool for my own raid team in World of Warcraft turned into a fun and interactive project that I’m proud of.

---

## ✨ Features

- **📅 Track Days Since Last Shoutout**: Use the !recent command to see how long it’s been since a specific player last received a shoutout.
- **🔥 Log Shoutouts**: Use the !shoutout command to log a new shoutout for a player with a custom message and reset the counter.
- **Shoutout History**: Use the !history command to view a player's full shoutout history, including dates and reasons.
- **Team Management**: Add players to the team using the !addplayer command and list all players with !players.
- **Custom Messaging**: Add personalized messages when logging shoutouts to make the bot more fun and engaging.

---

## ⌨️ Commands

### ![CountGlorpula-1x](https://github.com/user-attachments/assets/e6d65b63-7583-4a2c-8368-1b4961601543) `!recent <player_name>`
- **What it does**: Tells you how many days it’s been since the specified player last received shoutout.
- **How to use it**: 
!recent Tank
- **Example response**:
It has been **3 days** since Tank received a shoutout for not falling over immediately on first pull.

---

### `!shoutout <player_name> <custom_message>`
- **What it does**: Logs a shoutout for the specified player with a custom message and resets the counter.
- **How to use it**: 
!shoutout Tank for not falling over immediately on first pull

### `!history <player_name>`
- **What it does**: Displays the full shoutout history for the specified player, including dates and reasons.
- **How to use it**: 
!history Tank
- **Example response**:
Tank received a shoutout for:
- 2025-04-29: pulling too many mobs
- 2025-04-30: not using cooldowns

### `!addplayer <player_name>`
- **What it does**: Adds a new player to the team.
- **How to use it**:
!addplayer Healer
- **Example response**:
Healer has been added to the team!

### `!players`
- **What it does**: Lists all players currently on the team.
- **How to use it**:
!players
- **Example response**:
Current team: Tank, Rogue, Healer

---

## 🚀 How to Set It Up

1. **🔑 Get Your Bot Token**  
   - Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and grab your token.

2. **📂 Set Up Your `.env` File**  
   - Create a file called `.env` in the root of the project and add your bot token:
     ```env
     DISCORD_TOKEN=your_discord_bot_token_here
     ```

3. **Install Dependencies**:
   - Install the required Python packages:
      ```
      pip install -r requirements.txt
      ```

4. **▶️ Run the Bot**  
   - Make sure your Python environment is ready, then run the bot script:
     ```bash
     python main.py
     ```

5. **Invite the bot to your server**:
   - Use the OAuth2 URL from the Discord Developer Portal to invite the bot to your server.

6. **Let the Shoutouts Begin**
   - Invite the bot to your server and start tracking those moments!

---

## 🎮 Why I Made This

As a competitive *Mythic Raider* and *Mythic+* player in *World of Warcraft*, I spend a lot of time working with teams and celebrating each other's contributions. Naturally, this creates plenty of opportunities to recognize and appreciate the efforts of teammates when things go right. This bot was created to track those moments and make it easier to give shoutouts, fostering a positive and fun team environment.

---

## 📜 License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

## 📸 Preview


