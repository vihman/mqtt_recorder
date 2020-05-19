# mqtt_recorder
export PIPENV_VENV_IN_PROJECT="enabled"
pipenv install
ln -s .../config/etc/supervisor/conf.d/mqtt_recorder.conf /etc/supervisor/conf.d/
