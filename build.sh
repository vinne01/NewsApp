# #!/usr/bin/env bash
# # exit on error
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate
# if [[ $CREATE_SUPERUSER ]];
# then
#   python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
# fi

#!/usr/bin/env bash

# exit on error
set -o errexit

# Check if the `requirements.txt` file exists
if [ ! -f "requirements.txt" ]; then
  echo "Error: requirements.txt not found!"
  exit 1
fi

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if manage.py exists before running Django commands
if [ ! -f "manage.py" ]; then
  echo "Error: manage.py not found!"
  exit 1
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "Applying migrations..."
python manage.py migrate

# Create superuser if requested and environment variable is set
if [[ $CREATE_SUPERUSER && -n "$DJANGO_SUPERUSER_EMAIL" ]]; then
  echo "Creating superuser..."
  python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
else
  echo "Superuser creation skipped."
fi

echo "Build completed successfully."

