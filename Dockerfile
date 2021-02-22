FROM python:3

WORKDIR $working_dir

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "dice-bot.py" ]