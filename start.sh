if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Rajneesh058/finalmoviebot /finalmoviebot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /finalmoviebot
fi
cd /finalmoviebot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
