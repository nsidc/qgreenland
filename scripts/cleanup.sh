docker-compose exec luigi python -c \
  'from qgreenland.util.misc import cleanup_output_dirs; cleanup_output_dirs(delete_fetch_dir=False)'
