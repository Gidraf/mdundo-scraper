release:bash ./release-tasks.sh


web: gunicorn examples:app

init: flask db init
migrate: flask db migrate
upgrade: flask db upgrade