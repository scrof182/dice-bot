# Read Me

## To Run Locally

* Download and install Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* Create a Discord bot account and add to channel: [https://discordpy.readthedocs.io/en/latest/discord.html](https://discordpy.readthedocs.io/en/latest/discord.html)
* In creds.py, change the TOKEN variable to your new discord token
* in the Dockerfile, change WORKDIR to the correct working directory
* Build and run in docker
  * `docker build -t dice-bot .`
  * `docker run -it --rm --name dice-bot-running dice-bot`

## Usage

Accepts `?` or `!` or `/` or \`\`\`\`\` as input

Can call bot with either `roll` or `r`

* Roll 1 die of any type  `/r d20`
* Roll 1 die of any type with a modifier `/r d20+3`
* Roll multiple dice `/r 3d20`
* Roll multiple dice with a modifier `/r 3d6+3`
* Roll with advantage `/r 2d20k1`
* Roll with disadvantage `/r 2d20l1`
* Roll with advantage/disadvantage with mods `/r 2d20k1+4`

